from django.test import TestCase, Client

from api.tic_tac_toe.models import Player
from .factories import PlayerFactory


class PlayerAPITest(TestCase):
    """
    Test case for Player APIs
    """

    def setUp(self):
        self.client = Client()

    def test_get_players_api(self):
        players = PlayerFactory.create_batch(10)
        response = self.client.get('/players/')

        # Test if request returns sucessfully
        self.assertEquals(response.status_code, 200)
        # Test if players count is equal to DB record count
        self.assertEquals(len(response.data), len(players))

    def test_get_player_by_id_api(self):
        player = PlayerFactory.create(name='Raymund')
        response = self.client.get('/players/%s/' % player.id)

        # Test if request returns sucessfully
        self.assertEquals(response.status_code, 200)
        # Test if name is `Raymund`
        self.assertEquals(response.data['name'], 'Raymund')

    def test_fail_get_player_by_id_api(self):
        # `1` does not exist on database
        response = self.client.get('/players/%s/' % 1)
        # Test if request returns 404
        self.assertEquals(response.status_code, 404)

    def test_create_player_api(self):
        response = self.client.post(
            '/players/', {'name': 'Raymund'}
        )

        # Test if request returns sucessfully
        self.assertTrue(response.status_code < 300)

        data = response.data
        player = Player.objects.get(pk=data['id'])
        # Test if name is `Raymund`
        self.assertEquals(data['name'], player.name)

    def test_update_player_api(self):
        response = self.client.post(
            '/players/', {'name': 'Raymund'},
            content_type='application/json'
        )

        # Test if request returns sucessfully
        self.assertTrue(response.status_code < 300)

        data = response.data
        player = Player.objects.get(pk=data['id'])
        # Test if name is `Raymund`
        self.assertEquals(data['name'], player.name)

        response = self.client.patch(
            '/players/%s/' % data['id'], {'name': 'Viloria'},
            content_type='application/json'
        )

        # Test if request returns sucessfully
        self.assertTrue(response.status_code < 300)
        data = response.data
        player = Player.objects.get(pk=data['id'])
        # Test if name is `Viloria`
        self.assertEquals(data['name'], player.name)
