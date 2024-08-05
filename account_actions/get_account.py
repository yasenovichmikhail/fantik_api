from config.config import *
import requests
from user_actions.login_user import LoginUsers
from pprint import *


def get_account_info(jwt_token, base_url):
    try:
        headers = {'Authorization1': jwt_token}

        response = requests.get(f'{base_url}' + f'{GET_ACCOUNT_PATH}', headers=headers)
        print(f'Status code: {response.status_code}')
        assert response.status_code == 200, f"Request is failed with status code: {response.status_code}"
        return response.json()
    except BaseExceptions:
        print('Error occurred:\n', traceback.format_exc())


def main(username, password, sec_id, base_url):
    login = LoginUsers(username=username,
                       password=password,
                       sec_id=sec_id)
    jwt = login.login_users(base_url)
    result = get_account_info(jwt_token=jwt,
                              base_url=base_url)
    return pprint(result)


if __name__ == '__main__':
    main(USER_NAME, PASSWORD, SEC_ID, BASE_URL_DEV)
