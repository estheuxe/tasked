from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings as s
from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
import requests
import json

ytHeaders = {
	'Authorization': 'Bearer perm:cm9vdA==.NDYtMQ==.UQ5xwQt0IXO6fZUB5hGtRS1DulxQSN',
	'Accept': 'application/json',
	'Content-Type': 'application/json',
	'Cache-Control': 'no-cache'
}

class CardView(APIView):

	''' Все методы в случае успеха возвращают 200, кроме удаления. В нашем API я обработал доп. 201, 202 коды'''

	def get(self, request):

		''' Получение всех карт(задач) '''

		type = request.GET.get('type')

		if type == 'trello':
			trelloQS = {
				'fields': 'id,name,desc',
				'key': s.TRELLO_KEY,
				'token': s.TRELLO_TOKEN
			}
			
			idList = request.GET.get('id')

			response = requests.request('GET', s.URL_CARDS.format(id=idList), params=trelloQS)
			
			if response.status_code == 200:
				return Response({'cards': response.json()}, status=status.HTTP_200_OK)
			else:
				return Response(response.status_code)
		elif type == 'yt':
			ytCardFields = {
				'fields': 'id,summary,name,description,reporter(login)'
			}

			response = requests.request('GET', s.YT_URL_CARDS, params=ytCardFields, headers=ytHeaders)

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

		if type == 'yt':
			idBoard = request.GET.get('id')
			cardName = request.GET.get('name')
			cardDesc = request.GET.get('desc')
			ytCardFields = {
				'fields': 'idReadable'
			}
			ytJson = {
				'summary': cardName,
				'description': cardDesc,
				'project': {
					'id': idBoard,
				}
			}

			response = requests.request('POST', s.YT_URL_CARDS, params=ytCardFields, headers=ytHeaders, json=ytJson)
			
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
		elif type == 'yt':
			idCard = request.GET.get('id')
			newCardName = request.GET.get('name')
			newCardDesc = request.GET.get('desc')
			ytJson = {
				'summary': newCardName,
				'description': newCardDesc
			}

			# у них почему-то на изменение POST request
			response = requests.request('POST', s.YT_URL_CARD_EDIT.format(id=idCard), headers=ytHeaders, json=ytJson)

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
		elif type == 'yt':
			idCard = request.GET.get('id')

			response = requests.request('DELETE', s.YT_URL_CARD_EDIT.format(id=idCard), headers=ytHeaders)

			if response.status_code == 200:
				return Response(status=status.HTTP_204_NO_CONTENT)
			else:
				return Response(response.status_code)
		else:
			return Response(status=status.HTTP_400_BAD_REQUEST)