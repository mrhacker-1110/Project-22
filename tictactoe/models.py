from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class GameResult(models.Model):
    player_x = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='games_x')
    player_o = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='games_o')
    winner = models.CharField(max_length=1, choices=[('X','X'),('O','O'),('D','Draw')])
    date = models.DateTimeField(auto_now_add=True)
