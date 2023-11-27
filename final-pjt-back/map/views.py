from django.shortcuts import render
import requests
from rest_framework.response import Response
from django.conf import settings
from rest_framework.decorators import api_view
import folium
# Create your views here.
@api_view(['GET'])
def index(request): # type: ignore
    # 외부에 노출되지 않도록 내 pc에만 관리하는 변수 : 환경 변수
    # url = "정기예금 API"
    # 이거 검색해서 넘겨야 함.
    # print(request)
    # print(request.path)
    # print(request.__dict__)
    url = f'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=36.1081844,128.4139686&radius=1000&type=bank&keyword=%EC%9D%80%ED%96%89&key=AIzaSyCRQecy4yCB4ZNyFdWzyx_HQRitFaXwqPI'
    # map_osm = folium.Map(location = [37.559978, 126.975291], zoom_start = 16)
    # map_osm
    response = requests.get(url).json()
    return Response(response)


# Create your views here.
@api_view(['GET'])
def proxy(request, path): # type: ignore
    # 외부에 노출되지 않도록 내 pc에만 관리하는 변수 : 환경 변수
    # url = "정기예금 API"
    # 이거 검색해서 넘겨야 함.
    # print(request)
    # print(request.path)
    # print(path)
    # print(request.request)
    url = f'https://maps.googleapis.com' + request.get_full_path()
    print(url)
    # map_osm = folium.Map(location = [37.559978, 126.975291], zoom_start = 16)
    # map_osm
    response = requests.get(url).json()
    return Response(response)


