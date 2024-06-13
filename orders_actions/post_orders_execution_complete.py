import requests
from config.config import *
from user_actions.login_user import LoginUsers


def orders_execution_complete(jwt_token, order_id, device_type=DEVICE_TYPE):
    headers = {
        'accept': 'application/json',
        'Authorization1': jwt_token,
        'device_type_id': device_type
    }
    body = {
        "orderId": order_id,
        "metricsAmountBefore": 1,
        "metricsAmountAfter": 2,
        "startDate": CURRENT_TIMESTAMP,
        "finishDate": CURRENT_TIMESTAMP,
        "isAvailable": True,
        "isSkipped": False
    }

    response = requests.post(f'{BASE_URL}' + f'{POST_ORDERS_EXECUTION_COMPLETE_PATH}',
                             headers=headers, json=body)
    print(f'Status code: {response.status_code}')


def complete_orders(jwt_token, amount, order_id):
    for i in range(amount):
        orders_execution_complete(jwt_token=jwt_token, order_id=order_id, device_type=DEVICE_TYPE)


if __name__ == '__main__':
    login = LoginUsers(username=USER_NAME, password=PASSWORD, sec_id=SEC_ID)
    jwt = login.login_users()
    complete_orders(jwt, 9, 5445)
