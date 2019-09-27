from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings as s
from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from abc import ABC, abstractmethod
import requests
import json

class Taskedit():
	def __init__(self, type):
		self.type = type

	def newStrategy(self):
		if self.type == 'trello':
			return Context(TrelloStrategy())

		elif self.type == 'yt':
			return Context(YtStrategy())

		else:
			return Response(status=status.HTTP_400_BAD_REQUEST)

class BoardView(APIView):
	def get(self, request):

		type = request.GET.get('type')

		getStrategy = Taskedit(type).newStrategy()

		return getStrategy.getResp()

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
		response = self._strategy.get()
		if response.status_code == 200:
			return Response(response.json(), status=status.HTTP_200_OK)
		else:
			return Response(response.status_code)

class Strategy(ABC):
	@abstractmethod
	def get(self):
		pass

class TrelloStrategy(Strategy):
	def get(self):
		trelloQs = {
			'fields': 'id,name,desc',
			'key': s.TRELLO_KEY,
			'token': s.TRELLO_TOKEN
		}
		response = requests.request('GET', s.URL_BOARDS, params=trelloQs)
		return response

class YtStrategy(Strategy):
	def get(self):
		ytQs = {
			'fields': 'id,name'
		}
		response = requests.request('GET', s.YT_URL_BOARDS, params=ytQs, headers=s.YT_HEADERS)
		return response