from orders_actions.check_order_fulfill import fetch_user_data
from config.config import *


def fetch_sec_id(user_data):
    try:
        for key, value in user_data.items():
            if key == 'user':
                for key_info, value_info in value.items():
                    if key_info == 'sid':
                        return value_info
    except BaseExceptions:
        print('Error occurred:\n', traceback.format_exc())


def main(user_name):
    user_info = fetch_user_data(user_name)
    sec_id = fetch_sec_id(user_info)
    print(sec_id)


if __name__ == '__main__':
    # main('VlogsFromAmer1ca')
    user_info = fetch_user_data(USER_NAME)
    pprint(user_info)
