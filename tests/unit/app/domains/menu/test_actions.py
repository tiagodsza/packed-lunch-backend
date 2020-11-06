from unittest import TestCase
from unittest.mock import Mock, patch, call

import pytest

from app.domains.menu.actions import update_menu
from app.domains.menu.model import Menu
from app.exception.models import NotFoundException


class TestMenuActions(TestCase):

    @patch('app.domains.menu.actions.next')
    @patch('app.domains.menu.actions.MenuResponse')
    @patch('app.domains.menu.actions.get_repository')
    def test_update_menu_must_return_the_response(
            self,
            get_repository_mock,
            menu_response_mock,
            next_mock
    ):
        # Arrange
        create_menu_request_mock = Mock()
        menu_mock = Mock()
        repository_mock = Mock()
        repository_mock.get_by_id = Mock(return_value=menu_mock)
        menu_response_mock.from_domain.return_value = 'response'
        next_mock.return_value = repository_mock

        # Action
        response = update_menu(
            id=5,
            create_menu_request=create_menu_request_mock,
        )

        # Assertions
        self.assertEqual(response, 'response')
        get_repository_mock_calls = get_repository_mock.mock_calls
        self.assertEqual(len(get_repository_mock_calls), 1)
        get_repository_mock.assert_has_calls(
            [
                call()
            ]
        )
        repository_mock_calls = repository_mock.mock_calls
        self.assertEqual(len(repository_mock_calls), 2)
        repository_mock.assert_has_calls([
            call.get_by_id(Menu, 5),
            call.save(menu_mock),
        ])
        create_menu_request_mock_calls = create_menu_request_mock.mock_calls
        self.assertEqual(len(create_menu_request_mock_calls), 0)
        menu_mock_calls = menu_mock.mock_calls
        self.assertEqual(len(menu_mock_calls), 1)
        menu_mock.assert_has_calls([
            call.update(create_menu_request_mock)
        ])
        # next_mock_calls = next_mock.mock_calls
        # self.assertEqual(len(next_mock_calls), 3)
        # next_mock.assert_has_calls([
        #     call.batata
        # ])
        menu_response_mock_calls = menu_response_mock.mock_calls
        self.assertEqual(len(menu_response_mock_calls), 1)
        menu_response_mock.assert_has_calls([
            call.from_domain(menu_mock)
        ])


    @patch('app.domains.menu.actions.next')
    def test_update_menu_must_raise_not_found_exception_when_the_get_by_id_dont_returns_a_menu(
            self,
            next_mock,
    ):
        #Arrange
        repository_mock = Mock()
        repository_mock.get_by_id.return_value = None
        next_mock.return_value = repository_mock


        #Action
        with pytest.raises(NotFoundException) as ex:
            update_menu(5, 'create_menu_request')

        #Asserts
        self.assertEqual(ex.value.detail, 'Menu not found!')