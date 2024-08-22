from dataclasses import dataclass
from config.config import *
from user_actions.login_user import LoginUsers


def user_auth(jwt_token, base_url):
    try:
        headers = {'accept': 'application/json',
                   'Authorization1': jwt_token}
        response = requests.post(f'{base_url}' + f'{POST_USERS_AUTH_PATH}', headers=headers)
        if response.status_code == 200:
            print(f'Status code: {response.status_code}', f'Jwt was successfully updated', sep='\n')
            return print(response.json()['jwt'])
        elif response.status_code == 403:
            print(f'Status code: {response.status_code}', f'Forbidden', sep='\n')
        else:
            print(f'Something went wrong, status code: {response.status_code}')
    except BaseExceptions:
        print('Error occurred:\n', traceback.format_exc())


def main(username, password, sec_id, base_url):
    login = LoginUsers(username=username, password=password, sec_id=sec_id)
    jwt = login.login_users(base_url=base_url)
    user_auth(jwt_token=jwt, base_url=base_url)


if __name__ == '__main__':
    main(username=USER_NAME, password=PASSWORD, sec_id=SEC_ID, base_url=BASE_URL_DEV)

