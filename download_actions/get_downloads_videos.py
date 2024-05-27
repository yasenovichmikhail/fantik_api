import requests
from config.config import *
from user_actions.login_user import LoginUsers
from pprint import *


def get_download_videos(jwt_token):
    try:
        headers = {
            'accept': 'application/json',
            'Authorization1': jwt_token
        }
        response = requests.get(f'{TestData.BASE_URL}' + f'{TestData.DOWNLOAD_VIDEOS_PATH}', headers=headers)
        if response.status_code == 200:
            print(f'Status code: {response.status_code}', sep='\n')
            pprint(response.json())
        else:
            print(f'Something went wrong, status code: {response.status_code}')
    except BaseExceptions:
        print('Error occurred:\n', traceback.format_exc())


login = LoginUsers(TestData.USER_NAME, TestData.PASSWORD, TestData.SEC_ID)
jwt = login.login_users()
get_download_videos(jwt)
