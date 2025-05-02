from interface.controller.DTOs.UserDTO import UserDTO
from domain.entities.User import User
from infrastructure.API.create_user import create_user
from utils.logger import get_logger
logger = get_logger(__name__)
def create_user_use_case(base_url: str, user_dto: UserDTO) -> User:
    """
    Creates a new user on the external service using the provided user information.

    Args:
        base_url (str): The base URL of the external service API.
        user_dto (UserDTO): The data transfer object containing user details.

    Returns:
        User: The created user entity with email and password.
    """
    if not isinstance(base_url, str) or not base_url.startswith('http') or base_url.endswith("/"):
        raise TypeError("base_url deve ser uma string válida, que começa com 'http' e não termina com '/'")

    if not isinstance(user_dto, UserDTO):
        raise TypeError("user_dto deve ser uma instância de UserDTO")
    
    logger.info("Iniciando create user use case.")

    user = User(user_dto.email, user_dto.password)
    create_user(base_url, user)

    logger.info("User criado com sucesso.")
    return user

    