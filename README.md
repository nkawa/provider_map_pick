# provider_map_pick
Picking image map and send routing demand


- 地図上でクリックを2回すると、RouteDemand を発生
- RouteSupply を受け取って、地図上に表示する

動作させるためには、 Synerex 上に Routing Provider が必要

サンプル routing provider
- https://github.com/nkawa/provider_pgm_astar_routing

使用チャンネル
- ROUTING_SERVICE

使用プロトコル
- proto_cav

サブディレクトリ pyscript には、python から routing request を送る仕組みのサンプルあり。


