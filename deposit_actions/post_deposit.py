import requests
from config.config import *
from user_actions.login_user import LoginUsers
from pprint import *


def post_deposits(jwt_token, amount, base_url):
    try:
        headers = {
            'accept': 'application/json',
            'Authorization1': jwt_token
        }

        body = {
            'amountDepositsToIncrease': amount
        }

        response = requests.post(f'{base_url}' + f'{POST_DEPOSITS_PATH}', headers=headers,
                                 json=body)
        if response.status_code == 200:
            print(f'Status code: {response.status_code}', sep='\n')
            return response.json()
        else:
            print(f'Something went wrong, status code: {response.status_code}')
    except BaseExceptions:
        print('Error occurred:\n', traceback.format_exc())


def main(username, password, sec_id, amount, base_url):
    login = LoginUsers(username=username,
                       password=password,
                       sec_id=sec_id)
    jwt = login.login_users(base_url)
    result = post_deposits(jwt_token=jwt,
                           amount=amount,
                           base_url=base_url)
    return result


if __name__ == '__main__':
    main(username=USER_NAME, password=PASSWORD, sec_id=SEC_ID, base_url=BASE_URL_DEV, amount=10000)
