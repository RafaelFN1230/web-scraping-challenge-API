import requests
import json
from domain.entities.User import User

def create_user(base_url: str, user: User):
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
