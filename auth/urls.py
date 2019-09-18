from django.urls import path

from . import views

urlpatterns = [
	path('yandex/', views.gettoken, name='gettoken'),
	path('', views.index, name='index')
]