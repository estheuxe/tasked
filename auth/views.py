from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Card
from .serializers import CardSerializer

import webbrowser
import requests

appId = '11630581252b45c8b3d7459720ed2af1'
appPw = 'c200a37d97064c03ab55b1a1a5a28402'
trelloKey = '27138010bc3a442737533781e5029962'
trelloToken = '0ab806b21beb8db46ff186fb60c364843b541b100249ba7d36cc41f35472ca93'

url = 'https://oauth.yandex.ru/authorize?response_type=token&client_id=' + appId
urlLists = 'https://api.trello.com/1/lists/{id}/cards'
urlBoards = 'https://api.trello.com/1/boards/{id}/lists'

trelloQS = {
	'fields': 'id,name',
	'key': trelloKey,
	'token': trelloToken
}

def index(request):
	cards = Card.objects.all()
	return render(request, 'index.html', {'cards': cards})
	'''
	Yandex Tracker 
	webbrowser.open(url)
	return HttpResponse("auth page")
	'''
def gettoken(request):
	currUrl = request.get_full_path()
	return HttpResponse(currUrl)

def create(request):
	if request.method == 'POST':
		foo = Card()
		foo.name = request.POST.get('name')
		foo.desc = request.POST.get('desc')
		foo.save()
	return HttpResponseRedirect('/auth/')

def delete(request):
	Card.objects.all().delete()
	return HttpResponseRedirect('/auth/')

'''
class CardView(APIView):
	def get(self, request):
		cards = Card.objects.all()
		serializer = CardSerializer(cards, many=True)
		return Response({"cards": serializer.data})
'''

''' localhost:1337/auth/cards?type= trello|yandex '''

class CardView(APIView):
	def get(self, request):
		type = request.GET.get('type')
		if type == 'trello':
			#id nado kak-to dostavat'
			idList = '5d81c5e68f079e461725ca0b'
			response = requests.request("GET", urlLists.format(id=idList), params=trelloQS)
			return Response({"cards": resp.json()})

class BoardView(APIView):
	def get(self, request):
		type = request.GET.get('type')
		if type == 'trello':
			#id nado kak-to dostavat'
			idBoard = '5d81c5e6ecf65d36ef777b70'
			response = requests.request("GET", urlBoards.format(id=idBoard), params=trelloQS)
			return Response({"lists": response.json()})

'''
class HandleGetRequest(object):
	def foo(url, id, request):

		type = request.GET.get('type')

		if request.GET.get('type') == 'trello':
			trello(url, id, request)
		elif request.GET.get('type') == 'yandex':
			return HttpResponseRedirect('/auth/')
		else:
			cards = Card.objects.all()
			return render(request, 'index.html', {'cards': cards})

	def trello(url, id, request):
		response = requests.request("GET", url.format(id=id), params=trelloQS)
		return response
'''