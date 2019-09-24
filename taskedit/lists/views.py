from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings as s
from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
import requests
import json

#idList = '5d81c5e68f079e461725ca0b'
#idBoard = '5d81c5e6ecf65d36ef777b70'

trelloQS = {
	'fields': 'id,name,desc',
	'key': s.TRELLO_KEY,
	'token': s.TRELLO_TOKEN
}

class ListView(APIView):

	def get(self, request):

		''' Получение всех листов '''

		type = request.GET.get('type')

		if type == 'trello':
			idBoard = request.GET.get('id')
			response = requests.request("GET", s.URL_LISTS.format(id=idBoard), params=trelloQS)
			return Response({"lists": response.json()}, status=status.HTTP_200_OK)
		else:
			return Response(status=status.HTTP_400_BAD_REQUEST)
