from orders_actions.post_create_orders import create_orders
from user_actions.login_user import LoginUsers
from orders_actions.fetch_all_user_data import fetch_posts_aweme_id, fetch_user_data
import random
from config.config import *


def fetch_random_user_post(username, amount_of_posts):
    all_posts = fetch_posts_aweme_id(fetch_user_data(username, amount_of_posts))
    return random.choice(all_posts)


def main(base_url, username, password, sec_id, amount):
    login = LoginUsers(username=username, password=password, sec_id=sec_id)
    jwt = login.login_users(base_url)
    for i in range(1, 5):                                                                                # types of orders
        for j in range(1):                                                                               # amount of orders
            if i != 4:
                create_orders(jwt_token=jwt,
                              action_type=i,
                              amount=amount,
                              aweme_id=fetch_random_user_post(username, 15),
                              base_url=base_url)
            elif i == 4:
                create_orders(jwt_token=jwt,
                              action_type=i,
                              amount=amount,
                              base_url=base_url)


if __name__ == '__main__':
    main(base_url=BASE_URL_DEV, username=USER_NAME, password=PASSWORD, sec_id=SEC_ID, amount=10)
