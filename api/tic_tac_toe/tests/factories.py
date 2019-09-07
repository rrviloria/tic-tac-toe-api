import factory
import factory.fuzzy
from api.tic_tac_toe import models


class PlayerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Player

    name = factory.Faker('name')


class GameFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.Game

    player_x = factory.SubFactory(PlayerFactory)
    player_o = factory.SubFactory(PlayerFactory)
    winner = factory.SubFactory(PlayerFactory)
    highest_score = factory.fuzzy.FuzzyInteger(30)


class GameRoundFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = models.GameRound

    board = [['o', ' ', 'x'],
             [' ', 'x', ' '],
             ['x', ' ', 'o'], ]
    game = factory.SubFactory(GameFactory)
    winner = factory.SubFactory(PlayerFactory)
