from interface.controller.DTOs.UserDTO import UserDTO
from domain.entities.User import User
from infrastructure.API.create_user import create_user
from utils.logger import get_logger
logger = get_logger(__name__)
def create_user_use_case(base_url: str, user_dto: UserDTO) -> User:
    logger.info("Iniciando create user use case.")

    user = User(user_dto.email, user_dto.password)
    create_user(base_url, user)

    logger.info("User criado com sucesso.")
    return user
