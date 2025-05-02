import pytest
from unittest.mock import patch, MagicMock
from infrastructure.API.get_books import get_books
from interface.controller.DTOs.BookDTO import BookDTO, BookStoreDataDTO
from interface.schema.api.api_book_schema import BookSchema
from use_case.get_books_use_case import get_books_use_case

@pytest.fixture
def mock_books():
    """
    Fixture providing a list of mock book data for testing.

    This fixture returns a list of dictionaries, where each dictionary represents
    a book with attributes such as isbn, title, subTitle, author, publish_date,
    publisher, pages, description, and website. This mock data is used for
    testing functions that interact with book information.

    Yields:
        A list of dictionaries representing mock book data.
    """
    return [
        {
            "isbn": "111",
            "title": "Book 1",
            "subTitle": "Sub 1",
            "author": "Author 1",
            "publish_date": "2021-01-01",
            "publisher": "Publisher 1",
            "pages": 100,
            "description": "Description 1",
            "website": "http://example.com/1"
        },
        {
            "isbn": "222",
            "title": "Book 2",
            "subTitle": "Sub 2",
            "author": "Author 2",
            "publish_date": "2022-02-02",
            "publisher": "Publisher 2",
            "pages": 200,
            "description": "Description 2",
            "website": "http://example.com/2"
        },
    ]

def test_get_books_use_case(mock_books):
    """
    Test the get_books_use_case function to ensure it retrieves and converts 
    book data correctly.

    This test verifies that the get_books_use_case function returns a list of 
    BookDTO instances when given a base URL and token. It checks that the 
    returned list contains the expected number of BookDTO objects and that 
    their attributes match the mock data provided.

    Args:
        mock_books: A pytest fixture providing mock book data for testing.

    Asserts:
        The result is a list.
        Each item in the result is an instance of BookDTO.
        The title of the first book in the result matches the expected value.
    """

    base_url = "http://api.example.com"
    token = "dummy_token"

    with patch("use_case.get_books_use_case.get_books") as mock_get_books:
        mock_get_books.return_value = mock_books

        result = get_books_use_case(base_url, token)

        assert isinstance(result, list)
        assert all(isinstance(book, BookDTO) for book in result)
        assert result[0].title == "Book 1"
