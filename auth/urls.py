from django.urls import path

from . import views

urlpatterns = [
	#path('yandex/', views.gettoken, name='gettoken'),
	path('', views.index, name='index'),
	path('create/', views.create),
	path('delete/', views.delete),
	path('cards', views.CardView.as_view()),
	path('lists', views.ListView.as_view()),
	path('boards', views.BoardView.as_view()),
]

#boards?type=trello|yandex