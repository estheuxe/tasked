# tasked

python3 manage.py migrate

python3 manage.py runserver 1337




uriBoards = 'http://127.0.0.1:1337/boards/board'

uriLists = 'http://127.0.0.1:1337/lists/list'

uriCards = 'http://127.0.0.1:1337/cards/card'

GET:

	requests.request('GET', uriCards, params={'type': 'yt'})
	requests.request('GET', uriCards, params={'type': 'trello', 'id': '5d81c5e68f079e461725ca0b'}) # id of List

	requests.request('GET', uriLists, params={'type': 'trello', 'id': '5d81c5e6ecf65d36ef777b70'}) # id of Board
	# no lists for YouTrack, there is only Boards(Projects) and Cards(Issues)

	requests.request('GET', uriBoards, params={'type': 'trello'})
	requests.request('GET', uriBoards, params={'type': 'yt'})

POST(Cards only):
	
	qs = {
		'type': 'trello|yt',
		'id': 'id of List(only for trello)'
		'name': 'name text',
		'desc': 'desc text'
	}
	
	requests.request('POST', uriCards, params=qs)

PUT(Cards only):

	qs = {
		'type': 'trello|yt',
		'id': 'id of Card',
		'name': 'new name text',
		'desc': 'new desc text'
	}
	
	requests.request('PUT', uriCards, params=qs)
	
DELETE(Cards only):

	qs = {
		'type': 'trello|yt',
		'id': 'id of Card'
	}

	requests.request('DELETE', uriCards, params=qs)

Superuser:
	name: estheuxe
	pw: asdf5
