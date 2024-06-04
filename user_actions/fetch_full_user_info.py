from config.config import *
from orders_actions.check_order_fulfill import fetch_post_data


def fetch_full_user_data(username, amount_of_posts=0):
    try:
        body = {"username": username,
                "amount_of_posts": amount_of_posts}

        headers = {'content-type': 'application/json',
                   'X-RapidAPI-Key': 'fd80dfa220msha1c05eac4a74483p10c016jsn711bd34e755a',
                   'X-RapidAPI-Host': 'tiktok-unauthorized-api-scraper-no-watermark-analytics-feed.p.rapidapi.com'
                   }

        response = requests.post(VIEWER_SEARCH_BY_USERNAME_FULL_URL, headers=headers, json=body)
        return pprint(response.json())
    except BaseExceptions:
        print('Error occurred:\n', traceback.format_exc())


fetch_full_user_data(USER_NAME, amount_of_posts=5)
