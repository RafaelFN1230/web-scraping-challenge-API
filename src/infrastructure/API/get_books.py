import requests

from interface.schema.api.api_book_schema import BookSchema
def get_books(base_url, token) -> list[BookSchema]:
    """
    Collect all books from API

    Args:
        base_url (str): The base URL of the API.
        token (str): The authorization token.

    Returns:
        list[BookSchema]: A list of books in BookSchema format

    Raises:
        Exception: If the request fails.
    """
    url = f"{base_url}/BookStore/v1/Books"

    payload = {}
    headers = {
    'Accept': '*/*',
    'Authorization': f'Basic {token}'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    if response.status_code == 200:
        books = []
        data = response.json()
        for book in data.get("books", []):
            books.append(book)
        return books
    else:
        raise Exception (f"Erro {response.status_code}: {response.text}")
