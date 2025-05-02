from interface.controller.DTOs.UserDTO import UserDTO
from utils.random_helpers import generate_random_string, generate_strong_password


class GenerateFakeUserUseCase:
    @staticmethod
    def execute() -> UserDTO:
        first_name = generate_random_string()
        last_name = generate_random_string()
        email = f"{first_name.lower()}.{last_name.lower()}@email.com"
        password = generate_strong_password()

        return UserDTO(
            email=email,
            password=password
        )
