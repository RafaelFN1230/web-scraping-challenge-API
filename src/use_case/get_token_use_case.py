from infrastructure.API.get_token import get_token
from domain.entities.User import User

def get_token_use_case(base_url: str, user: User) -> str:
    return get_token(base_url, user)
