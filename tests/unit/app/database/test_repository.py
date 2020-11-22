from unittest import TestCase
from unittest.mock import Mock, call, patch

from sqlalchemy.orm import sessionmaker

from app.database.repository import Repository, get_repository, create_repository


class TestRepository(TestCase):

    def test_repository_must_be_instantiated(self):
        #Arrange
        repository = Repository()

        # Action
        repository.set_db('b')

        # Asserts
        self.assertIsInstance(repository, Repository)
        self.assertTrue(hasattr(repository, '_db'))

    def test_set_db_must_to_attribute_a_value_to_the_db(self):
        #Arrange
        repository = Repository()
        db_mock = Mock()

        #Action
        repository.set_db(db_mock)

        #Asserts
        self.assertEqual(repository._db, db_mock)

    def test_close__db_must_call_close(self):
        #Arrange
        repository = Repository()
        db_mock = Mock()
        repository.set_db(db_mock)

        #Action
        repository.close()

        #Asserts
        db_mock_calls = db_mock.mock_calls
        self.assertEqual(len(db_mock_calls), 1)
        db_mock.assert_has_calls([
            call.close()
        ])

    def test_get_must_call_query_and_return_resposne_all(self):
        #Arrange
        repository = Repository()
        response_mock = Mock()
        db_mock = Mock()
        db_mock.query = Mock(return_value=response_mock)
        repository.set_db(db_mock)

        #Action
        repository.get('model')

        #Asserts
        db_mock_calls = db_mock.mock_calls
        self.assertEqual(len(db_mock_calls), 1)
        db_mock.assert_has_calls([
            call.query('model')
        ])
        response_mock_calls = response_mock.mock_calls
        self.assertEqual(len(response_mock_calls), 1)
        response_mock.assert_has_calls([
            call.all()
        ])

    def test_get_by_id(self):
        #Arrange
        repository = Repository()
        db_mock = Mock()
        repository.set_db(db_mock)
        respose_mock = Mock()
        db_mock.query().get = Mock(return_value=respose_mock)

        #Action
        response = repository.get_by_id('model', 23)

        #Asserts
        self.assertEqual(response, respose_mock)
        db_mock_calls = db_mock.mock_calls
        self.assertEqual(len(db_mock_calls), 3)
        db_mock.assert_has_calls([
            call.query(),
            call.query('model'),
            call.query().get(23)
        ])
        response_mock_calls = respose_mock.mock_calls
        self.assertEqual(len(response_mock_calls), 0)

    def test_save(self):
        #Arrange
        repository = Repository()
        session_mock = Mock()
        repository.set_db(session_mock)

        #Action
        repository.save('model')

        #Asserts
        session_mock_calls = session_mock.mock_calls
        self.assertEqual(len(session_mock_calls), 2)
        session_mock.assert_has_calls([
            call.add('model'),
            call.commit()
        ])

    @patch('app.database.repository.Session')
    @patch('app.database.repository.Repository')
    def test_create_repository_must_return_a_repository(
            self,
            repository_mock,
            session_mock,
    ):
        #Arrange
        repository_response_mock = Mock()
        repository_mock.side_effect = [repository_response_mock]

        #Action
        repository = create_repository()

        #Asserts
        self.assertEqual(next(repository), repository_response_mock)
        repository_mock_calls = repository_mock.mock_calls
        self.assertEqual(len(repository_mock_calls), 1)
        repository_mock.assert_has_calls([
            call()
        ])
        repository_response_mock_calls = repository_response_mock.mock_calls
        self.assertEqual(len(repository_response_mock_calls), 1)
        session_mock_calls = session_mock.mock_calls
        self.assertEqual(len(session_mock_calls), 1)
        session_mock.assert_has_calls([
            call()
        ])

    @patch('app.database.repository.create_repository')
    @patch('app.database.repository.next')
    def test_get_repository_must_call_next_create_repository(
            self,
            next_mock,
            create_repository_mock,
    ):
        #Arranges
        next_mock.return_value = 'repository'

        #Action
        repository = get_repository()

        #Asserts
        self.assertEqual(repository, 'repository')
        next_mock_calls = next_mock.mock_calls
        self.assertEqual(len(next_mock_calls), 1)
        next_mock.assert_has_calls([
            call(create_repository_mock())
        ])
