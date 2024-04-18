import requests
from config.config import TestData
from user_actions.login_user import LoginUsers
from pprint import *


def get_orders_execution(jwt_token):
    headers = {
        'accept': 'application/json',
        'Authorization1': jwt_token
    }

    response = requests.get(f'{TestData.BASE_URL}' + f'{TestData.GET_ORDERS_EXECUTION_PATH}', headers=headers)
    print(f'Status code: {response.status_code}')
    return pprint(response.json())


login = LoginUsers(username=TestData.USER_NAME, password=TestData.PASSWORD, sec_id=TestData.SEC_ID)
jwt = login.login_users()
get_orders_execution(jwt)
