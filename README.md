# tasked

python3 manage.py migrate
python3 manage.py runserver 1337

uriBoards = 'http://127.0.0.1:1337/boards/board'
uriLists = 'http://127.0.0.1:1337/lists/list'
uriCards = 'http://127.0.0.1:1337/cards/card'

возможные параметры {
  'type': 'trello',             # пока только трелло
  'id': idList|idCard|idBoard   # в зависимости от запроса
	'name': 'qwertyqwerty',       # если того требует запрос
	'desc': 'dddddddd',           # если того требует запрос
}
