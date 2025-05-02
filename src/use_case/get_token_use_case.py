from infrastructure.API.get_token import get_token
from domain.entities.User import User
from utils.logger import get_logger

logger = get_logger(__name__)
def get_token_use_case(base_url: str, user: User) -> str:
    logger.info("Iniciando coleta de token.")
    token = get_token(base_url, user)
    logger.info("Token coletado com sucesso.")
    return token
