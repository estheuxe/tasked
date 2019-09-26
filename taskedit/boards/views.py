from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings as s
from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from abc import ABC, abstractmethod
import requests
import json

class BoardView(APIView):
	def get(self, request):

		resp = Context(TrelloStrategy())

		type = request.GET.get('type')

		if type == 'trello':

			return resp.getResp()

		elif type == 'yt':

			resp.strategy = YtStrategy()
			
			return resp.getResp()

		else:
			
			return Response(status=status.HTTP_400_BAD_REQUEST)

''' applying the pattern "Strategy" '''

class Context():
	def __init__(self, strategy: 'Strategy') -> None:
		self._strategy = strategy

	@property
	def strategy(self) -> 'Strategy':
		return self._strategy

	@strategy.setter
	def strategy(self, strategy: 'Strategy') -> None:
		self._strategy = strategy

	def getResp(self) -> 'Response':
		response = self._strategy.foo()
		if response.status_code == 200:
			return Response({'boards': response.json()}, status=status.HTTP_200_OK)
		else:
			return Response(response.status_code)

class Strategy(ABC):
	@abstractmethod
	def foo(self):
		pass

class TrelloStrategy(Strategy):
	def foo(self):
		trelloQs = {
			'fields': 'id,name,desc',
			'key': s.TRELLO_KEY,
			'token': s.TRELLO_TOKEN
		}
		response = requests.request('GET', s.URL_BOARDS, params=trelloQs)
		return response

class YtStrategy(Strategy):
	def foo(self):
		ytQs = {
			'fields': 'id,name'
		}
		response = requests.request('GET', s.YT_URL_BOARDS, params=ytQs, headers=s.YT_HEADERS)
		return response