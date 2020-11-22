from unittest import TestCase
from unittest.mock import patch, Mock, call

from app.routes.menu.menu_response import MenuResponse


class TestMenuResponse(TestCase):
    @patch('app.routes.menu.menu_response.MenuResponse')
    def test_from_domain(self, menu_response_mock):
        #Arrange
        menu_response_mock.return_value= 'menu_response'
        data_mock = Mock()
        data_mock.id = 1,
        data_mock.created_at='2020-11-22',
        data_mock.updated_at='2020-11-22',
        data_mock.deleted_at='2020-11-22',
        data_mock.number=2,
        data_mock.food='T-bone',
        data_mock.categorie='Meat',
        data_mock.restaurant='Chef Meat',

        #Action
        response = MenuResponse.from_domain(data_mock)

        #Asserts
        self.assertEqual(response, 'menu_response')
        menu_response_mock_calls = menu_response_mock.mock_calls
        self.assertEqual(len(menu_response_mock_calls), 1)
        menu_response_mock.assert_has_calls([
            call(
                id=(1,),
                created_at=('2020-11-22',),
                updated_at=('2020-11-22',),
                deleted_at=('2020-11-22',),
                number=(2,),
                food=('T-bone',),
                categorie=('Meat',),
                restaurant=('Chef Meat',),
            )
        ])
