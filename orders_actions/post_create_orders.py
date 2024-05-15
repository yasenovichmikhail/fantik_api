import requests
from config.config import *
from user_actions.login_user import LoginUsers


def create_orders(jwt_token, action_type, amount, aweme_id=None):
    try:
        headers = {
            'accept': 'application/json',
            'Authorization1': jwt_token
        }

        body = {
            "actionTypeId": action_type,
            "awemeId": aweme_id,
            "shortLink": None,
            "actionsAmount": amount,
            "orderDurationHours": 0,
            "orderName": "test",
            "rewardId": None
        }

        response = requests.post(f'{TestData.BASE_URL}' + f'{TestData.ORDERS_CREATE_PATH}', headers=headers, json=body)
        if response.status_code == 200:
            print(f'Your order successfully created', f'Status code: {response.status_code}', sep='\n')
        else:
            print(f'Something went wrong, status code: {response.status_code}')
    except BaseExceptions:
        print('Error occurred:\n', traceback.format_exc())


if __name__ == '__main__':
    login = LoginUsers(username=TestData.USER_NAME, password=TestData.PASSWORD, sec_id=TestData.SEC_ID)
    jwt = login.login_users()
    create_orders(jwt_token=jwt, action_type=4, amount=10)
