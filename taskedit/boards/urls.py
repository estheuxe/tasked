from django.urls import path

from . import views

urlpatterns = [
	path('board', views.BoardView.as_view()),
]