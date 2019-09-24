from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings as s
from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
import requests
import json

trelloQS = {
	'fields': 'id,name,desc',
	'key': s.TRELLO_KEY,
	'token': s.TRELLO_TOKEN
}

class CardView(APIView):

	''' Все методы в случае успеха возвращают 200, кроме удаления. В нашем API я обработал доп. 201, 202 коды'''

	def get(self, request):

		''' Получение всех карт(задач) '''

		type = request.GET.get('type')

		if type == 'trello':
			idList = request.GET.get('id')
			response = requests.request('GET', s.URL_CARDS.format(id=idList), params=trelloQS)
			
			if response.status_code == 200:
				return Response({'cards': response.json()}, status=status.HTTP_200_OK)
			else:
				return Response(response.status_code)
		else:
			return Response(status=status.HTTP_400_BAD_REQUEST)

	def post(self, request):

		''' Создание карты(задачи) '''

		type = request.GET.get('type')

		if type == 'trello':
			idList = request.GET.get('id')
			cardName = request.GET.get('name')
			cardDesc = request.GET.get('desc')
			postTrelloCardQuery = {
				'idList': idList,
				'name': cardName,
				'desc': cardDesc,
				'key': s.TRELLO_KEY,
				'token': s.TRELLO_TOKEN
			}

			response = requests.request('POST', s.POST_TRELLO_URL, params=postTrelloCardQuery)
			
			if response.status_code == 200:
				return Response(status=status.HTTP_201_CREATED)
			else:
				return Response(response.status_code)
		else:
			return Response(status=status.HTTP_400_BAD_REQUEST)

	def put(self, request):

		''' Изменение определенной карты(задачи) '''

		type = request.GET.get('type')

		if type == 'trello':
			# при условии, что мы знаем id
			idCard = request.GET.get('id')
			newCardName = request.GET.get('name')
			newCardDesc = request.GET.get('desc')
			putTrelloCardQuery = {
				'name': newCardName,
				'desc': newCardDesc,
				'key': s.TRELLO_KEY,
				'token': s.TRELLO_TOKEN
			}

			response = requests.request('PUT', s.URL_FOR_CARD.format(id=idCard), params=putTrelloCardQuery)
			
			if response.status_code == 200:
				return Response(status=status.HTTP_202_ACCEPTED)
			else:
				return Response(response.status_code)
		else:
			return Response(status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request):

		''' Удаление определенной карты(задачи) '''

		type = request.GET.get('type')

		if type == 'trello':
			idCard = request.GET.get('id')
			response = requests.request('DELETE', s.URL_FOR_CARD.format(id=idCard), params={'key': s.TRELLO_KEY,'token': s.TRELLO_TOKEN})
			
			if response.status_code == 204:
				return Response(status=status.HTTP_204_NO_CONTENT)
			else:
				return Response(response.status_code)
		else:
			return Response(status=status.HTTP_400_BAD_REQUEST)

	def grab(self, request):
		
		''' Эта функция уйдет когда появятся вебхуки '''

		type = request.GET.get('type')

		if type == 'trello':
			infoTrelloCardQuery = {
				'fields': 'name,desc',
				'key': s.TRELLO_KEY,
				'token': s.TRELLO_TOKEN
			}
			idCard = request.GET.get('id')

			grabResp = requests.request('GET', s.URL_CARDS.format(id=idCard), params=infoTrelloCardQuery)

			''' to DB '''
			cardName = print(grabResp.json().get('name'))
			cardDesc = print(grabResp.json().get('desc'))