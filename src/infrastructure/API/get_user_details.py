import requests

def get_user_by_id(user_id: str, authorization_token: str):
    url = f'https://demoqa.com/Account/v1/User/{user_id}'
    headers = {
        'Accept': '*/*',
        'Authorization': f'Basic {authorization_token}',
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json() 
    else:
        raise Exception(f'Erro {response.status_code}: {response.text}') 
