
## Python からの routing を実行するためのサブコマンド
#### by N.Kawaguchi 2021/12/30

```
git clone https://github.com/nkawa/provider_map_pick.git

cd provider_map_pick/pyscript

git submodule update --init --recursive

pip install grpcio-tools
pip install futures
pip install protobuf3
```

### 開発時には以下が必要
```
python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. ./api/synerex.proto
python -m grpc_tools.protoc -I. --python_out=.  ./cav/cav.proto
```

ただし、原状は上記は不要（すでに実行済み）
Synerex NodeServer / SynerexServer の起動が必要

proxy provider を動かす必要があり。
* https://github.com/synerex/provider_proxy

また、ルーティングプロバイダとして以下を動かす
* https://github.com/nkawa/provider_pgm_astar_routing


その上で python から呼び出しが可能

実行例：
```
python route_request.py 142 388 188 446

⇒ pixel 上での XY 座標で示される
```

以下のように config ファイルを指定すると、座標変換を行う
```
python route_request.py --config higashi.json 142 388 188 446
```
higashi.json ファイルの中の MinLon, 及び MaxLat , Scale のみを利用している
