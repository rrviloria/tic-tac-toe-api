from django.test import TestCase, Client

from api.tic_tac_toe.models import GameRound
from .factories import GameRoundFactory, GameFactory, PlayerFactory


class GameRoundAPITest(TestCase):
    """
    Test case for Game APIs
    """

    def setUp(self):
        self.client = Client()

    def test_get_game_rounds_api(self):
        games = GameRoundFactory.create_batch(10)
        response = self.client.get('/game-rounds/')

        # Test if request returns sucessfully
        self.assertEquals(response.status_code, 200)
        # Test if game rounds count is equal to DB record count
        self.assertEquals(len(response.data), len(games))

    def test_get_game_round_by_id_api(self):
        game_round = GameRoundFactory.create()
        response = self.client.get('/game-rounds/%s/' % game_round.id)

        # Test if request returns sucessfully
        self.assertEquals(response.status_code, 200)
        # Test if id is same on DB
        self.assertEquals(response.data['id'], game_round.id)

    def test_fail_get_game_round_by_id_api(self):
        # `1` does not exist on database
        response = self.client.get('/game-rounds/%s/' % 1)
        # Test if request returns 404
        self.assertTrue(response.status_code, 404)

    def test_create_game_round_api(self):
        winner = PlayerFactory.create()
        game = GameFactory.create()
        response = self.client.post(
            '/game-rounds/', {
                'winner': str(winner.id),
                'game': str(game.id),
                'board': [[' ', 'x', 'x']]  # this should be 3x3
            },
            content_type='application/json'
        )

        # Test if request returns sucessfully
        self.assertTrue(response.status_code < 300)
        data = response.data
        game_round = GameRound.objects.get(pk=data['id'])
        # Test if winner is winner.id
        self.assertEquals(data['winner'], game_round.winner.id)
        # Test if game is game.id
        self.assertEquals(data['game'], game_round.game.id)
