from domain.entities.User import User
from interface.controller.DTOs.UserDTO import UserDTO


def user_entity_to_dto(user: User) -> UserDTO:
    """
    Maps a User entity into a UserDTO.

    Args:
        user: User entity to be mapped.

    Returns:
        UserDTO: The mapped UserDTO.
    """
    return UserDTO(
        email=user.email,
        password=user.password
    )
