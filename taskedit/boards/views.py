from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings as s
from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from abc import ABC, abstractmethod
import requests
import json

import sys,os
sys.path.insert(0,os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import core

class BoardView(APIView):
	def get(self, request):

		''' Получение всех досок '''

		type = request.GET.get('type')
		service = core.service(type)
		response = service.watchBoards()
		return Response(response.json())#, status=status.HTTP_200_OK)