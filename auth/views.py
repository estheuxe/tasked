from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Card
import webbrowser

appId = '11630581252b45c8b3d7459720ed2af1'
appPw = 'c200a37d97064c03ab55b1a1a5a28402'

url = 'https://oauth.yandex.ru/authorize?response_type=token&client_id=' + appId

def index(request):
	cards = Card.objects.all()
	return render(request, 'index.html', {'cards': cards})
	'''
	Yandex Tracker 
	webbrowser.open(url)
	return HttpResponse("auth page")
	'''
def gettoken(request):
	currUrl = request.get_full_path()
	return HttpResponse(currUrl)

def create(request):
	if request.method == 'POST':
		foo = Card()
		foo.name = request.POST.get('name')
		foo.desc = request.POST.get('desc')
		foo.save()
	return HttpResponseRedirect('/auth/')

def delete(request):
	Card.objects.all().delete()
	return HttpResponseRedirect('/auth/')
