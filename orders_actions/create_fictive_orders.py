import concurrent.futures
import requests
import time
import json
from config.config import TestData
from pprint import *


def fetch_user_posts():
    body = {"username": "animalplanet",
            "amount_of_posts": 20}

    headers = {'content-type': 'application/json',
               'X-RapidAPI-Key': 'fd80dfa220msha1c05eac4a74483p10c016jsn711bd34e755a',
               'X-RapidAPI-Host': 'tiktok-unauthorized-api-scraper-no-watermark-analytics-feed.p.rapidapi.com'}

    response = requests.post(TestData.VIEWER_SEARCH_URL, headers=headers, json=body)
    return response


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

    response = requests.post(f'{TestData.BASE_URL}' + f'{TestData.CREATE_FICTIVE_ORDERS_PATH}', json=body)
    return print(f'Status code: {response.status_code}')


t1 = time.perf_counter()
data = fetch_user_posts().json()

aweme_list = []

fetch_posts_aweme_id(data)

# with concurrent.futures.ThreadPoolExecutor() as executor:
#     executor.map(create_fictive_order, aweme_list)

print(aweme_list)
t2 = time.perf_counter()
print(f'Finished in {t2 - t1} second(s)')



