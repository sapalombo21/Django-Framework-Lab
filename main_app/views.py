from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Game

def home(request):
    return HttpResponse('<h1>Welcome to my games list</h1>')

def about(request):
    return render(request, 'about.html')

def games_index(request):
    games = Game.objects.all()
    return render(request, 'games/index.html', {'games':games})