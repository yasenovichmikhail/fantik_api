import requests
from config.config import *
from user_actions.login_user import LoginUsers


def post_orders_execution_complete(jwt_token, device_type):
    headers = {
        'accept': 'application/json',
        'Authorization1': jwt_token,
        'device_type_id': device_type
    }
    body = COMPLETE_ORDERS_BODY

    response = requests.post(f'{BASE_URL}' + f'{POST_ORDERS_EXECUTION_COMPLETE_PATH}',
                             headers=headers, json=body)
    print(f'Status code: {response.status_code}')


def complete_orders(amount, jwt_token):
    for i in range(amount):
        post_orders_execution_complete(jwt_token, DEVICE_TYPE)


login = LoginUsers(username=USER_NAME, password=PASSWORD, sec_id=SEC_ID)
jwt = login.login_users()

complete_orders(ORDER_AMOUNT, jwt)
