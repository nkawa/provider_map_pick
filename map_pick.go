package main

import (
	"encoding/json"
	"flag"
	"log"
	"net/http"
	"os"
	"path"
	"path/filepath"
	"strings"
	"sync"
	"time"

	"github.com/gin-gonic/gin"
	"go.opentelemetry.io/otel/trace"
	"google.golang.org/protobuf/proto"

	sxcav "github.com/synerex/proto_cav"
	sxapi "github.com/synerex/synerex_api"
	sxproto "github.com/synerex/synerex_proto"
	sxutil "github.com/synerex/synerex_sxutil"

	"github.com/gorilla/websocket"
	//	"go.opentelemetry.io/otel"//
	//	"go.opentelemetry.io/otel/trace"
)

var (
	nodesrv         = flag.String("nodesrv", "127.0.0.1:9990", "Node ID Server")
	robotId         = flag.Int("robotid", 0, "Robot ID")
	localsx         = flag.String("local", "", "Local Synerex Server")
	mu              sync.Mutex
	tracer          trace.Tracer
	sxServerAddress string
	mainWs          *WSServ
	requestSeq      = int64(0)
	sxClient        *sxutil.SXServiceClient
)

// Route Callback

func routeCallback(clt *sxutil.SXServiceClient, sp *sxapi.Supply) {
	if sp.SenderId == uint64(clt.ClientID) {
		// ignore my message.
		return
	}
	if sp.SupplyName == "SupplyRoute" {
		rcd := &sxcav.Path{}
		err := proto.Unmarshal(sp.Cdata.Entity, rcd)
		if err != nil {
			log.Print(err)
		}
		log.Printf("[INFO/robot] receive route robot %d", rcd.RobotId)
		//		id := int(rcd.RobotId)
		/*
			if rob, ok := robotList[id]; ok {
				rob.SetPath(rcd)
				jsonbyte, err := robot.MakePathMsg(rcd)
				if err != nil {
					log.Print(err)
				} else {
					robot.SendPath(id, jsonbyte, syMqttClient)
				}
			}
		*/
	}
}

/* Websocket clients */

type WClient struct {
	ws   *WSServ
	conn *websocket.Conn
	send chan []byte
}

type WSServ struct {
	clients    map[*WClient]bool // connected cilents
	register   chan *WClient
	unregister chan *WClient
	broadcast  chan []byte
}

func NewWSServ() *WSServ {
	return &WSServ{
		broadcast:  make(chan []byte),
		clients:    make(map[*WClient]bool),
		register:   make(chan *WClient),
		unregister: make(chan *WClient),
	}
}

// main goroutine for Terminal server
func (ws *WSServ) run() {

	for {
		select {
		case client := <-ws.register:
			ws.clients[client] = true
		case client := <-ws.unregister:
			if _, ok := ws.clients[client]; ok {
				delete(ws.clients, client)
				close(client.send)
			}
		case message := <-ws.broadcast: // broadcasting to all clients.
			log.Printf("Broadcasting!", message, len(ws.clients))
			for client := range ws.clients {
				select { // non-blocking send
				case client.send <- message:
				default:
					close(client.send)
					delete(ws.clients, client)
				}
			}
		}
	}
}

const (
	// Time allowed to write a message to the peer.
	writeWait = 10 * time.Second
	// Time allowed to read the next pong message from the peer.
	pongWait = 60 * time.Second
	// Send pings to peer with this period. Must be less than pongWait.
	pingPeriod = (pongWait * 9) / 10
	// Maximum message size allowed from peer.
	maxMessageSize = 512
)

type XYinfo []struct {
	X int `json:"x"`
	Y int `json:"y"`
}

func (c *WClient) messageHandler(msg []byte) {
	// handling message from client
	str := string(msg)
	log.Printf("get message[%s]", str)
	cmds := strings.Split(str, "!")

	if cmds[0] == "click2" {
		log.Printf("Got click2")
		var sd XYinfo // source and destination
		json.Unmarshal([]byte(cmds[1]), &sd)
		//		log.Printf("x0,y0,x1,y1", sd[0].X, sd[0].Y, sd[1].X, sd[1].Y)
		// routing request!
		rcd := sxcav.PathRequest{
			RobotId: int64(*robotId),
			Seq:     requestSeq,
			Start: &sxcav.Point{
				X: float32(sd[0].X),
				Y: float32(sd[0].Y),
			},
			Goal: &sxcav.Point{
				X: float32(sd[1].X),
				Y: float32(sd[1].Y),
			},
		}
		requestSeq += 1
		out, err := proto.Marshal(&rcd)
		if err != nil {
			log.Print(err)
		}
		cout := sxapi.Content{Entity: out}
		smo := sxutil.SupplyOpts{
			Name:  "RouteDemand",
			Cdata: &cout,
		}
		_, err = sxClient.NotifySupply(&smo)
		if err != nil {
			log.Print(err)
			//			sxutil.reconnectClient(sxClient, sxServerAddress, &mu)
		} else {
			log.Printf("send dest request robot%d from (%f, %f) to (%f, %f)", *robotId, rcd.Start.X, rcd.Start.Y, rcd.Goal.X, rcd.Goal.Y)
		}

	}

	switch str {
	case "getall":

	}

}

// read client message each terminals.
func (c *WClient) readPump() {
	defer func() {
		c.ws.unregister <- c
		c.conn.Close()
	}()
	c.conn.SetReadLimit(maxMessageSize)
	c.conn.SetReadDeadline(time.Now().Add(pongWait))
	c.conn.SetPongHandler(func(string) error { c.conn.SetReadDeadline(time.Now().Add(pongWait)); return nil })
	for {
		_, message, err := c.conn.ReadMessage()
		if err != nil {
			if websocket.IsUnexpectedCloseError(err, websocket.CloseGoingAway, websocket.CloseAbnormalClosure) {
				log.Printf("TS websocket error: %v", err)
			}
			break
		}
		//		go c.ws.messageHandler(message)
		go c.messageHandler(message)
		//		go c.ws.messageHandler(message)
	}
}
func (c *WClient) writePump() {
	ticker := time.NewTicker(pingPeriod)
	defer func() {
		ticker.Stop()
		c.conn.Close()
	}()
	for {
		select {
		case message, ok := <-c.send:
			c.conn.SetWriteDeadline(time.Now().Add(writeWait))
			if !ok {
				// The hub closed the channel.
				c.conn.WriteMessage(websocket.CloseMessage, []byte{})
				return
			}

			w, err := c.conn.NextWriter(websocket.TextMessage)
			if err != nil {
				return
			}
			w.Write(message)

			// Add queued chat messages to the current websocket message.
			n := len(c.send) //
			for i := 0; i < n; i++ {
				w.Write(<-c.send)
			}

			if err := w.Close(); err != nil {
				return
			}
		case <-ticker.C:
			c.conn.SetWriteDeadline(time.Now().Add(writeWait))
			if err := c.conn.WriteMessage(websocket.PingMessage, nil); err != nil {
				return
			}
		}
	}
}

var upgrader = websocket.Upgrader{
	ReadBufferSize:  1024,
	WriteBufferSize: 1024,
}

func servWS(ws *WSServ, w http.ResponseWriter, r *http.Request) {
	conn, err := upgrader.Upgrade(w, r, nil)
	if err != nil {
		log.Println(err)
		return
	}
	client := &WClient{ws: ws, conn: conn, send: make(chan []byte, 256)}
	log.Printf("WS Connected:%#v", client)
	ws.register <- client

	// Allow collection of memory referenced by the caller by doing all work in
	// new goroutines.
	go client.writePump()
	go client.readPump()
}

func index(ctx *gin.Context) {
	log.Printf("Get index: %#v", ctx)
	ctx.Header("Access-Control-Allow-Origin", "*")
	ctx.HTML(200, "index.html", gin.H{"data": "Hello"})
}

// Map Pick provider main
func main() {
	flag.Parse()
	go sxutil.HandleSigInt()
	sxutil.RegisterDeferFunction(sxutil.UnRegisterNode)
	log.Printf("Map Pick Provider(%s) built %s sha1 %s", sxutil.GitVer, sxutil.BuildTime, sxutil.Sha1Ver)

	channels := []uint32{sxproto.MQTT_GATEWAY_SVC, sxproto.ROUTING_SERVICE}

	var rerr error
	sxServerAddress, rerr = sxutil.RegisterNode(*nodesrv, "MapPicker", channels, nil)
	if rerr != nil {
		log.Fatal("Can't register node:", rerr)
	}

	// this is for OLTP. OpenTelemetry Protocol.
	/*
		tp := sxutil.NewOltpTracer() // this enables default tracer!
		defer func() {
			log.Printf("Closing oltp traceer")
			if err := tp.Shutdown(context.Background()); err != nil {
				log.Printf("Can't shoutdown tracer %v", err)
			}
		}()
		tracer = otel.Tracer("map_picker", trace.WithInstrumentationVersion("0.0.1"))
		log.Printf("Tracer generated %#v", tracer)
	*/
	if *localsx != "" { // quick hack for AWS local network
		sxServerAddress = *localsx
	}
	log.Printf("Connecting SynerexServer at [%s]", sxServerAddress)

	wg := sync.WaitGroup{} // for syncing other goroutines

	client := sxutil.GrpcConnectServer(sxServerAddress)

	if client == nil {
		log.Fatal("Can't connect Synerex Server")
	} else {
		log.Print("Connecting SynerexServer")
	}

	sxClient = sxutil.NewSXServiceClient(client, sxproto.ROUTING_SERVICE, "{Client:MapPicker}")

	wg.Add(1)
	log.Print("Subscribe Supply")
	//	go subscribeOrderSupply(geClient)

	router := gin.Default()
	execBin, _ := os.Executable()
	execPath := filepath.Dir(execBin)
	templatePath := path.Join(execPath, "templates/*.html")
	log.Printf("TemplatePath: %s", templatePath)
	router.Static("/static", "./static")
	router.LoadHTMLGlob(templatePath)

	router.GET("/menu", func(c *gin.Context) {
		log.Printf("Get from %#v", c)
		c.Header("Access-Control-Allow-Origin", "*")
		c.Data(http.StatusOK, "text/html; charset=utf-8", []byte("getMenu"))
		//		index(c)
	})

	mainWs = NewWSServ() // web socket server
	// for websocket
	router.GET("/ws", func(c *gin.Context) {
		servWS(mainWs, c.Writer, c.Request)
	})
	go mainWs.run()

	router.GET("/", index)
	router.Run(":8081")

	wg.Wait()

}
