import time

from config.config import *
from orders_actions.post_create_orders import create_orders
from user_actions.login_user import LoginUsers
import pandas as pd
import schedule
from multiprocessing import Process
import threading

conn = DB_PROD_CONNECTION
amount_before = 0
amount_after = 0
time_before = 0
time_after = 0
FLAG = True


def fetch_post_data(aweme_id):
    try:
        body = {"aweme_id": aweme_id}

        headers = {'content-type': 'application/json',
                   'X-RapidAPI-Key': 'fd80dfa220msha1c05eac4a74483p10c016jsn711bd34e755a',
                   'X-RapidAPI-Host': 'tiktok-unauthorized-api-scraper-no-watermark-analytics-feed.p.rapidapi.com'}

        response = requests.post(VIEWER_SEARCH_BY_AWEME_ID_URL, headers=headers, json=body)
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

        response = requests.post(VIEWER_SEARCH_BY_USERNAME_URL, headers=headers, json=body)
        return response.json()
    except BaseExceptions:
        print('Error occurred:\n', traceback.format_exc())


def fetch_action_count(post_data, type_info, fetch_action):
    try:
        for key, value in post_data.items():
            if key == type_info:
                for key_play, value_play in value.items():
                    if key_play == fetch_action:
                        return value_play
    except BaseExceptions:
        print('Error occurred:\n', traceback.format_exc())


def create_message(action_type, amount, metrics_before, metrics_after, order_id, time_before, time_after):
    difference = metrics_after - metrics_before
    diff = time_after - time_before
    diff = time.gmtime(diff)
    time_diff = time.strftime("%M min %S sec", diff)
    if action_type != 5:
        text_message = f'Your order {order_id} for {amount} {ACTION_TYPES_REF[action_type]} has been successfully ' \
                       f'completed. Amount before: {metrics_before}, amount after: {metrics_after}.' \
                       f'The difference is: {difference}. Finished in {time_diff}'
    else:
        text_message = f'Your order {order_id} for {amount}k {ACTION_TYPES_REF[action_type]} has been successfully ' \
                       f'completed. Amount before: {metrics_before}, amount after: {metrics_after}.' \
                       f'The difference is: {difference}. Finished in {time_diff}'
    return text_message


def send_msg(text):
    token = TG_TOKEN
    chat_id = TG_CHAT_ID
    url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + text
    results = requests.get(url_req)
    print(results.json())


def create_order(action_type, amount, duration, fetch_action, base_url, aweme_id=None):
    global amount_before
    global time_before
    try:
        login = LoginUsers(username=USER_NAME,
                           password=PASSWORD,
                           sec_id=SEC_ID)
        jwt = login.login_users(base_url)
        create_orders(jwt_token=jwt,
                      action_type=action_type,
                      amount=amount,
                      duration=duration,
                      base_url=base_url,
                      aweme_id=aweme_id)
        time_before = time.perf_counter()
        if action_type != 4:
            amount_before = fetch_action_count(post_data=fetch_post_data(aweme_id),
                                               fetch_action=fetch_action,
                                               type_info=POSTS_INFO)
            print(f"{ACTION_TYPES_REF[action_type]} before: {amount_before}")
        elif action_type == 4:
            amount_before = fetch_action_count(post_data=fetch_user_data(USER_NAME),
                                               type_info=USER_INFO, fetch_action=fetch_action)
            print(f"{ACTION_TYPES_REF[action_type]} before: {amount_before}")
    except BaseExceptions:
        print('Error occurred:\n', traceback.format_exc())


def fetch_order_id(action_type):
    select_active_order_id = f"""
    select order_id
    from tm_user_orders
    where user_id = {USER_ID}
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


def job(action_type_id, fetch_action, amount, aweme_id=None):
    global amount_after
    global time_after
    order_id = fetch_order_id(action_type_id)
    order_status = check_order_status(order_id=order_id)
    if order_status == 2:
        time_after = time.perf_counter()
        if action_type_id != 4:
            amount_after = fetch_action_count(post_data=fetch_post_data(aweme_id),
                                              type_info=POSTS_INFO,
                                              fetch_action=fetch_action)
            print(f"{ACTION_TYPES_REF[action_type_id]} after: {amount_after}")
        elif action_type_id == 4:
            amount_after = fetch_action_count(post_data=fetch_user_data(USER_NAME),
                                              type_info=USER_INFO,
                                              fetch_action=fetch_action)
            print(f"{ACTION_TYPES_REF[action_type_id]} after: {amount_after}")
        message = create_message(action_type=action_type_id,
                                 metrics_before=amount_before,
                                 metrics_after=amount_after,
                                 order_id=order_id,
                                 time_before=time_before,
                                 time_after=time_after,
                                 amount=amount)
        send_msg(message)
        global FLAG
        FLAG = False


def create_and_check_order(action_type, amount, duration, fetch_action, aweme_id=None, base_url=BASE_URL_DEV):
    create_order(action_type=action_type,
                 aweme_id=aweme_id,
                 amount=amount,
                 duration=duration,
                 fetch_action=fetch_action,
                 base_url=base_url)
    schedule.every(1).minutes.do(job, action_type_id=action_type,
                                 amount=amount,
                                 fetch_action=fetch_action,
                                 aweme_id=aweme_id)
    while FLAG:
        schedule.run_pending()


if __name__ == '__main__':
    processes = []
    for i in [1, 2, 3, 4, 5]:
        process = Process(target=create_and_check_order, args=(*FULFILL_ORDER_FORM[i], BASE_URL_PROD))
        process.start()
        processes.append(process)
        time.sleep(1)
    for proc in processes:
        proc.join()
