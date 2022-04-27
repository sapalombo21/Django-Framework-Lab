from dataclasses import field
from django.shortcuts import redirect, render
from .forms import ReviewForm

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Game, Engine

def home(request):
    return HttpResponseRedirect('/games')

def about(request):
    return render(request, 'about.html')

def games_index(request):
    games = Game.objects.all()
    return render(request, 'games/index.html', {'games':games})

def games_detail(request, game_id):
    game = Game.objects.get(id=game_id)
    engines_game_doesnt_have = Engine.objects.exclude(id__in = game.engine.all().values_list('id'))
    review_form = ReviewForm()
    return render(request, 'games/detail.html', {'game': game, 'review_form': review_form, 'engines': engines_game_doesnt_have})

def add_review(request, game_id):
    form = ReviewForm(request.POST)
    if form.is_valid():
        new_review = form.save(commit=False)
        new_review.game_id = game_id
        new_review.save()
    return redirect('detail', game_id=game_id)

def assoc_engine(request, game_id, engine_id):
    Game.objects.get(id=game_id).engine.add(engine_id)
    return redirect('detail', game_id=game_id)

def engine_remove(request, game_id, engine_id):
    engine = Engine.objects.get(id=engine_id)
    Game.objects.get(id=game_id).engine.remove(engine)
    return redirect('detail', game_id=game_id)

class GameCreate(CreateView):
    model = Game
    fields = ['name', 'summary','price','series']
    success_url = '/games/'

class GameUpdate(UpdateView):
    model = Game
    fields = ['summary','price','series']

class GameDelete(DeleteView):
    model = Game
    success_url = '/games/'

class EngineCreate(CreateView):
    model = Engine
    fields = '__all__'
    success_url = '/games'