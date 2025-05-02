from domain.entities.User import User
from interface.controller.DTOs.UserDTO import UserDTO


def user_entity_to_dto(user: User) -> UserDTO:
    return UserDTO(
        email=user.email,
        password=user.password
    )
