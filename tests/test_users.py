from unittest import TestCase
from models.users import Users


class TestUserMethods(TestCase):
    def setUp(self) -> None:
        self.user_test = Users.create('mamedes01','mamedes','1234')

    def test_user_authenticate(self):
        input_password = '1234'
        print(self.user_test)
        self.assertTrue(self.user_test.auth(input_password))

    def test_user_is_not_authenticate(self):
        input_incorrect_password = '12345'
        self.assertFalse(self.user_test.auth(input_incorrect_password))

    def test_user_created(self):
        print(self.user_test)
        print(f'hash: {self.user_test.password_hash}')
        self.assertIsInstance(self.user_test, Users)


