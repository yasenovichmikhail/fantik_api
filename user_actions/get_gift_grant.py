import requests
from config.config import TestData
from user_actions.login_user import LoginUsers
from pprint import *


def get_gift_grant(jwt_token):
    try:
        headers = {
            'accept': 'application/json',
            'Authorization1': jwt_token
        }

        response = requests.get(f'{TestData.BASE_URL}' + f'{TestData.GET_GIFT_GRANT_PATH}', headers=headers)
        if response.status_code == 200:
            print(f'Status code: {response.status_code}', f'The gift was successfully used', sep='\n')
            pprint(response.json())
        elif response.status_code == 403:
            print(f'Status code: {response.status_code}', f'The gift is not available', sep='\n')
        else:
            print(f'Something went wrong, status code: {response.status_code}')
    except:
        BaseException("Error occurred")


login = LoginUsers(username=TestData.USER_NAME, password=TestData.PASSWORD, sec_id=TestData.SEC_ID)
jwt = login.login_users()
get_gift_grant(jwt)