from unittest import TestCase
from unittest.mock import patch

import pytest

from app.database.model import AbstractModelMixin
from app.exception.models import NotFoundException


class Food(AbstractModelMixin):
    pass

class TestAbstractModel(TestCase):

    def test_abstract_model_mixin_was_inherited_by_the_class(self):
        #Action
        food = Food()

        #Asserts
        self.assertIsInstance(food, AbstractModelMixin)
        self.assertTrue(hasattr(food, 'id'))
        self.assertTrue(hasattr(food, 'created_at'))
        self.assertTrue(hasattr(food, 'updated_at'))
        self.assertTrue(hasattr(food, 'deleted_at'))

    @patch('app.database.model.datetime')
    def test_inactivate(self, datetime_mock):
        #Arrange
        food = Food()
        food.deleted_at = None
        datetime_mock.now.return_value = '2020-11-18'

        #Action
        food.inactivate()

        #Asserts
        print(food.deleted_at)
        self.assertEqual(food.deleted_at, '2020-11-18')

    def test_is_inactive_must_return_true_when_the_deleted_at_has_a_date(self):
        #Arrange
        food = Food()
        food.deleted_at = '2020-11-18'

        #Asserts
        self.assertEqual(food.is_inactive(), True)

    def test_is_inactive_must_return_false_when_the_deleted_at_has_not_a_date(self):
        # Arrange
        food = Food()
        food.deleted_at = None

        # Asserts
        self.assertEqual(food.is_inactive(), False)

    def test_inactivate_must_raise_not_found_exception_when_trying_inactivate_a_object_already_inactivated(self):
        #Arrange
        food = Food()
        food.deleted_at = None
        food.inactivate()

        #Action
        with pytest.raises(NotFoundException) as ex:
            food.inactivate()

        #Asserts
        self.assertEqual(ex.value.status_code, 404)
        self.assertEqual(ex.value.detail, 'Food not found.')