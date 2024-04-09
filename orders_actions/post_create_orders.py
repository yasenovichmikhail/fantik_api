import requests
from config.config import TestData
import json
from user_actions.login_user import LoginUsers
from pprint import *

login = LoginUsers(username=TestData.USER_NAME, password=TestData.PASSWORD, sec_id=TestData.SEC_ID)


def create_orders(jwt_token):

    headers = {
        'accept': 'application/json',
        'Authorization1': jwt_token
    }

    body = TestData.ORDER_BODY

    response = requests.post(f'{TestData.BASE_URL}' + f'{TestData.ORDERS_CREATE_PATH}', headers=headers, json=body)
    return print(f'Status code: {response.status_code}', f'Your order successfully created', sep='\n')


jwt = login.login_users()
create_orders(jwt)