import requests
import json

from domain.entities.User import User

def get_token(base_url, user: User):
    """
    Requests a token for the given user.

    Args:
        base_url (str): The base URL of the API.
        user (User): The user to request a token for.

    Returns:
        str: The token for the user.

    Raises:
        Exception: If the request fails.
    """
    url = f"{base_url}/Account/v1/GenerateToken"

    payload = json.dumps({
    "userName": user.email,
    "password": user.password
    })

    headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    if response.status_code == 200:
        return response.json()["token"]
    else:
        raise Exception (f"Erro {response.status_code}: {response.text}")
