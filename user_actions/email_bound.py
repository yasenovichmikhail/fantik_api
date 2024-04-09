import requests
from config.config import TestData
from user_actions.login_user import LoginUsers


login = LoginUsers(username=TestData.USER_NAME, password=TestData.PASSWORD, sec_id=TestData.SEC_ID)
jwt_auth = login.login_users()


def email_bound_request(jwt_token):
    headers = {
        'Authorization1': jwt_token
    }

    body = {
        'email': TestData.EMAIL
    }

    response = requests.post(f'{TestData.BASE_URL}' + f'{TestData.POST_EMAIL_REQUEST_PATH}', headers=headers,
                             json=body)
    key = response.json()['key']
    # print(f'Status code: {response.status_code}', key, sep='\n')
    return key


def email_bound_confirm(key):
    body = {
        'key': key
    }

    response = requests.post(f'{TestData.BASE_URL}' + f'{TestData.POST_EMAIL_CONFIRM_PATH}', json=body)
    print(f'Status code: {response.status_code}', f'Your email has been changed successfully', sep='\n')


def bound_email(jwt):
    key = email_bound_request(jwt)
    email_bound_confirm(key)


bound_email(jwt_auth)

