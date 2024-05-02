import requests
from config.config import TestData
from user_actions.login_user import LoginUsers


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
            print(f'Status code: {response.status_code}', sep='\n')
        else:
            print(f'Something went wrong, status code: {response.status_code}')
    except:
        print(BaseException('Error occurred'))


if __name__ == '__main__':
    login = LoginUsers(username=TestData.USER_NAME, password=TestData.PASSWORD, sec_id=TestData.SEC_ID)
    jwt = login.login_users()
    referral_tokens(jwt)