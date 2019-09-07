from django.db import models
from django.contrib.postgres.fields import ArrayField


class Player(models.Model):
    name = models.CharField(
        max_length=150,
        help_text='Player name',
    )

    def __str__(self):
        return self.name


class Game(models.Model):
    # On this case we can assume there can only be 2 players
    # We can do Many to Many relationship for multiple players
    # but that's unnecessary at this point
    player_x = models.ForeignKey(
        Player,
        null=False,
        default=None,
        related_name='game_player_x',
        on_delete=models.CASCADE,
        help_text='A player representing X',
    )
    player_o = models.ForeignKey(
        Player,
        null=False,
        default=None,
        related_name='game_player_o',
        on_delete=models.CASCADE,
        help_text='A player representing O',
    )
    winner = models.ForeignKey(
        Player,
        null=True,
        default=None,
        related_name='game_winner',
        on_delete=models.CASCADE,
        help_text='Winner of the game',
    )

    # player's score varies per game
    player_x_score = models.IntegerField(default=0)
    player_o_score = models.IntegerField(default=0)
    highest_score = models.IntegerField(null=True, default=None)

    created_at = models.DateTimeField(auto_now_add=True)


class GameRound(models.Model):
    # A model for game history per round
    # 3 x 3 tic tac toe board. Sample
    # ['o', ' ', 'x']
    # [' ', 'x', ' ']
    # ['x', ' ', 'o']
    board = ArrayField(
        ArrayField(
            models.CharField(max_length=1, blank=True),
            size=6
        ),
        size=6
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
        help_text='Winner of the round',
    )
