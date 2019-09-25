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

ytHeaders = {
	'Authorization': 'Bearer perm:cm9vdA==.NDYtMQ==.UQ5xwQt0IXO6fZUB5hGtRS1DulxQSN',
	'Accept': 'application/json',
	'Content-Type': 'application/json',
	'Cache-Control': 'no-cache'
}

class BoardView(APIView):
	
	def get(self, request):

		''' Получение всех досок '''

		type = request.GET.get('type')

		if type == 'trello':
			response = requests.request('GET', s.URL_BOARDS, params=trelloQS)

			if response.status_code == 200:
				return Response({'boards': response.json()}, status=status.HTTP_200_OK)
			else:
				return Response(response.status_code)
		elif type == 'yt':
			response = requests.request('GET', s.YT_URL_BOARDS, params={'fields': 'name,id'}, headers=ytHeaders)

			if response.status_code == 200:
				return Response({'boards': response.json()}, status=status.HTTP_200_OK)
			else:
				return Response(response.status_code)
		else:
			return Response(status=status.HTTP_400_BAD_REQUEST)