from datetime import datetime

from django.test import SimpleTestCase
from freezegun import freeze_time

from api_server.auth._registration_tokens import RegistrationTokenStorage


@freeze_time("2025-01-04 12:00:00")
class Test__RegistryTokenStorage__use_token(SimpleTestCase):
    def setUp(self):
        self.token_storage: RegistrationTokenStorage = RegistrationTokenStorage()
        self.token_storage.tokens.clear()

    def test_when_token_valid_and_not_expired_then_return_True_True(self):
        self.token_storage.tokens.append(("valid_not_expired_token", datetime(2025, 1, 6)))

        status: tuple[bool, bool] = self.token_storage.use_token("valid_not_expired_token")

        self.assertEqual(status, (True, True))

    def test_when_token_valid_and_not_expired_then_remove_it_from_storage(self):
        self.token_storage.tokens.append(("valid_not_expired_token", datetime(2025, 1, 6)))

        self.token_storage.use_token("valid_not_expired_token")

        self.assertNotIn(("valid_not_expired_token", datetime(2025, 1, 6)), self.token_storage.tokens)

    def test_when_token_valid_and_expired_then_return_True_False(self):
        self.token_storage.tokens.append(("valid_expired_token", datetime(2025, 1, 3)))

        status: tuple[bool, bool] = self.token_storage.use_token("valid_expired_token")

        self.assertEqual(status, (True, False))

    def test_when_token_valid_and_expired_then_not_remove_it_from_storage(self):
        self.token_storage.tokens.append(("valid_expired_token", datetime(2025, 1, 3)))

        self.token_storage.use_token("valid_expired_token")

        self.assertIn(("valid_expired_token", datetime(2025, 1, 3)), self.token_storage.tokens)

    def test_when_token_invalid_then_return_False_True(self):
        self.token_storage.tokens.append(("token", datetime(2025, 1, 3)))

        status: tuple[bool, bool] = self.token_storage.use_token("invalid-token")

        self.assertEqual(status, (False, True))

    def test_when_token_invalid_then_not_remove_anything_from_storage(self):
        self.token_storage.tokens.append(("expired_token", datetime(2025, 1, 3)))
        self.token_storage.tokens.append(("not_expired_token", datetime(2025, 1, 8)))

        self.token_storage.use_token("invalid_token")

        self.assertEqual(
            [("expired_token", datetime(2025, 1, 3)), ("not_expired_token", datetime(2025, 1, 8))], 
            self.token_storage.tokens
        )


@freeze_time("2025-01-04 12:00:00")
class Test__RegistryTokenStorage__delete_expired_tokens(SimpleTestCase):
    def setUp(self):
        self.token_storage: RegistrationTokenStorage = RegistrationTokenStorage()
        self.token_storage.tokens.clear()

    def test_when_one_token_before_expiration_date_and_one_token_after_then_remove_this_after_expiration_date(self):
        self.token_storage.tokens.append(("not_expired_token", datetime(2025, 1, 6)))
        self.token_storage.tokens.append(("expired_token", datetime(2025, 1, 3)))

        self.token_storage.delete_expired_tokens()

        self.assertEqual([("not_expired_token", datetime(2025, 1, 6))], self.token_storage.tokens)

    def test_when_one_token_before_expiration_date_and_one_token_after_then_return_1(self):
        self.token_storage.tokens.append(("not_expired_token", datetime(2025, 1, 6)))
        self.token_storage.tokens.append(("expired_token", datetime(2025, 1, 3)))

        number_of_expired_tokens: int = self.token_storage.delete_expired_tokens()

        self.assertEqual(number_of_expired_tokens, 1)


@freeze_time("2025-01-01 12:00:00")
class Test__RegistryTokenStorage__add_token(SimpleTestCase):
    def setUp(self):
        self.token_storage: RegistrationTokenStorage = RegistrationTokenStorage()
        self.token_storage.tokens.clear()

    def test_when_token_is_not_str_then_raise_ValueError(self):
        token: int = 1
        with self.assertRaises(ValueError):
            self.token_storage.add_token(token)

    def test_when_storage_is_empty_then_add_token_with_its_expiration_date(self):
        token: str = "token"
        expected_expiration_date: datetime = datetime(2025, 1, 4, 12, 0, 0)
        
        self.token_storage.add_token(token)
        
        self.assertEqual([(token, expected_expiration_date)], self.token_storage.tokens)

    def test_when_storage_is_empty_then_return_True(self):
        token: str = "token"
        
        uniq: bool = self.token_storage.add_token(token)
        
        self.assertTrue(uniq)

    def test_when_storage_is_not_empty_and_new_uniq_token_added_then_add_token_with_its_expiration_date(self):
        self.token_storage.add_token("token_1")
        expected_expiration_date: datetime = datetime(2025, 1, 4, 12, 0, 0)
        token: str = "token_2"

        self.token_storage.add_token(token)
        
        self.assertIn((token, expected_expiration_date), self.token_storage.tokens)

    def test_when_storage_is_not_empty_and_new_uniq_token_added_then_return_True(self):
        self.token_storage.add_token("token_1")
        token: str = "token_2"

        uniq: bool = self.token_storage.add_token(token)
        
        self.assertTrue(uniq)

    def test_when_storage_is_not_empty_and_the_same_token_added_then_not_add_token_with_its_expiration_date(self):
        self.token_storage.add_token("token_1")
        token: str = "token_1"

        self.token_storage.add_token(token)
        
        self.assertEqual(
            [("token_1", datetime(2025, 1, 4, 12, 0, 0))], 
            self.token_storage.tokens
        )

    def test_when_storage_is_not_empty_and_the_same_token_added_then_return_False(self):
        self.token_storage.add_token("token_1")
        token: str = "token_1"

        uniq: bool = self.token_storage.add_token(token)
        
        self.assertFalse(uniq)