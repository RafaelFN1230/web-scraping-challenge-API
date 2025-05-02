import pytest
from domain.entities.User import User
from infrastructure.API.create_user import create_user
from infrastructure.API.get_books import get_books
from infrastructure.API.get_token import get_token
from infrastructure.API.validate_authorization import validate_authorization
from interface.schema.api.api_book_schema import BookSchema
from utils.random_helpers import generate_strong_password


BASE_URL = "https://demoqa.com"

@pytest.fixture
def new_user():
    """
    A pytest fixture that creates a new random user
    with a password that complies with the API's requirements.
    
    Returns:
        User: A new User instance with a random email and a strong password.
    """
    import random
    email = f"user{random.randint(1000, 9999)}@email.com"
    password = generate_strong_password()
    return User(email=email, password=password)

def test_create_user(new_user):
    """
    Tests the creation of a new user via the create_user API function.

    This test verifies that a user can be successfully created by checking
    if the response includes a 'userId' and if the 'username' in the response
    matches the email of the created user.

    Args:
        new_user (User): A pytest fixture that provides a new random User instance.

    Asserts:
        The response contains a 'userId'.
        The 'username' in the response matches the email of the new user.
    """

    response = create_user(BASE_URL, new_user)
    assert "userID" in response
    assert response["username"] == new_user.email

def test_get_token(new_user):
    """
    Tests the token generation for a newly created user via the get_token API function.

    This test verifies that a token can be successfully generated for a user
    by checking if the returned token is a non-empty string.

    Args:
        new_user (User): A pytest fixture that provides a new random User instance.

    Asserts:
        The token is an instance of str.
        The token has a length greater than 0.
    """

    create_user(BASE_URL, new_user)
    token = get_token(BASE_URL, new_user)
    assert isinstance(token, str)
    assert len(token) > 0

def test_validate_user(new_user):
    """
    Tests the validation of a newly created user via the validate_user API function.

    This test verifies that a user can be successfully validated by checking
    if the validate_user function returns True.

    Args:
        new_user (User): A pytest fixture that provides a new random User instance.

    Asserts:
        The validate_user function returns True.
    """

    create_user(BASE_URL, new_user)
    get_token(BASE_URL, new_user)
    is_authorized = validate_authorization(BASE_URL, new_user)
    assert is_authorized is True

def test_get_books(new_user):
    """
    Tests the retrieval of books via the get_books API function.

    This test ensures that books can be successfully retrieved for a user by checking
    if the returned books are in a list format. It verifies that each book contains
    valid 'title', 'publisher', and 'author' fields that are non-empty strings.

    Args:
        new_user (User): A pytest fixture that provides a new random User instance.

    Asserts:
        The books are returned as a list.
        Each book has a non-empty 'title', 'publisher', and 'author' field.
    """

    create_user(BASE_URL, new_user)
    token = get_token(BASE_URL, new_user)
    books = get_books(BASE_URL, token)
    
    assert isinstance(books, list)
    if books:
        for book in books:
            assert "title" in book and isinstance(book["title"], str) and book["title"].strip() != ""
            assert "publisher" in book and isinstance(book["publisher"], str) and book["publisher"].strip() != ""
            assert "author" in book and isinstance(book["author"], str) and book["author"].strip() != ""