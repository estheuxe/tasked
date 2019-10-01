from abc import ABC, abstractmethod
from django.conf import settings as s
import requests
import json

def service(type):
	if type == 'trello':
		return Trello()

	elif type == 'yt':
		return Yt()

	return Taskedit()

class Taskedit(ABC):

	''' Класс не используется явно '''

	@abstractmethod
	def watchBoards(self):
		pass

	def watchLists(self, idBoard):
		pass

	def watchCards(self, idList):
		pass

	def createCard(self, idList, cardName, cardDesc):
		pass

	def updateCard(self, idCard, newCardName, newCardDesc):
		pass

	def removeCard(self, idCard):
		pass

class Trello(Taskedit):
	trelloQs = {
		'fields': 'id,name,desc',
		'key': s.TRELLO_KEY,
		'token': s.TRELLO_TOKEN
	}

	def orderer(resp):
		dt = []

		for entity in resp.json():
			xid = entity.get('id')
			xname = entity.get('name')
			dt.append({'id': xid, 'name': xname})

		return dt

	def watchBoards(self):
		response = requests.request('GET', s.TRELLO_URL_BOARDS, params=Trello.trelloQs)
		orderedList = Trello.orderer(response)

		return {'Boards': orderedList}

	def watchLists(self, idBoard):
		self.idBoard = idBoard
		response = requests.request('GET', s.TRELLO_URL_LISTS.format(id=self.idBoard), params=Trello.trelloQs)
		orderedList = Trello.orderer(response)

		return {'Lists': orderedList}

	def watchCards(self, idList):
		self.idList = idList
		response = requests.request('GET', s.TRELLO_URL_CARDS.format(id=self.idList), params=Trello.trelloQs)
		orderedList = Trello.orderer(response)

		return {'Cards': orderedList}

	def createCard(self, idList, cardName, cardDesc):
		self.idList = idList
		self.cardName = cardName
		self.cardDesc = cardDesc
		postTrelloCardQuery = {
			'idList': self.idList,
			'name': self.cardName,
			'desc': self.cardDesc,
			'key': s.TRELLO_KEY,
			'token': s.TRELLO_TOKEN
		}

		return requests.request('POST', s.TRELLO_URL_POST_CARD, params=postTrelloCardQuery)

	def updateCard(self, idCard, newCardName, newCardDesc):
		self.idCard = idCard
		self.newCardName = newCardName
		self.newCardDesc = newCardDesc
		putTrelloCardQuery = {
			'name': self.newCardName,
			'desc': self.newCardDesc,
			'key': s.TRELLO_KEY,
			'token': s.TRELLO_TOKEN
		}

		return requests.request('PUT', s.TRELLO_URL_FOR_CARD.format(id=self.idCard), params=putTrelloCardQuery)

	def removeCard(self, idCard):
		self.idCard = idCard

		return requests.request('DELETE', s.TRELLO_URL_FOR_CARD.format(id=self.idCard), params={'key': s.TRELLO_KEY,'token': s.TRELLO_TOKEN})

class Yt(Taskedit):

	def watchBoards(self):
		ytBoards = {
			'fields': 'id,name'
		}
		dt = []

		response = requests.request('GET', s.YT_URL_GLOBAL, params=ytBoards, headers=s.YT_HEADERS)

		for ytBoard in response.json():
			idBoard = ytBoard.get('id')
			nameBoard = ytBoard.get('name')
			dt.append({'id': idBoard, 'name': nameBoard})

		return {'Boards': dt}

	def watchLists(self, idBoard):
		self.idBoard = idBoard
		ytQ = {
			'fields': 'id,name,values(id,name)'
		}
		dt = []

		response = requests.request('GET', s.YT_URL_LISTS.format(id=self.idBoard), params=ytQ, headers=s.YT_HEADERS)

		for value in response.json().get('values'):
			idList = value.get('id')
			nameList = value.get('name')
			dt.append({'id': idList, 'name': nameList})

		return {'Lists': dt}

	def watchCards(self, idList):
		self.idList = idList
		ytQ = {
			'fields': 'id,summary,fields(id,name,value(id,name))'
		}
		dt = []

		response = requests.request('GET', s.YT_URL_CARDS.format(id=self.idList), params=ytQ, headers=s.YT_HEADERS)

		for card in response.json():
			idCard = card.get('id')
			nameCard = card.get('summary')

			for field in card.get('fields'):
				if field.get('value') != None:
					if field.get('value').get('id') == self.idList:
						dt.append({'id': idCard, 'name': nameCard})

		return {'Cards': dt}

	def createCard(self, idList, cardName, cardDesc):
		self.idList = idList
		self.cardName = cardName
		self.cardDesc = cardDesc
		ytCreateCardFields = {
			'fields': 'idReadable'
		}

		ytCr = {
			'summary': self.cardName,
			'description': self.cardDesc,
			'project': {
				'id': '0-3'
			},
			'customFields': [
				{
					'value': {
						'id': self.idList,
						'$type': 'StateBundleElement'
					},
					'name': 'Stage',
					'$type': 'StateIssueCustomField'
				}
			]
		}

		return requests.request('POST', s.YT_URL_CARDS, params=ytCreateCardFields, headers=s.YT_HEADERS, json=ytCr)			

	def updateCard(self, idCard, newCardName, newCardDesc):
		self.idCard = idCard
		self.newCardName = newCardName
		self.newCardDesc = newCardDesc
		ytJson = {
			'summary': self.newCardName,
			'description': self.newCardDesc
		}

		return requests.request('POST', s.YT_URL_CARD_EDIT.format(id=self.idCard), headers=s.YT_HEADERS, json=ytJson)

	def removeCard(self, idCard):
		self.idCard = idCard

		return requests.request('DELETE', s.YT_URL_CARD_EDIT.format(id=self.idCard), headers=s.YT_HEADERS)