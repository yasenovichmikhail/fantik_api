import requests
from config.config import TestData
from user_actions.login_user import LoginUsers
from pprint import *


def post_deposits(jwt_token):
    try:
        headers = {
            'accept': 'application/json',
            'Authorization1': jwt_token
        }

        body = TestData.DEPOSIT_BODY

        response = requests.post(f'{TestData.BASE_URL}' + f'{TestData.POST_DEPOSITS_PATH}', headers=headers,
                                 json=body)
        if response.status_code == 200:
            print(f'Status code: {response.status_code}', sep='\n')
            pprint(response.json())
        else:
            print(f'Something went wrong, status code: {response.status_code}')
    except:
        BaseException("Error occurred")


login = LoginUsers(TestData.USER_NAME, TestData.PASSWORD, TestData.SEC_ID)
jwt = login.login_users()
post_deposits(jwt)
