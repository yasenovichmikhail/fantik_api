import requests
from config.config import *
from user_actions.login_user import LoginUsers
from pprint import *


def referral_validate(jwt_token, base_url):
    try:
        headers = {
            'accept': 'application/json',
            'Authorization1': jwt_token
        }

        body = REFERRAL_TOKEN_BODY

        response = requests.post(f'{base_url}' + f'{REFERRAL_VALIDATE_PATH}',
                                 headers=headers,
                                 json=body)
        if response.status_code == 200:
            print(f'Status code: {response.status_code}', sep='\n')
            pprint(response.json())
        else:
            print(f'Something went wrong, status code: {response.status_code}')
    except BaseExceptions:
        print('Error occurred:\n', traceback.format_exc())


def main(base_url):
    login = LoginUsers(username=USER_NAME, password=PASSWORD, sec_id=SEC_ID)
    jwt = login.login_users(base_url)
    referral_validate(jwt, base_url)


if __name__ == '__main__':
    main(BASE_URL_DEV)
