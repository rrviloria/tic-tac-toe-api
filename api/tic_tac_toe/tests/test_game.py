from django.test import TestCase, Client

from api.tic_tac_toe.models import Game
from .factories import GameFactory, PlayerFactory


class GameAPITest(TestCase):
    """
    Test case for Game APIs
    """

    def setUp(self):
        self.client = Client()

    def test_get_games_api(self):
        games = GameFactory.create_batch(10)
        response = self.client.get('/games/')

        # Test if request returns sucessfully
        self.assertEquals(response.status_code, 200)
        # Test if games count is equal to DB record count
        self.assertEquals(len(response.data), len(games))

    def test_get_games_api_highest_score(self):
        games = GameFactory.create_batch(20)
        max_score = max([game.highest_score for game in games])
        top_scores = 5  # get top 5 game scores
        response = self.client.get(
            '/games/', {
                'ordering': '-highest_score',
                'limit': top_scores
            })

        # Test if request returns sucessfully
        self.assertEquals(response.status_code, 200)
        # Test if it's only showing 5 games
        self.assertEquals(
            len(response.data['results']), top_scores)
        # Test if highest score is same as computed max_score
        self.assertEquals(
            response.data['results'][0]['highest_score'],
            max_score)

    def test_get_game_by_id_api(self):
        game = GameFactory.create()
        response = self.client.get('/games/%s/' % game.id)

        # Test if request returns sucessfully
        self.assertEquals(response.status_code, 200)
        # Test if data is the same on DB
        self.assertEquals(response.data['id'], game.id)

    def test_fail_get_game_by_id_api(self):
        # `1` does not exist on database
        response = self.client.get('/games/%s/' % 1)
        # Test if request returns 404
        self.assertEquals(response.status_code, 404)

    def test_create_game_api(self):
        player1 = PlayerFactory.create(name='Raymund')
        player2 = PlayerFactory.create(name='Viloria')
        response = self.client.post(
            '/games/', {
                'player_x': str(player1.id),
                'player_o': str(player2.id),
            },
            content_type='application/json'
        )
        # Test if request returns sucessfully
        self.assertTrue(response.status_code < 300)
        data = response.data
        game = Game.objects.get(pk=data['id'])
        # Test if player_x is player1
        self.assertEquals(data['player_x'], player1.id)
        # Test if player_o is player2
        self.assertEquals(data['player_o'], player2.id)

    def test_update_game_api(self):
        player1 = PlayerFactory.create(name='Raymund')
        player2 = PlayerFactory.create(name='Viloria')
        response = self.client.post(
            '/games/', {
                'player_x': str(player1.id),
                'player_o': str(player2.id),
            },
            content_type='application/json'
        )
        # Test if request returns sucessfully
        self.assertTrue(response.status_code < 300)
        data = response.data
        game = Game.objects.get(pk=data['id'])
        # Test if player_x is player1
        self.assertEquals(data['player_x'], player1.id)
        # Test if player_o is player2
        self.assertEquals(data['player_o'], player2.id)

        updated_data = {
            'player_x_score': 5,
            'player_o_score': 10,
            'winner': player2.id
        }
        response = self.client.patch(
            '/games/%s/' % game.id, updated_data,
            content_type='application/json'
        )
        # Test if request returns sucessfully
        self.assertTrue(response.status_code < 300)

        data = response.data
        game = Game.objects.get(pk=data['id'])
        # Test if data is updated on DB
        self.assertEquals(
            data['player_x_score'], game.player_x_score)
        self.assertEquals(
            data['player_o_score'], game.player_o_score)
        self.assertEquals(data['winner'], game.winner.id)
