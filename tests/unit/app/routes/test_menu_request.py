from unittest import TestCase
from unittest.mock import patch, call

from pydantic.main import BaseModel

from app.routes.menu.menu_request import CreateMenuRequest


class TestCreateMenuRequest(TestCase):

    @patch('app.routes.menu.menu_request.Menu')
    def test_if_to_domain_returns_the_menu(self, menu_mock):
        # Arrange
        create_menu_request = CreateMenuRequest(
            number=2,
            food='T-bone',
            categorie='Meat',
            restaurant='Chef Meat',
        )
        menu_mock.return_value = 'menu'

        # Action
        menu = create_menu_request.to_domain()

        # Asserts
        self.assertIsInstance(create_menu_request, BaseModel)
        self.assertEqual(menu, 'menu')
        menu_mock_calls = menu_mock.mock_calls
        self.assertEqual(len(menu_mock_calls), 1)
        menu_mock.assert_has_calls([
            call(
                number=2,
                food='T-bone',
                categorie='Meat',
                restaurant='Chef Meat',
            )
        ])
