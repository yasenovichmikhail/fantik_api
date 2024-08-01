import requests
from config.config import *
from user_actions.login_user import LoginUsers


def create_orders(jwt_token, action_type, amount, order_duration_min, base_url, aweme_id=None):
    try:
        headers = {
            'accept': 'application/json',
            'Authorization1': jwt_token
        }
        if action_type != 5:
            body = {
                "actionTypeId": action_type,
                "awemeId": aweme_id,
                "shortLink": None,
                "actionsAmount": amount,
                "actionsFactor": 1,
                "orderDurationMinutes": order_duration_min,
                "orderName": "test",
                "rewardId": None
            }
        else:
            body = {
                "actionTypeId": action_type,
                "awemeId": aweme_id,
                "shortLink": None,
                "actionsAmount": amount,
                "actionsFactor": 1000,
                "orderDurationMinutes": order_duration_min,
                "orderName": "test",
                "rewardId": None
            }

        response = requests.post(f'{base_url}' + f'{ORDERS_CREATE_PATH}', headers=headers, json=body)
        if response.status_code == 200:
            print(f'Your order successfully created', f'Status code: {response.status_code}', sep='\n')
        else:
            print(f'Something went wrong, status code: {response.status_code}')
    except BaseExceptions:
        print('Error occurred:\n', traceback.format_exc())


def main(username, password, sec_id, action_type, amount, order_duration_min, base_url, aweme_id=None):
    login = LoginUsers(username=username, password=password, sec_id=sec_id)
    jwt = login.login_users(env=base_url)
    create_orders(jwt_token=jwt,
                  action_type=action_type,
                  amount=amount,
                  order_duration_min=order_duration_min,
                  aweme_id=aweme_id,
                  base_url=base_url)


if __name__ == '__main__':
    main(username=USER_NAME,
         password=PASSWORD,
         sec_id=SEC_ID,
         action_type=5,
         amount=1000,
         order_duration_min=30,
         aweme_id=AWEME_ID,
         base_url=BASE_URL_DEV)
