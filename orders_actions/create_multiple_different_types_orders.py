from orders_actions.post_create_orders import create_orders
from user_actions.login_user import LoginUsers
from orders_actions.fetch_all_user_data import fetch_posts_aweme_id, fetch_user_data
import random
from config.config import *


def fetch_random_posts(username, amount_of_posts):
    all_posts = fetch_posts_aweme_id(fetch_user_data(username, amount_of_posts))
    return random.choice(all_posts)


login = LoginUsers(username=USER_NAME, password=PASSWORD, sec_id=SEC_ID)
jwt = login.login_users()
for i in range(1, 5):                                                                                # types of orders
    for j in range(1):                                                                               # amount of orders
        if i != 4:
            create_orders(jwt_token=jwt,
                          action_type=i,
                          amount=20,
                          aweme_id=fetch_random_posts(USER_NAME, 15))
        elif i == 4:
            create_orders(jwt_token=jwt, action_type=i, amount=10)
