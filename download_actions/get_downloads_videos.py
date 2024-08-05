import requests
from config.config import *
from user_actions.login_user import LoginUsers
from pprint import *


def get_download_videos(jwt_token, base_url):
    try:
        headers = {
            'accept': 'application/json',
            'Authorization1': jwt_token
        }
        response = requests.get(f'{base_url}' + f'{DOWNLOAD_VIDEOS_PATH}', headers=headers)
        if response.status_code == 200:
            print(f'Status code: {response.status_code}', sep='\n')
            return response.json()
        else:
            print(f'Something went wrong, status code: {response.status_code}')
    except BaseExceptions:
        print('Error occurred:\n', traceback.format_exc())


def main(username, password, sec_id, base_url):
    login = LoginUsers(username=username,
                       password=password,
                       sec_id=sec_id)
    jwt = login.login_users(base_url)
    video = get_download_videos(jwt_token=jwt,
                                base_url=base_url)
    return pprint(video)


if __name__ == '__main__':
    main(username=USER_NAME, password=PASSWORD, sec_id=SEC_ID, base_url=BASE_URL_PROD)
