import requests
from config.config import *
from user_actions.login_user import LoginUsers
from orders_actions.create_multiple_different_types_orders import fetch_random_user_post
from orders_actions.fetch_different_type_of_links import fetch_types_of_links
from orders_actions.check_order_fulfill import fetch_post_data
from pprint import *


def post_download_videos(jwt_token, link, base_url):
    try:
        headers = {
            'accept': 'application/json',
            'Authorization1': jwt_token
        }

        body = {
            'postLink': link
        }

        response = requests.post(f'{base_url}' + f'{DOWNLOAD_VIDEOS_PATH}',
                                 headers=headers,
                                 json=body)
        if response.status_code == 200:
            print(f'Status code: {response.status_code}', sep='\n')
            return response.json()
        else:
            print(f'Something went wrong, status code: {response.status_code}')
    except BaseExceptions:
        print('Error occurred:\n', traceback.format_exc())


def main(username, password, sec_id, base_url, amount=10):
    login = LoginUsers(username=username,
                       password=password,
                       sec_id=sec_id)
    jwt = login.login_users(base_url)
    random_post = fetch_random_user_post(username=username,
                                         amount_of_posts=amount)
    links = fetch_types_of_links(post_data=fetch_post_data(random_post))
    for i in range(3):
        post_download_videos(jwt_token=jwt,
                             link=links[i],
                             base_url=base_url)


if __name__ == '__main__':
    main(username=USER_NAME, password=PASSWORD, sec_id=SEC_ID, base_url=BASE_URL_DEV)



