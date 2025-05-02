from interface.controller.DTOs.UserDTO import UserDTO
from domain.entities.User import User
from infrastructure.API.create_user import create_user

def create_user_use_case(base_url: str, user_dto: UserDTO) -> User:
    user = User(user_dto.email, user_dto.password)
    create_user(base_url, user)
    return user
