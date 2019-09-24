from django.contrib import admin
from django.urls import path, include

urlpatterns = [
	path('boards/', include('taskedit.boards.urls')),
	path('lists/', include('taskedit.lists.urls')),
	path('cards/', include('taskedit.cards.urls')),
	path('admin/', admin.site.urls)
]
