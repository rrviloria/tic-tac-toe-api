from django.db import models
from django.contrib.postgres.fields import ArrayField


class Player(models.Model):
    name = models.CharField(
        max_length=150,
        help_text='Player name',
    )


class Game(models.Model):
    # On this case we can assume there can only be 2 players
    # We can do Many to Many relationship for multiple players
    # but that's unnecessary at this point
    player_x = models.ForeignKey(
        Player,
        null=True,
        related_name='game_player_x',
        on_delete=models.CASCADE,
        help_text='A player representing X',
    )
    player_x_score = models.IntegerField(default=0)

    player_o = models.ForeignKey(
        Player,
        null=True,
        related_name='game_player_o',
        on_delete=models.CASCADE,
        help_text='A player representing O',
    )
    player_o_score = models.IntegerField(default=0)
    highest_score = models.IntegerField(default=None)

    created_at = models.DateTimeField(auto_now_add=True)


class GameRound(models.Model):
    # 3 x 3 tic tac toe board. Sample
    # [' ', ' ', 'X']
    # [' ', 'X', ' ']
    # ['X', ' ', ' ']
    board = ArrayField(
        ArrayField(
            models.CharField(max_length=1, blank=True),
            size=3
        ),
        size=3
    )

    game = models.ForeignKey(
        Game,
        null=True,
        on_delete=models.CASCADE,
        help_text='Current game',
    )

    winner = models.ForeignKey(
        Player,
        null=True,
        on_delete=models.CASCADE,
        help_text='A player representing O',
    )
