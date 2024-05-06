import requests
from config.config import *
from user_actions.login_user import LoginUsers
from pprint import *


def referral_tokens(jwt_token):
    try:
        headers = {
            'accept': 'application/json',
            'Authorization1': jwt_token
        }

        body = {
            'usage_type': 'USER_REGISTRATION'
        }

        response = requests.post(f'{TestData.BASE_URL}' + f'{TestData.REFERRAL_TOKENS_PATH}', headers=headers,
                                 json=body)
        if response.status_code == 200:
            pprint(response.json())
        else:
            print(f'Something went wrong, status code: {response.status_code}')
    except BaseExceptions:
        print('Error occurred:\n', traceback.format_exc())


login = LoginUsers(username=TestData.USER_NAME, password=TestData.PASSWORD, sec_id=TestData.SEC_ID)
jwt = login.login_users()
referral_tokens(jwt)
