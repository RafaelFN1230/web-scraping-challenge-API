from interface.controller.DTOs.UserDTO import UserDTO
from use_case.create_user_use_case import create_user_use_case
from use_case.get_token_use_case import get_token_use_case
from use_case.get_books_use_case import get_books_use_case
from use_case.generate_csv_use_case import generate_books_csv_use_case
from use_case.generate_fake_user import GenerateFakeUserUseCase

class MainController:
    def __init__(self, base_url: str):
        self.base_url = base_url

    def execute(self, csv_path: str):
        user_data = GenerateFakeUserUseCase.execute()
        user = create_user_use_case(self.base_url, user_data)
        token = get_token_use_case(self.base_url, user)
        books = get_books_use_case(self.base_url, token)
        generate_books_csv_use_case(books, csv_path)
