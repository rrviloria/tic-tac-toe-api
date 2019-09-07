"""API view sets for rest-api

    Reference: https://www.django-rest-framework.org/tutorial/quickstart/#views
"""
from rest_framework import viewsets
from rest_framework import filters

from django_filters.rest_framework import DjangoFilterBackend
from api.tic_tac_toe.models import Player, Game, GameRound
from api.tic_tac_toe.serializers import \
    PlayerSerializer, GameSerializer, GameRoundSerializer


class PlayerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows products to be viewed or edited.
    """
    queryset = Player.objects
    serializer_class = PlayerSerializer


class GameViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows products to be viewed or edited.
    """
    queryset = (
        Game.objects
        # optimization: avoid n + 1 query problem
        .select_related(
            'player_x',
            'player_o',
            'winner',
        )
    )
    serializer_class = GameSerializer

    filter_backends = (
        filters.OrderingFilter,
        DjangoFilterBackend,
    )
    ordering_fields = ('highest_score',)
    filterset_fields = {
        'highest_score': ['isnull'],
        'winner': ['isnull'],
    }


class GameRoundViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows products to be viewed or edited.
    """
    queryset = (
        GameRound.objects
        # optimization: avoid n + 1 query problem
        .select_related(
            'game',
            'winner'
        )
    )
    serializer_class = GameRoundSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ('game__id',)
