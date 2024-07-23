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
            pprint(response.json())
            return response.json()
        else:
            print(f'Something went wrong, status code: {response.status_code}')
    except BaseExceptions:
        print('Error occurred:\n', traceback.format_exc())


login = LoginUsers('aaaaa75017', PASSWORD, 'MS4wLjABAAAADqkVdPXRX0PtK48xBSZK3iUM2SMnsdWONxyGJ1AR-uVok9Zu8bd9PYgUBAa5AA7l')
jwt = login.login_users(BASE_URL_DEV)
video = get_download_videos(jwt, BASE_URL_DEV)
x = len(video['downloadVideoDtoList'])
print(x)
for value in video['downloadVideoDtoList']:
    print(value)
