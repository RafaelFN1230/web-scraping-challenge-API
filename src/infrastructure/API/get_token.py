import requests
import json

from domain.entities.User import User

def get_token(base_url, user: User):
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
