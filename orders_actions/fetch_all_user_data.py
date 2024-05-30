from config.config import *
from orders_actions.post_create_orders import create_orders
from user_actions.login_user import LoginUsers
import pandas as pd
import schedule


conn = TestData.DB_PROD_CONNECTION
amount_before = 0
amount_after = 0
telegram_message = ''
FLAG = True


def fetch_post_data(aweme_id):
    try:
        body = {"aweme_id": aweme_id}

        headers = {'content-type': 'application/json',
                  'X-RapidAPI-Key': 'fd80dfa220msha1c05eac4a74483p10c016jsn711bd34e755a',
                  'X-RapidAPI-Host': 'tiktok-unauthorized-api-scraper-no-watermark-analytics-feed.p.rapidapi.com'}

        response = requests.post(TestData.VIEWER_SEARCH_BY_AWEME_ID_URL, headers=headers, json=body)
        return response.json()

    except BaseExceptions:
        print('Error occurred:\n', traceback.format_exc())


def fetch_user_data(username, amount_of_posts=0):
    try:
        body = {"username": username,
                "amount_of_posts": amount_of_posts}

        headers = {'content-type': 'application/json',
                   'X-RapidAPI-Key': 'fd80dfa220msha1c05eac4a74483p10c016jsn711bd34e755a',
                   'X-RapidAPI-Host': 'tiktok-unauthorized-api-scraper-no-watermark-analytics-feed.p.rapidapi.com'
                   }

        response = requests.post(TestData.VIEWER_SEARCH_BY_USERNAME_URL, headers=headers, json=body)
        return response.json()
    except BaseExceptions:
        print('Error occurred:\n', traceback.format_exc())


def fetch_posts_aweme_id(data):
    aweme_list = []
    for key, value in data.items():
        if key == 'posts':
            for content in value:
                for aweme, aweme_value in content.items():
                    if aweme == 'aweme_id':
                        aweme_list.append(aweme_value)
    return aweme_list


def fetch_action_count(post_data, type_info, fetch_action):
    try:
        for key, value in post_data.items():
            if key == type_info:
                for key_play, value_play in value.items():
                    if key_play == fetch_action:
                        return value_play
    except BaseExceptions:
        print('Error occurred:\n', traceback.format_exc())


def create_message(action_type, before, after, order_id):
    difference = after - before
    text_message = f'Your order {order_id} for {TestData.ACTION_TYPES_REF[action_type]} has been successfully ' \
                   f'completed. Amount before: {before}, amount after: {after}. The difference was: {difference}'
    return text_message


def send_msg(text):
    token = TestData.TG_TOKEN
    chat_id = TestData.TG_CHAT_ID
    url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + text
    results = requests.get(url_req)
    print(results.json())


def create_order(action_type,  amount, fetch_action, aweme_id=None):
    global amount_before
    try:
        login = LoginUsers(username=TestData.USER_NAME, password=TestData.PASSWORD, sec_id=TestData.SEC_ID)
        jwt = login.login_users()
        create_orders(jwt_token=jwt, action_type=action_type, amount=amount, aweme_id=aweme_id)
        if action_type != 4:
            amount_before = fetch_action_count(post_data=fetch_post_data(aweme_id), fetch_action=fetch_action,
                                               type_info=TestData.POSTS_INFO)
            print(f"{TestData.ACTION_TYPES_REF[action_type]} before: {amount_before}")
        elif action_type == 4:
            amount_before = fetch_action_count(post_data=fetch_user_data(TestData.USER_NAME),
                                               type_info=TestData.USER_INFO, fetch_action=fetch_action)
            print(f"{TestData.ACTION_TYPES_REF[action_type]} before: {amount_before}")
    except BaseExceptions:
        print('Error occurred:\n', traceback.format_exc())


def fetch_order_id(action_type):
    select_active_order_id = f"""
    select order_id
    from tm_user_orders
    where user_id = {TestData.USER_ID}
    and action_type_id = {action_type}
    order by order_id desc;
    """
    result = pd.read_sql(select_active_order_id, conn)
    return result.iloc[0]['order_id']


def check_order_status(order_id):
    select_order_status_id = f"""
        select order_status_id
        from tm_user_orders
        where order_id = {order_id};
    """
    order_status_id = pd.read_sql(select_order_status_id, conn)
    return order_status_id.iloc[0]['order_status_id']


def check_current_status(action_type_id):
    order_status = check_order_status(order_id=fetch_order_id(action_type_id))
    return order_status


def fetch_order_execution(action_type, fetch_action, aweme_id=None):
    if check_current_status(action_type) == 2:
        if action_type != 4:
            global amount_after
            global FLAG
            amount_after = fetch_action_count(post_data=fetch_post_data(aweme_id),
                                              type_info=TestData.POSTS_INFO,
                                              fetch_action=fetch_action)
            FLAG = False
            print(f"{TestData.ACTION_TYPES_REF[action_type]} after: {amount_after}")
            return amount_after
        elif action_type == 4:
            amount_after = fetch_action_count(post_data=fetch_user_data(TestData.USER_NAME),
                                              type_info=TestData.USER_INFO,
                                              fetch_action=fetch_action)
            print(f"{TestData.ACTION_TYPES_REF[action_type]} after: {amount_after}")
            FLAG = False
            return amount_after


def create_and_check_order(action_type, amount, fetch_action, aweme_id=None):
    create_order(action_type=action_type, aweme_id=aweme_id, amount=amount, fetch_action=fetch_action)
    schedule.every(1).minutes.do(fetch_order_execution, action_type=action_type, fetch_action=fetch_action,
                                 aweme_id=aweme_id)
    global telegram_message
    telegram_message = create_message(action_type=1,
                                      before=amount_before,
                                      after=amount_after,
                                      order_id=35)
    while FLAG:
        schedule.run_pending()

# send_msg(message)


if __name__ == '__main__':
    print(telegram_message)
    # all_aweme = fetch_posts_aweme_id(fetch_user_data(TestData.USER_NAME, 20))
    # z = fetch_random_aweme_id(x)
    # print(*z)
    # for i in range(1, 6):
    #     create_and_check_order(*TestData.FULFILL_ORDER_FORM[i])


