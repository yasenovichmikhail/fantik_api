import requests
from config.config import *
from user_actions.login_user import LoginUsers


def orders_execution_complete(jwt_token, order_id, base_url, device_type=DEVICE_TYPE):
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

        response = requests.post(f'{base_url}' + f'{POST_ORDERS_EXECUTION_COMPLETE_PATH}',
                                 headers=headers, json=body)
        print(f'Status code: {response.status_code}')
    except BaseExceptions:
        print('Error occurred:\n', traceback.format_exc())


def complete_orders(jwt_token, amount, order_id, base_url):
    for i in range(amount):
        orders_execution_complete(jwt_token=jwt_token, order_id=order_id, base_url=base_url)


def main():
    login = LoginUsers(username='psp',
                       password='qwertyasd',
                       sec_id='MS4wLjABAAAAfqnocaqWXSt7uMB39wpWj0u4DolsPbo6WJdayt6-vtY')
    jwt = login.login_users(BASE_URL_DEV)
    complete_orders(jwt, 10, 5561, base_url=BASE_URL_DEV)


if __name__ == '__main__':
    main()
