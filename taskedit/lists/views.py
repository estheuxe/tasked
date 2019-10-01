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

class ListView(APIView):

	def get(self, request):

		''' Получение всех листов '''

		type = request.GET.get('type')
		service = core.service(type)
		idBoard = request.GET.get('id')
		response = service.watchLists(idBoard)
		return Response(response)