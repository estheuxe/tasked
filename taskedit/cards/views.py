from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings as s
from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
import requests
import json

import sys,os
sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import core

class CardView(APIView):

	def get(self, request):

		''' Получение информации обо всех картах(задачах) '''

		type = request.GET.get('type')
		service = core.service(type)
		idList = request.GET.get('id')
		response = service.watchCards(idList)
		return Response(response)

	def post(self, request):

		''' Создание карты(задачи) '''

		type = request.GET.get('type')
		service = core.service(type)
		idList = request.GET.get('id')
		cardName = request.GET.get('name')
		cardDesc = request.GET.get('desc')
		project = requests.GET.get('project')
		if project != None:
			response = service.createCard(idList,cardName,cardDesc,project)
		else:
			response = service.createCard(idList,cardName,cardDesc)
		return Response(response.json())

	def put(self, request):

		''' Изменение определенной карты(задачи) '''

		type = request.GET.get('type')
		service = core.service(type)
		idCard = request.GET.get('id')
		newCardName = request.GET.get('name')
		newCardDesc = request.GET.get('desc')
		response = service.updateCard(idCard,newCardName,newCardDesc)
		return Response(response.json())

	def delete(self, request):

		''' Удаление определенной карты(задачи) '''

		type = request.GET.get('type')
		service = core.service(type)
		idCard = request.GET.get('id')
		response = service.removeCard(idCard,newCardName,newCardDesc)
		return Response(response.json())