from unittest import TestCase
from unittest.mock import Mock

from app.database.model import AbstractModelMixin
from app.domains.menu.model import Menu


class TestMenu(TestCase):
    def test_if_menu_class_is_istantiated(self):
        # Arrange

        # Action
        menu = Menu(
            number=1,
            food='Batatinha frita',
            categorie='Low Carb',
            restaurant='Restaurant Brasa'
        )

        # Asserts
        self.assertIsInstance(menu, AbstractModelMixin)
        self.assertEqual(menu.number, 1)
        self.assertEqual(menu.food, 'Batatinha frita')
        self.assertEqual(menu.categorie, 'Low Carb')
        self.assertEqual(menu.restaurant, 'Restaurant Brasa')

    def test_update(self):
        # Aranges
        menu = Menu(
            number=1,
            food='Batatinha frita',
            categorie='Low Carb',
            restaurant='Restaurant Brasa'
        )
        create_menu_request_mock = Mock()
        create_menu_request_mock.number = 2
        create_menu_request_mock.food = 'Salda de cenoura'
        create_menu_request_mock.categorie = 'Vegano'
        create_menu_request_mock.restaurant = 'Chef Fábricio'

        # Action
        menu.update(create_menu_request_mock)

        # Asserts
        self.assertEqual(menu.number, 2)
        self.assertEqual(menu.food, 'Salda de cenoura')
        self.assertEqual(menu.categorie, 'Vegano')
        self.assertEqual(menu.restaurant, 'Chef Fábricio')
