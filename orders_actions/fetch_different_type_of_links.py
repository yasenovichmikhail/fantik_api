from orders_actions.check_order_fulfill import fetch_post_data
from pprint import pprint
from config.config import *

post_info = fetch_post_data('7150561058204224774')
types_of_links = ['share_link', 'short_link', 'web_link']


def fetch_types_of_links(post_data):
    links = []
    try:
        for key, value in post_data.items():
            if key == 'posts':
                for key_action, value_action in value.items():
                    if key_action in types_of_links:
                        links.append(value_action)
        return links
    except BaseExceptions:
        print('Error occurred:\n', traceback.format_exc())


def main(post_data):
    fetch_types_of_links(post_info)


if __name__ == '__main__':
    pprint(main(post_data=post_info))
