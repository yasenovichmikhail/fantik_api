import requests
from config.config import *
from user_actions.login_user import LoginUsers
from pprint import *


def get_users_email(jwt_token):
    try:
        headers = {
            'accept': 'application/json',
            'Authorization1': jwt_token
        }

        response = requests.get(f'{BASE_URL}' + f'{GET_USERS_EMAIL_PATH}', headers=headers)
        if response.status_code == 200:
            print(f'Status code: {response.status_code}', sep='\n')
            print(response.content)
        elif response.status_code == 204:
            print(f'Status code: {response.status_code}', f'User has no bounded email address', sep='\n')
        else:
            print(f'Something went wrong, status code: {response.status_code}')
    except:
        BaseException("Error occurred")


login = LoginUsers(username=USER_NAME, password=PASSWORD, sec_id=SEC_ID)
jwt = login.login_users()
get_users_email(jwt)
