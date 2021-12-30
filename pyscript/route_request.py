import grpc
import time
import json
import random
import sxutil
import sys
import argparse
import synerex_pb2
import synerex_pb2_grpc
import cav_pb2
from google.protobuf.timestamp_pb2 import Timestamp


ns = []
config = {}

def readConfig(configFile):
    global config
    with open(configFile) as f:
        str = f.read()
        config = json.loads(str) 
    
# only valid under 1000!!
def rand_ints_nodup():
    while True:
        global ns
        n = random.randint(0, 1000)
        if not n in ns:
            ns.append(n)
            break
    return n

# synerex （上のrouting provider )から結果が返ってくる
def routeCallback(clt, supply):
    rawPath = supply.cdata.entity
#    print("Got Route Supply Data:",supply.supply_name, rawPath)
    path = cav_pb2.Path()
    path.ParseFromString(supply.cdata.entity)
#    print("Parsed",path)
        
# 
    if len(config) > 0:
        cx = config["MinLon"]
        cy = config["MaxLat"]
        sc = config["Scale"]
        for pt in path.path:            
            print(pt.seq, ",", cx+(pt.pose.x*sc),",", cy-(pt.pose.y*sc))
        
    else: # make conversion
        for pt in path.path:
            print(pt.seq, ",", pt.pose.x,",", pt.pose.y)
        
                
    sys.exit()

def routeRequest(x0,y0,x1,y1):
    channels = [5]           # ROUTING_SVC
    srv = 'localhost:18000'  # proxy provider
#    sxutil.log(srv)
    with grpc.insecure_channel(srv) as channel:
#        sxutil.log("Connecting Synerex Server: "+srv)
        client = synerex_pb2_grpc.SynerexStub(channel)
        sxClient = sxutil.SXServiceClient(client, 5, '')        
        timestamp = Timestamp()
        preq = cav_pb2.PathRequest(start = cav_pb2.Point(x=x0,y=y0),
                                   goal = cav_pb2.Point(x=x1,y=y1))
        preqBin = preq.SerializeToString()
                
        dm = synerex_pb2.Demand(id=rand_ints_nodup(), 
                                sender_id=sxClient.ClientID, 
                                channel_type=sxClient.ChannelType, 
                                demand_name="RouteDemand",
                                cdata=synerex_pb2.Content(entity=preqBin),
                                ts=timestamp)
        resp = client.NotifyDemand(dm)
#        print("Notify Supply!",resp)
        sxClient.SubscribeSupply(routeCallback)
        print("Subscribe end")
    
    
def run():
    parser = argparse.ArgumentParser(description = 'Synerex Routing Interface')
    parser.add_argument('points', metavar='PT', type=float, nargs=4)
#    parser.add_argument('--projection', default='pixel')
    parser.add_argument('--config', default='')
    
    args = parser.parse_args()
    
    if args.config != '':
        readConfig(args.config)
        
    routeRequest(args.points[0],args.points[1],args.points[2],args.points[3])
    
    
    
if __name__ == '__main__':
    run()
    