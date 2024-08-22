import requests
from config.config import *
from user_actions.login_user import LoginUsers


def email_bound_request(jwt_token, email, base_url):
    headers = {
        'Authorization1': jwt_token
    }

    body = {
        'email': email
    }

    response = requests.post(f'{base_url}' + f'{POST_EMAIL_REQUEST_PATH}', headers=headers,
                             json=body)
    key = response.json()['key']
    return key


def email_bound_confirm(key, base_url):
    body = {
        'key': key
    }

    response = requests.post(f'{base_url}' + f'{POST_EMAIL_CONFIRM_PATH}', json=body)
    print(f'Status code: {response.status_code}', f'Your email has been changed successfully', sep='\n')


def bound_email(jwt_token, email, base_url):
    key = email_bound_request(jwt_token=jwt_token, email=email, base_url=base_url)
    email_bound_confirm(key=key, base_url=base_url)


def main(username, password, sec_id, email, base_url):
    login = LoginUsers(username=username, password=password, sec_id=sec_id)
    jwt = login.login_users(base_url=base_url)
    bound_email(jwt_token=jwt, email=email, base_url=base_url)


if __name__ == '__main__':
    main(username=USER_NAME, password=PASSWORD, sec_id=SEC_ID, email=EMAIL, base_url=BASE_URL_DEV)

