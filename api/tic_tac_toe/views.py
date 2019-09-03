"""API view sets for rest-api

    Reference: https://www.django-rest-framework.org/tutorial/quickstart/#views
"""

# from datetime import timedelta
# from django.utils import timezone
# from django.db.models import Sum

from rest_framework import viewsets
from rest_framework import filters

from django_filters.rest_framework import DjangoFilterBackend
# from rest_framework.decorators import action
# from rest_framework.response import Response

from api.tic_tac_toe.mixins import \
    MultiSerializerViewSetMixin
from api.tic_tac_toe.models import Player, Game, GameRound
from api.tic_tac_toe.serializers import \
    PlayerSerializer, GameSerializer, GameRoundSerializer



class PlayerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows products to be viewed or edited.
    """
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer


class GameViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows products to be viewed or edited.
    """
    queryset = Game.objects.all()
    serializer_class = GameSerializer

    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['highest_score']


class GameRoundViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows products to be viewed or edited.
    """
    queryset = GameRound.objects.all()
    serializer_class = GameRoundSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['game__id']
