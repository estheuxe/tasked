from django.urls import path

from . import views

urlpatterns = [
	#path('yandex/', views.gettoken, name='gettoken'),
	path('', views.index, name='index'),
	path('create/', views.create),
	path('delete/', views.delete)
]