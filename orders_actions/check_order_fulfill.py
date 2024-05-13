from config.config import *
from orders_actions.post_create_orders import create_orders
from user_actions.login_user import LoginUsers
import pandas as pd
import schedule

conn = TestData.DB_CONNECTION
AMOUNT_BEFORE = 0
AMOUNT_AFTER = 0
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


def fetch_action_count(post_data, fetch_action):
    try:
        for key, value in post_data.items():
            if key == 'posts':
                for key_play, value_play in value.items():
                    if key_play == fetch_action:
                        return value_play
    except BaseExceptions:
        print('Error occurred:\n', traceback.format_exc())


def create_message(amount_before, amount_after, order_id):
    differance = amount_after - amount_before
    text_message = f'Your order {order_id} was successfully completed. Amount before: {amount_before}, ' \
                   f'amount after: {amount_after}. The difference was: {differance}'
    return text_message


def send_msg(text):
    token = TestData.TG_TOKEN
    chat_id = TestData.TG_CHAT_ID
    url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + text
    results = requests.get(url_req)
    print(results.json())


def create_order(action_type, aweme_id, amount, fetch_action):
    try:
        login = LoginUsers(username=TestData.USER_NAME, password=TestData.PASSWORD, sec_id=TestData.SEC_ID)
        jwt = login.login_users()
        create_orders(jwt, action_type, aweme_id, amount)
        global AMOUNT_BEFORE
        AMOUNT_BEFORE = fetch_action_count(post_data=fetch_post_data(aweme_id), fetch_action=fetch_action)
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


def job(action_type_id, aweme_id, fetch_action):
    order_id = fetch_order_id(action_type_id)
    order_status = check_order_status(fetch_order_id(action_type_id))
    if order_status == 2:
        global AMOUNT_AFTER
        AMOUNT_AFTER = fetch_action_count(post_data=fetch_post_data(aweme_id),
                                          fetch_action=fetch_action)
        message = create_message(AMOUNT_BEFORE, AMOUNT_AFTER, order_id)
        send_msg(message)
        global FLAG
        FLAG = False


def create_and_check_order(action_type, aweme_id, amount, fetch_action):
    create_order(action_type, aweme_id, amount, fetch_action)
    schedule.every(10).minutes.do(job, action_type, aweme_id, fetch_action)
    while FLAG:
        schedule.run_pending()


create_and_check_order(action_type=TestData.ACTION_TYPE_ID, aweme_id=TestData.AWEME_ID, amount=TestData.ORDER_AMOUNT,
                       fetch_action=TestData.ACTION_TYPE_VIEWS)
