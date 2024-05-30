import requests
from config.config import *
from user_actions.login_user import LoginUsers
from pprint import *


def referral_validate(jwt_token):
    try:
        response_value_expected = ['token', 'token_type', 'validity']
        response_value_actual = []
        headers = {
            'accept': 'application/json',
            'Authorization1': jwt_token
        }

        body = REFERRAL_TOKEN_BODY

        response = requests.post(f'{BASE_URL}' + f'{REFERRAL_VALIDATE_PATH}', headers=headers,
                                 json=body)
        if response.status_code == 200:
            print(f'Status code: {response.status_code}', sep='\n')
            pprint(response.json())
            # resp = response.json()
            # for key in resp.keys():
            #     response_value_actual.append(key)
            # assert response_value_actual == response_value_expected, f"Response body doesn't match, " \
            #                                                          f"Expected {response_value_expected}, " \
            #                                                          f"got {response_value_actual}"
        else:
            print(f'Something went wrong, status code: {response.status_code}')
    except BaseExceptions:
        print('Error occurred:\n', traceback.format_exc())


login = LoginUsers(username=USER_NAME, password=PASSWORD, sec_id=SEC_ID)
jwt = login.login_users()
referral_validate(jwt)