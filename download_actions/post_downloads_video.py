import requests
from config.config import *
from user_actions.login_user import LoginUsers
from pprint import *


def post_download_videos(jwt_token, base_url):
    try:
        headers = {
            'accept': 'application/json',
            'Authorization1': jwt_token
        }

        body = {
            'postLink': POST_SHORT_LINK
        }

        response = requests.post(f'{base_url}' + f'{DOWNLOAD_VIDEOS_PATH}',
                                 headers=headers,
                                 json=body)
        if response.status_code == 200:
            print(f'Status code: {response.status_code}', sep='\n')
            pprint(response.json())
        else:
            print(f'Something went wrong, status code: {response.status_code}')
    except BaseExceptions:
        print('Error occurred:\n', traceback.format_exc())


login = LoginUsers(USER_NAME, PASSWORD, SEC_ID)
jwt = login.login_users(BASE_URL_DEV)
post_download_videos(jwt, BASE_URL_DEV)



