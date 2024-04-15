import requests
from config.config import TestData
from user_actions.login_user import LoginUsers


def post_orders_execution_complete(jwt_token, device_type):
    headers = {
        'accept': 'application/json',
        'Authorization1': jwt_token,
        'device_type_id': device_type
    }
    body = TestData.COMPLETE_ORDERS_BODY

    response = requests.post(f'{TestData.BASE_URL}' + f'{TestData.POST_ORDERS_EXECUTION_COMPLETE_PATH}',
                             headers=headers, json=body)
    print(f'Status code: {response.status_code}')


def complete_orders(amount, jwt_token):
    for i in range(amount):
        post_orders_execution_complete(jwt_token, TestData.DEVICE_TYPE)


login = LoginUsers(username=TestData.USER_NAME, password=TestData.PASSWORD, sec_id=TestData.SEC_ID)
jwt = login.login_users()

complete_orders(TestData.ORDER_AMOUNT, jwt)
