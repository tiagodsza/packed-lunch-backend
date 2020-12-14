from unittest import TestCase
from unittest.mock import patch, Mock, call

from fastapi.testclient import TestClient

from app import app
from app.routes.menu.menu_request import CreateMenuRequest

client = TestClient(app)


class TestMenuRoutes(TestCase):

    @patch('app.routes.menu.menu_routes.get_repository')
    def test_get_menu(
            self,
            get_repository_mock,
    ):
        # Arrange
        repository_mock = Mock()
        repository_mock.get.return_value = 'response'
        get_repository_mock.side_effect = [repository_mock]

        # Action
        response = client.get('/menu/')

        # Asserts
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), 'response')
        get_repository_mock_calls = get_repository_mock.mock_calls
        self.assertEqual(len(get_repository_mock_calls), 1)
        get_repository_mock.assert_has_calls([
            call()
        ])

    @patch('app.routes.menu.menu_routes.get_menu_by_id')
    def test_get_by_id(self, get_menu_by_id_mock):
        # Arrange
        get_menu_by_id_mock.return_value = 'response'

        # Action
        response = client.get('/menu/1')

        # Asserts
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), 'response')
        get_menu_by_id_mock_calls = get_menu_by_id_mock.mock_calls
        self.assertEqual(len(get_menu_by_id_mock_calls), 1)
        get_menu_by_id_mock.assert_has_calls([
            call(1)
        ])

    @patch('app.routes.menu.menu_routes.create_menu')
    def test_post_menu(
            self,
            create_menu_mock
    ):
        # Arrange
        create_menu_mock.return_value = 'response'

        # Action
        response = client.post(
            '/menu/',
            json={
                'number': '1',
                'food': 'T-bone',
                'categorie': 'Meat',
                'restaurant': 'Chef Meat',
            },
        )

        # Asserts
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(), 'response')
        create_menu_mock_calls = create_menu_mock.mock_calls
        self.assertEqual(len(create_menu_mock_calls), 1)
        create_menu_mock.assert_has_calls([
            call(CreateMenuRequest(number=1, food='T-bone', categorie='Meat', restaurant='Chef Meat'))
        ])

    @patch('app.routes.menu.menu_routes.update_menu')
    def test_update_menu(self, update_menu_mock):
        # Arrange
        update_menu_mock.return_value = 'response'

        # Action
        response = client.put(
            '/menu/1',
            json={
                'number': '1',
                'food': 'T-bone',
                'categorie': 'Meat',
                'restaurant': 'Chef Meat',
            },
        )

        # Asserts
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), 'response')
        update_menu_mock_calls = update_menu_mock.mock_calls
        self.assertEqual(len(update_menu_mock_calls), 1)
        update_menu_mock.assert_has_calls([
            call(1, CreateMenuRequest(number=1, food='T-bone', categorie='Meat', restaurant='Chef Meat'))
        ])

    @patch('app.routes.menu.menu_routes.delete_menu')
    def test_delete_menu(self, delete_menu_mock):
        # Arranges
        delete_menu_mock.return_value = 'response'

        # Action
        response = client.delete('/menu/6')

        # Asserts
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), 'response')
        delete_menu_mock_calls = delete_menu_mock.mock_calls
        self.assertEqual(len(delete_menu_mock_calls), 1)
        delete_menu_mock.assert_has_calls([
            call(6)
        ])
