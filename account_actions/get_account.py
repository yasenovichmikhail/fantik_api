from config.config import TestData
import requests
from user_actions.login_user import LoginUsers
from pprint import *

login = LoginUsers(username=TestData.USER_NAME, password=TestData.PASSWORD, sec_id=TestData.SEC_ID)
jwt_auth = login.login_users()


def get_account_info():
    headers = {'Authorization1': jwt_auth}

    response = requests.get(f'{TestData.BASE_URL}' + f'{TestData.GET_ACCOUNT_PATH}', headers=headers)
    print(f'Status code: {response.status_code}')
    assert response.status_code == 200, f"Request is failed with status code: {response.status_code}"
    pprint(response.json())


get_account_info()