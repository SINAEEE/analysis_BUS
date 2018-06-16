
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




from collect.api import json_request as jr

url ='http://ws.bus.go.kr/api/rest/busRouteInfo/getRouteInfo?ServiceKey=L67Cl24axIN5YZAkFU4c9ZVT3%2B%2FS8nzuC%2FDCnoEpzgFZKHkq%2B0vGkNeNbnYbhmLRtnkmzxyNOnwT9RdcFULAGA%3D%3D&busRouteId=100100112'


#1 방식
json_result = jr.json_request(url)
print(json_result)
