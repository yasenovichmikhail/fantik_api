import requests
from config.config import *
from user_actions.login_user_dev import LoginUsers


def orders_execution_complete(jwt_token, order_id, device_type=DEVICE_TYPE):
    try:
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

        response = requests.post(f'{BASE_URL_DEV}' + f'{POST_ORDERS_EXECUTION_COMPLETE_PATH}',
                                 headers=headers, json=body)
        print(f'Status code: {response.status_code}')
    except BaseExceptions:
        print('Error occurred:\n', traceback.format_exc())


def complete_orders(jwt_token, amount, order_id):
    for i in range(amount):
        orders_execution_complete(jwt_token=jwt_token, order_id=order_id, device_type=DEVICE_TYPE)


if __name__ == '__main__':
    login = LoginUsers(username='klio', password='qwertyasd',
                       sec_id='MS4wLjABAAAApS6u0PpUEzf8UwD32MAktyUQYKQO8s0GkpuxKNpkytPW9LteiX7Hx9RfCXwc034N')
    jwt = login.login_users()
    complete_orders(jwt, 9, 5454)
