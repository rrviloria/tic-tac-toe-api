from rest_framework.serializers import \
    Serializer, CharField, DecimalField, ModelSerializer

from api.tic_tac_toe.models import Player, Game, GameRound


class PlayerSerializer(ModelSerializer):

    class Meta:
        model = Player
        fields = ('id', 'name')


class GameSerializer(ModelSerializer):

    class Meta:
        model = Game
        fields = (
            'id', 'highest_score',
            'player_x', 'player_x_score',
            'player_o', 'player_o_score',
        )


class GameRoundSerializer(ModelSerializer):

    class Meta:
        model = GameRound
        fields = (
            'id', 'board', 'game', 'winner'
        )
