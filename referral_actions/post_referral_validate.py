import requests
from config.config import TestData
from user_actions.login_user import LoginUsers
from pprint import *


def referral_validate(jwt_token):
    try:
        headers = {
            'accept': 'application/json',
            'Authorization1': jwt_token
        }

        body = TestData.REFERRAL_TOKEN_BODY

        response = requests.post(f'{TestData.BASE_URL}' + f'{TestData.REFERRAL_VALIDATE_PATH}', headers=headers,
                                 json=body)
        if response.status_code == 200:
            print(f'Status code: {response.status_code}', sep='\n')
            pprint(response.json())
        else:
            print(f'Something went wrong, status code: {response.status_code}')
    except:
        print(BaseException("Error occurred"))


login = LoginUsers(username=TestData.USER_NAME, password=TestData.PASSWORD, sec_id=TestData.SEC_ID)
jwt = login.login_users()
referral_validate(jwt)