from config.config import *
from orders_actions.post_create_orders import create_orders
from user_actions.login_user import LoginUsers
import pandas as pd
import schedule

conn = TestData.DB_CONNECTION


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


def fetch_play_count(post_data):
    try:
        for key, value in post_data.items():
            if key == 'posts':
                for key_play, value_play in value.items():
                    if key_play == 'play_count':
                        return value_play
    except BaseExceptions:
        print('Error occurred:\n', traceback.format_exc())


def create_message(amount_before, amount_after, order_id):
    text_message = f'View order {order_id} was successfully completed. Amount before: {amount_before}, ' \
                   f'amount after: {amount_after}'
    return text_message


def send_msg(text):
    token = TestData.TG_TOKEN
    chat_id = TestData.TG_CHAT_ID
    url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + text
    results = requests.get(url_req)
    print(results.json())


def create_view_order():
    try:
        login = LoginUsers(username=TestData.USER_NAME, password=TestData.PASSWORD, sec_id=TestData.SEC_ID)
        jwt = login.login_users()
        create_orders(jwt)
    except BaseExceptions:
        print('Error occurred:\n', traceback.format_exc())


def fetch_order_id():
    result = pd.read_sql(TestData.SELECT_ACTIVE_ORDER_ID, conn)
    return result.iloc[0]['order_id']


def check_order_status(order_id):
    select_order_status_id = f"""
        select order_status_id
        from tm_user_orders
        where order_id = {order_id};
    """
    order_status_id = pd.read_sql(select_order_status_id, conn)
    return order_status_id.iloc[0]['order_status_id']


def job():
    order_id = fetch_order_id()
    order_status = check_order_status(fetch_order_id())
    if order_status == 2:
        play_count_after = fetch_play_count(fetch_post_data(TestData.AWEME_ID))
        message = create_message(play_count_before, play_count_after, order_id)
        send_msg(message)


play_count_before = fetch_play_count(fetch_post_data(TestData.AWEME_ID))
# create_view_order()

schedule.every(10).minutes.do(job)
#
while True:
    schedule.run_pending()
