import requests
import json
from domain.entities.User import User

def create_user(base_url: str, user: User):
    """
    Creates a new user account using the given base URL and user details.

    Args:
        base_url (str): The base URL of the API endpoint.
        user (User): An instance of the User entity containing email and password.

    Returns:
        dict: A JSON response containing the details of the created user.

    Raises:
        Exception: If the user already exists (status code 406) or any other error occurs.
    """

    url = f"{base_url}/Account/v1/User"
    payload = json.dumps({
        "userName": user.email, 
        "password": user.password
    })
    headers = {
        'Content-Type': 'application/json', 
        'Accept': '*/*'
    }

    response = requests.post(url, headers=headers, data=payload)
    if response.status_code == 201:
        return response.json()
    elif response.status_code == 406:
        raise Exception ("Usuário já existe.")
    else:
        raise Exception(f"Erro {response.status_code}: {response.text}")
