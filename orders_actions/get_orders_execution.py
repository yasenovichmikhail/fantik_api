import requests
from config.config import *
from user_actions.login_user import LoginUsers
from pprint import *


def get_orders_execution(jwt_token, base_url):
    headers = {
        'accept': 'application/json',
        'Authorization1': jwt_token
    }

    response = requests.get(f'{base_url}' + f'{GET_ORDERS_EXECUTION_PATH}', headers=headers)
    print(f'Status code: {response.status_code}')
    return pprint(response.json())


def main(base_url):
    login = LoginUsers(username=USER_NAME, password=PASSWORD, sec_id=SEC_ID)
    jwt = login.login_users(base_url)
    get_orders_execution(jwt, base_url)


if __name__ == '__main__':
    main(BASE_URL_PROD)
