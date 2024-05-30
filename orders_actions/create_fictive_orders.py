import concurrent.futures
from config.config import *


def fetch_all_user_data(username, amount_of_posts):
    try:
        body = {"username": username,
                "amount_of_posts": amount_of_posts}

        headers = {'content-type': 'application/json',
                   'X-RapidAPI-Key': 'fd80dfa220msha1c05eac4a74483p10c016jsn711bd34e755a',
                   'X-RapidAPI-Host': 'tiktok-unauthorized-api-scraper-no-watermark-analytics-feed.p.rapidapi.com'
                   }

        response = requests.post(VIEWER_SEARCH_BY_USERNAME_FULL_URL, headers=headers, json=body)
        return response.json()
    except BaseExceptions:
        print('Error occurred:\n', traceback.format_exc())


def fetch_posts_aweme_id(data):
    for key, value in data.items():
        if key == 'posts':
            for content in value:
                for aweme, aweme_value in content.items():
                    if aweme == 'aweme_id':
                        aweme_list.append(aweme_value)


def create_fictive_order(aweme):
    body = {"actionTypeId": 1,
            "awemeId": aweme,
            "shortLink": "",
            "actionsAmount": 10,
            "orderDurationHours": 12,
            "orderName": "fictive",
            "rewardId": None}

    response = requests.post(f'{BASE_URL}' + f'{CREATE_FICTIVE_ORDERS_PATH}', json=body)
    return print(f'Status code: {response.status_code}')


# t1 = time.perf_counter()
data = fetch_all_user_data(USER_NAME, 20)
pprint(data)

aweme_list = []

# fetch_posts_aweme_id(data)

# with concurrent.futures.ThreadPoolExecutor() as executor:
#     executor.map(create_fictive_order, aweme_list)

# print(len(aweme_list))
# t2 = time.perf_counter()
# print(f'Finished in {t2 - t1} second(s)')
