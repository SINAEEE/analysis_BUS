
from urllib.parse import urlencode
from .json_request import json_request


ENDPOINT = "http://ws.bus.go.kr/api/rest/busRouteInfo/getRouteInfo"
SERVICE_KEY ="L67Cl24axIN5YZAkFU4c9ZVT3%2B%2FS8nzuC%2FDCnoEpzgFZKHkq%2B0vGkNeNbnYbhmLRtnkmzxyNOnwT9RdcFULAGA%3D%3D"



def bus_gen_url(endpoint=ENDPOINT, service_key=SERVICE_KEY, **params):
    url = '%s?ServiceKey=%s&%s' % (endpoint, service_key, urlencode(params))
    return url


def bus_fetch_info(busRouteId=""):
    url = bus_gen_url(
        busRouteId=busRouteId,
        _type='json'
    )
    #print(url)
    #json_result = json_request(url=url)
    #print(json_result)


