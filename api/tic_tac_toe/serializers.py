from rest_framework.serializers import \
    Serializer, CharField, DecimalField, ModelSerializer, \
    SlugRelatedField

from api.tic_tac_toe.models import Player, Game, GameRound


class PlayerSerializer(ModelSerializer):

    class Meta:
        model = Player
        fields = ('id', 'name')


class GameSerializer(ModelSerializer):
    player_x_name = CharField(read_only=True, source='player_x.name')
    player_o_name = CharField(read_only=True, source='player_o.name')
    winner_name = CharField(read_only=True, source='winner.name')

    class Meta:
        model = Game
        fields = (
            'id', 'highest_score',
            'player_x', 'player_x_score',
            'player_o', 'player_o_score',
            'player_x_name', 'player_o_name',
            'winner', 'winner_name'
        )


class GameRoundSerializer(ModelSerializer):

    class Meta:
        model = GameRound
        fields = (
            'id', 'board', 'game', 'winner'
        )
