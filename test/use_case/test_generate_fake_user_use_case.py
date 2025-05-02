import re
import pytest
from unittest.mock import patch
from interface.controller.DTOs.UserDTO import UserDTO
from use_case.generate_fake_user import GenerateFakeUserUseCase

def test_generate_fake_user_use_case_returns_valid_user_dto():
    """
    Tests that the GenerateFakeUserUseCase.execute() method returns a valid UserDTO.
    
    The test verifies that the returned UserDTO is an instance of UserDTO, has an email
    that matches the expected pattern, and has a password that is not None and has a
    length of at least 8 characters.
    """
    user_dto = GenerateFakeUserUseCase.execute()

    assert isinstance(user_dto, UserDTO)
    assert re.match(r"^[a-z]+\.[a-z]+@email\.com$", user_dto.email)
    assert user_dto.password is not None
    assert len(user_dto.password) >= 8
    assert any(char.islower() for char in user_dto.password)
    assert any(char.isupper() for char in user_dto.password)
    assert any(char.isdigit() for char in user_dto.password)
    assert any(char in "!@#$%&*" for char in user_dto.password)

@pytest.fixture
def mocked_random_string_and_password():
    """
    Pytest fixture to mock generate_random_string and generate_strong_password

    The fixture will return two mocked functions: mock_random_string and mock_password.

    mock_random_string will return "John" and "Doe" when called, and
    mock_password will return "SenhaF0rte!"

    This fixture is useful for testing the GenerateFakeUserUseCase
    with fixed values for the generated user's email and password.
    """
    with patch("use_case.generate_fake_user.generate_random_string") as mock_random_string, \
        patch("use_case.generate_fake_user.generate_strong_password") as mock_password:
        mock_random_string.side_effect = ["John", "Doe"]
        mock_password.return_value = "SenhaF0rte!"
        yield mock_random_string, mock_password

def test_generate_fake_user_use_case_with_mocks(mocked_random_string_and_password):
    """
    Test GenerateFakeUserUseCase.execute() with mocked random string and password.

    This test uses mocked values for the random string and password generation 
    to ensure that the GenerateFakeUserUseCase.execute() method returns a UserDTO 
    with the expected email and password.

    Args:
        mocked_random_string_and_password: A fixture providing mocked functions 
        for generating random strings and strong passwords.

    Asserts:
        The returned user_dto is an instance of UserDTO.
        The email in the user_dto matches the expected mocked email.
        The password in the user_dto matches the expected mocked password.
    """

    mock_random_string, mock_password = mocked_random_string_and_password

    user_dto = GenerateFakeUserUseCase.execute()

    assert isinstance(user_dto, UserDTO)
    assert user_dto.email == "john.doe@email.com"
    assert user_dto.password == "SenhaF0rte!"
