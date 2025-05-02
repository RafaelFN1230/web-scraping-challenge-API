import random
import pytest
from unittest.mock import patch
from use_case.create_user_use_case import create_user_use_case
from interface.controller.DTOs.UserDTO import UserDTO
from domain.entities.User import User
from utils.random_helpers import generate_strong_password


@patch('use_case.create_user_use_case.create_user')
def test_success(mock_create_user):
    """
    Test successful execution of create_user_use_case.

    This test verifies that the create_user_use_case function correctly creates
    a User instance with the provided UserDTO and base URL. It checks that the
    returned User instance has the expected email and password, and that the
    create_user function is called once with the correct arguments.

    Args:
        mock_create_user: A mock of the create_user function to intercept and
        verify calls.
    """

    base_url = 'https://example.com'
    user_dto = UserDTO(
        email=f"user{random.randint(1000, 9999)}@email.com",
        password=generate_strong_password()
    )
    mock_create_user.return_value = None

    result = create_user_use_case(base_url, user_dto)

    assert isinstance(result, User)
    assert result.email == user_dto.email
    assert result.password == user_dto.password
    mock_create_user.assert_called_once_with(base_url, result)


@patch('use_case.create_user_use_case.create_user')
def test_invalid_base_url(mock_create_user):
    """
    Test that create_user_use_case raises a TypeError when the base_url is None.

    Args:
        mock_create_user: A mock of the create_user function to intercept and
        verify calls.
    """
    
    base_url = None
    user_dto = UserDTO(email='test@example.com', password='password')

    with pytest.raises(TypeError):
        create_user_use_case(base_url, user_dto)


@patch('use_case.create_user_use_case.create_user')
def test_invalid_user_dto(mock_create_user):
    """
    Test that create_user_use_case raises a TypeError when the user_dto is None.

    Args:
        mock_create_user: A mock of the create_user function to intercept and
        verify calls.
    """

    base_url = 'https://example.com'
    user_dto = None

    with pytest.raises(TypeError):
        create_user_use_case(base_url, user_dto)
