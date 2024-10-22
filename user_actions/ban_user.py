import requests
from config.config import *
from user_actions.login_user import LoginUsers
from pprint import *


def ban_user(user_id, base_url):
    try:
        params = {
            'user_id': user_id
        }

        response = requests.get(f'{base_url}' + f'{BAN_USERS}', params=params)
        if response.status_code == 200:
            print(f'Status code: {response.status_code}', sep='\n')
            print(f'User {user_id} was banned')
        else:
            print(f'Something went wrong, status code: {response.status_code}')
    except:
        BaseException("Error occurred")


if __name__ == '__main__':
    ban_user(user_id=1460036,
             base_url=BASE_URL_PROD)
