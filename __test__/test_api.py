
from collect.api import api as bapi

"""
result = bapi.bus_gen_url(
          busRouteId=100100112,
          #busRouteNm=721,
          #length="",
          #routeType="",
          #stStationNm="",
          #term="",
          #lastBusYn="",
          _type='json'
)
print(result)
"""
"""
#1. 노선기본정보항목조회 (매개변수 : 검색할노선번호)
results = bapi.bus_fetch_basic_info(busRouteId=100100112)
print(results)
"""

#2. 노선번호에 해당하는 노선목록 조회
results = bapi.bus_fetch_get_bus_route_list(busRouteId=1)
print(results)


"""
##xml -> loads.json 예제

from collect.api import json_request as jr

url ='http://ws.bus.go.kr/api/rest/busRouteInfo/getRouteInfo?ServiceKey=L67Cl24axIN5YZAkFU4c9ZVT3%2B%2FS8nzuC%2FDCnoEpzgFZKHkq%2B0vGkNeNbnYbhmLRtnkmzxyNOnwT9RdcFULAGA%3D%3D&busRouteId=100100112'

json_result = jr.json_request(url)
print(json_result)
"""