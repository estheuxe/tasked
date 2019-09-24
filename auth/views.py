from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Card
from .serializers import CardSerializer

import webbrowser
import requests
import json

appId = '11630581252b45c8b3d7459720ed2af1'
appPw = 'c200a37d97064c03ab55b1a1a5a28402'
trelloKey = '27138010bc3a442737533781e5029962'
trelloToken = '0ab806b21beb8db46ff186fb60c364843b541b100249ba7d36cc41f35472ca93'

url = 'https://oauth.yandex.ru/authorize?response_type=token&client_id=' + appId
urlForCard = 'https://api.trello.com/1/cards/{id}'
urlCards = 'https://api.trello.com/1/lists/{id}/cards'
urlLists = 'https://api.trello.com/1/boards/{id}/lists'
urlBoards = 'https://api.trello.com/1/members/me/boards'
postTrelloUrl = 'https://api.trello.com/1/cards'

#idList = '5d81c5e68f079e461725ca0b'
#idBoard = '5d81c5e6ecf65d36ef777b70'

trelloQS = {
	'fields': 'id,name,desc',
	'key': trelloKey,
	'token': trelloToken
}

def index(request):
	
	uriWH = "https://api.trello.com/1/tokens/{APIToken}/webhooks/?key={APIKey}"

	paramsForWH = {
		#'callbackURL': 'http://127.0.0.1:1337',
		'callbackURL':  'https://449c6702.ngrok.io/auth/',
		'idModel': '5d81c5e68f079e461725ca0b',
		'description': 'First Webhook',
	}

	answwh = requests.request("POST", uriWH.format(APIToken=trelloToken, APIKey=trelloKey), params=paramsForWH)

	return HttpResponse(answwh.status_code)
	
	#cards = Card.objects.all()
	#return render(request, 'index.html', {'cards': cards})	

	'''
	Yandex Tracker 
	webbrowser.open(url)
	return HttpResponse("auth page")
	'''

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

''' serializer method
class CardView(APIView):
	def get(self, request):
		cards = Card.objects.all()
		serializer = CardSerializer(cards, many=True)
		return Response({"cards": serializer.data})
'''

class CardView(APIView):

	def get(self, request):

		type = request.GET.get('type')

		if type == 'trello':

			idList = request.GET.get('id')

			response = requests.request("GET", urlCards.format(id=idList), params=trelloQS)

			return Response({"cards": response.json()}, status=status.HTTP_200_OK)

		else:

			return Response(status=status.HTTP_400_BAD_REQUEST)

	def post(self, request):

		type = request.GET.get('type')

		if type == 'trello':

			idList = request.GET.get('id')
			cardName = request.GET.get('name')
			cardDesc = request.GET.get('desc')

			postTrelloCardQuery = {
				'idList': idList,
				'name': cardName,
				'desc': cardDesc,
				'key': trelloKey,
				'token': trelloToken
			}

			requests.request("POST", postTrelloUrl, params=postTrelloCardQuery)

			return Response(status=status.HTTP_201_CREATED)

		else:

			return Response(status=status.HTTP_400_BAD_REQUEST)

	def put(self, request):

		type = request.GET.get('type')

		if type == 'trello':

			# при условии, что мы знаем id
			idCard = request.GET.get('id')
			newCardName = request.GET.get('name')
			newCardDesc = request.GET.get('desc')

			putTrelloCardQuery = {
				'name': newCardName,
				'desc': newCardDesc,
				'key': trelloKey,
				'token': trelloToken
			}

			requests.request("PUT", urlForCard.format(id=idCard), params=putTrelloCardQuery)

			return Response(status=status.HTTP_202_ACCEPTED)

		else:

			return Response(status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request):

		type = request.GET.get('type')

		if type == 'trello':

			idCard = request.GET.get('id')

			requests.request("DELETE", urlForCard.format(id=idCard), params={'key': trelloKey,'token': trelloToken})

			return Response(status=status.HTTP_204_NO_CONTENT)

		else:

			return Response(status=status.HTTP_400_BAD_REQUEST)

	def grab(self, request):
		
		type = request.GET.get('type')

		if type == 'trello':

			infoTrelloCardQuery = {
				'fields': 'name,desc',
				'key': trelloKey,
				'token': trelloToken
			}

			idCard = request.GET.get('id')

			grabResp = requests.request("GET", urlCards.format(id=idCard), params=infoTrelloCardQuery)

			''' to DB '''
			cardName = print(grabResp.json().get('name'))
			cardDesc = print(grabResp.json().get('desc'))

			return Response("{0}:{1}".format(cardName,cardDesc), status.HTTP_200_OK)

		else:

			return Response(status=status.HTTP_400_BAD_REQUEST)

class ListView(APIView):

	def get(self, request):

		type = request.GET.get('type')

		if type == 'trello':

			idBoard = request.GET.get('id')

			response = requests.request("GET", urlLists.format(id=idBoard), params=trelloQS)

			return Response({"lists": response.json()}, status=status.HTTP_200_OK)

		else:

			return Response(status=status.HTTP_400_BAD_REQUEST)

class BoardView(APIView):

	def get(self, request):

		type = request.GET.get('type')

		if type == 'trello':

			response = requests.request("GET", urlBoards, params=trelloQS)

			return Response({"boards": response.json()}, status=status.HTTP_200_OK)

		else:

			return Response(status=status.HTTP_400_BAD_REQUEST)