from django.shortcuts import render, redirect
from .models import Player, GameResult
from .forms import PlayerForm

def index(request):
    players = Player.objects.all()
    results = GameResult.objects.all().order_by('-date')
    return render(request, 'tictactoe/index.html', {'players': players, 'results': results})

def create_player(request):
    if request.method == 'POST':
        form = PlayerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PlayerForm()
    return render(request, 'tictactoe/create_player.html', {'form': form})

def play_game(request):
    players = Player.objects.all()
    if request.method == 'POST':
        player_x = Player.objects.get(id=request.POST['player_x'])
        player_o = Player.objects.get(id=request.POST['player_o'])
        winner = request.POST['winner']
        GameResult.objects.create(player_x=player_x, player_o=player_o, winner=winner)
        return redirect('index')
    return render(request, 'tictactoe/play_game.html', {'players': players})
