import requests
from config.config import TestData
from user_actions.login_user import LoginUsers
from pprint import *


def post_download_videos(jwt_token):
    try:
        headers = {
            'accept': 'application/json',
            'Authorization1': jwt_token
        }

        body = {
            'postLink': TestData.POST_SHORT_LINK
        }

        response = requests.post(f'{TestData.BASE_URL}' + f'{TestData.DOWNLOAD_VIDEOS_PATH}', headers=headers,
                                 json=body)
        if response.status_code == 200:
            print(f'Status code: {response.status_code}', sep='\n')
            pprint(response.json())
        else:
            print(f'Something went wrong, status code: {response.status_code}')
    except:
        BaseException("Error occurred")


login = LoginUsers(TestData.USER_NAME, TestData.PASSWORD, TestData.SEC_ID)
jwt = login.login_users()
resp = post_download_videos(jwt)

