import pytest
from unittest.mock import patch, MagicMock
from interface.controller.main_controller import MainController
from interface.controller.DTOs.UserDTO import UserDTO
from interface.controller.DTOs.BookDTO import BookDTO

@pytest.fixture
def mock_user():
    """
    Fixture providing a mocked UserDTO instance.

    Returns:
        UserDTO: A mocked UserDTO with predefined email and password.
    """

    return UserDTO(email="mockuser", password="mockpass")

@pytest.fixture
def mock_books():
    """
    Fixture providing a list of two BookDTO instances.

    Returns:
        list[BookDTO]: A list of two BookDTO instances with predefined title, author and publisher.
    """
    return [
        BookDTO(image="-", title="Livro 1", author="Autor A", publisher="Editora X"),
        BookDTO(image="-", title="Livro 2", author="Autor B", publisher="Editora Y"),
    ]

@patch("interface.controller.main_controller.generate_books_csv_use_case")
@patch("interface.controller.main_controller.get_books_use_case")
@patch("interface.controller.main_controller.get_token_use_case")
@patch("interface.controller.main_controller.create_user_use_case")
@patch("interface.controller.main_controller.GenerateFakeUserUseCase.execute")
def test_main_controller_execute(
    mock_generate_fake_user,
    mock_create_user,
    mock_get_token,
    mock_get_books,
    mock_generate_csv,
    mock_user,
    mock_books
):
    """
    Test the execute method of the MainController class.

    This test verifies that the execute method of the MainController class
    correctly calls the other methods of the class in the correct order.

    The test provides a mocked UserDTO instance and a list of two BookDTO
    instances as fixtures. The test then verifies that the execute method
    correctly calls the following methods with the correct arguments:

    - GenerateFakeUserUseCase.execute
    - create_user_use_case
    - get_token_use_case
    - get_books_use_case
    - generate_books_csv_use_case

    Args:
        mock_generate_fake_user: A mock of the GenerateFakeUserUseCase.execute method.
        mock_create_user: A mock of the create_user_use_case function.
        mock_get_token: A mock of the get_token_use_case function.
        mock_get_books: A mock of the get_books_use_case function.
        mock_generate_csv: A mock of the generate_books_csv_use_case function.
        mock_user: A fixture providing a mocked UserDTO instance.
        mock_books: A fixture providing a list of two BookDTO instances.
    """
    base_url = "http://api.exemplo.com"
    csv_path = "output/test_books.csv"
    controller = MainController(base_url)

    mock_generate_fake_user.return_value = mock_user
    mock_create_user.return_value = mock_user
    mock_get_token.return_value = "mock_token"
    mock_get_books.return_value = mock_books

    controller.execute(csv_path)

    mock_generate_fake_user.assert_called_once()
    mock_create_user.assert_called_once_with(base_url, mock_user)
    mock_get_token.assert_called_once_with(base_url, mock_user)
    mock_get_books.assert_called_once_with(base_url, "mock_token")
    mock_generate_csv.assert_called_once_with(mock_books, csv_path)
