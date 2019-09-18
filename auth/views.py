from django.shortcuts import render
from django.http import HttpResponse
import webbrowser

appId = '11630581252b45c8b3d7459720ed2af1'
appPw = 'c200a37d97064c03ab55b1a1a5a28402'

url = 'https://oauth.yandex.ru/authorize?response_type=token&client_id=' + appId

def index(request):
	webbrowser.open(url)
	return HttpResponse("auth page")

def gettoken(request):
	currUrl = request.get_full_path()
	return HttpResponse(currUrl)