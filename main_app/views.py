from dataclasses import field
from django.shortcuts import render
from .forms import ReviewForm

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Game

def home(request):
    return HttpResponseRedirect('/games')

def about(request):
    return render(request, 'about.html')

def games_index(request):
    games = Game.objects.all()
    return render(request, 'games/index.html', {'games':games})

def games_detail(request, game_id):
    game = Game.objects.get(id=game_id)
    review_form = ReviewForm()
    return render(request, 'games/detail.html', {'game': game, 'review_form': review_form})

class GameCreate(CreateView):
    model = Game
    fields = '__all__'
    success_url = '/games/'

class GameUpdate(UpdateView):
    model = Game
    fields = ['summary','price','series']

class GameDelete(DeleteView):
    model = Game
    success_url = '/games/'