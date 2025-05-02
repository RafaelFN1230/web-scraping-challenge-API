from interface.controller.DTOs.UserDTO import UserDTO
from use_case.create_user_use_case import create_user_use_case
from use_case.get_token_use_case import get_token_use_case
from use_case.get_books_use_case import get_books_use_case
from use_case.generate_csv_use_case import generate_books_csv_use_case
from use_case.generate_fake_user import GenerateFakeUserUseCase

class MainController:
    def __init__(self, base_url: str):
        """
        Initialize the MainController with a base URL.

        Args:
            base_url (str): The base URL for the API endpoints.
        """

        self.base_url = base_url

    def execute(self, csv_path: str):
        """
        Execute the entire workflow of the application.

        The workflow consists of the following steps:

        1. Generate a fake user using the GenerateFakeUserUseCase.
        2. Create the generated user using the create_user_use_case.
        3. Get a token for the created user using the get_token_use_case.
        4. Get the books using the get_books_use_case and the obtained token.
        5. Generate a CSV file with the books using the generate_books_csv_use_case.

        Args:
            csv_path (str): The path where the CSV file will be generated.
        """
        user_data = GenerateFakeUserUseCase.execute()
        user = create_user_use_case(self.base_url, user_data)
        token = get_token_use_case(self.base_url, user)
        books = get_books_use_case(self.base_url, token)
        generate_books_csv_use_case(books, csv_path)
