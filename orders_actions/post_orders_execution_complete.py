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
        orders_execution_complete(jwt_token=jwt_token,
                                  order_id=order_id,
                                  base_url=base_url)


def main(username, password, sec_id, amount, order_id, base_url):
    login = LoginUsers(username=username,
                       password=password,
                       sec_id=sec_id)
    jwt = login.login_users(base_url)
    complete_orders(jwt_token=jwt,
                    amount=amount,
                    order_id=order_id,
                    base_url=base_url)


if __name__ == '__main__':
    main(username=USER_NAME,
         password=PASSWORD,
         sec_id=SEC_ID,
         amount=20,
         order_id=5672,
         base_url=BASE_URL_DEV)
