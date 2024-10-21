import requests
from config.config import *
from user_actions.login_user import LoginUsers
from pprint import *


def ban_user(user_id):
    try:
        headers = {
            'user_id': user_id
        }

        response = requests.get(f'{BASE_URL_PROD}' + f'{BAN_USERS}', headers=headers)
        if response.status_code == 200:
            print(f'Status code: {response.status_code}', sep='\n')
            print(response.content)
        else:
            print(f'Something went wrong, status code: {response.status_code}')
    except:
        BaseException("Error occurred")


def main(user_id):
    ban_user(user_id=user_id)


if __name__ == '__main__':
    main(user_id=1408103)
