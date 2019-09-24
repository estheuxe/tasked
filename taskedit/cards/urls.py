from django.urls import path

from . import views

urlpatterns = [
	path('card', views.CardView.as_view()),
]