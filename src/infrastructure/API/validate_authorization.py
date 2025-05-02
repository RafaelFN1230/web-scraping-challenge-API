import requests
import json
from domain.entities.User import User

def validate_authorization(base_url: str, user: User) -> bool:
    """
    Validates if a user has recived the proper authorization.

    Args:
        base_url (str): The base URL of the external service API.
        user (User): The user to be validated.

    Returns:
        bool: True if the user is authorized, False otherwise.

    Raises:
        Exception: If the request fails.
    """
    url = f"{base_url}/Account/v1/Authorized"
    payload = json.dumps({
        "userName": user.email,
        "password": user.password
    })
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    response = requests.post(url, headers=headers, data=payload)

    if response.status_code == 200:
        return response.json() is True
    elif response.status_code == 401:
        return False
    else:
        raise Exception(f"Erro {response.status_code}: {response.text}")
