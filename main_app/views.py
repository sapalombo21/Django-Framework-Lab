from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

class Game():
    def __init__(self, name, summary, price, series):
        self.name = name
        self.summary = summary
        self.price = price
        self.series = series

games = [
    Game('Minecraft','Mine and craft to survive in this cube world',30.00,'Minecraft'),
    Game('Minecraft: Bedrock edition', 'Mine and craft on console (now made in C#)',30.00, 'Minecraft'),
    Game('Halo Infinite','Master Chief is finally on a halo ring', 60.00, 'Halo'),
    Game('Guilty Gear -Strive-', 'Brand new entry in the series, a whole new generation of Guilty Gear', 60.00, 'Guilty Gear'),
    Game('Rust','Mine mats, build a base, and raid enemy bases',30.00,None)
]

def home(request):
    return HttpResponse('<h1>Welcome to my games list</h1>')

def about(request):
    return render(request, 'about.html')

def games_index(request):
    return render(request, 'games/index.html', {'games':games})