import pytest
from unittest.mock import patch
from domain.entities.User import User
from use_case.get_token_use_case import get_token_use_case
from utils.random_helpers import generate_random_string, generate_strong_password

@pytest.fixture
def mock_user():
    """
    A pytest fixture providing a random User instance.

    The fixture returns a User instance with a random email and strong password.
    """
    return User(
        email=f"{generate_random_string()}@email.com",
        password=generate_strong_password()
    )

def test_get_token_use_case(mock_user):
    """
    Test get_token_use_case function.

    The test verifies that the get_token_use_case function returns a string token
    when given a valid base_url and User instance. The test uses a mock of the
    get_token function to intercept and verify the call.

    Args:
        mock_user (User): A pytest fixture providing a random User instance.

    Asserts:
        The returned token is an instance of str.
        The returned token matches the expected dummy_token.
    """
    base_url = "http://api.example.com"
    dummy_token = "dummy_token"

    with patch("use_case.get_token_use_case.get_token") as mock_get_token:
        mock_get_token.return_value = dummy_token

        result = get_token_use_case(base_url, mock_user)

        assert isinstance(result, str)
        assert result == dummy_token
