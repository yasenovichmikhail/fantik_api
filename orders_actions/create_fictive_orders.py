import concurrent.futures
from config.config import *


def fetch_user_posts():
    try:
        body = {"username": "animalplanet",
                "amount_of_posts": 20}

        headers = {'content-type': 'application/json'}

        response = requests.post(TestData.VIEWER_SEARCH_BY_USERNAME_URL, headers=headers, json=body)
        return response
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

    response = requests.post(f'{TestData.BASE_URL}' + f'{TestData.CREATE_FICTIVE_ORDERS_PATH}', json=body)
    return print(f'Status code: {response.status_code}')


t1 = time.perf_counter()
data = fetch_user_posts().json()
# pprint(data)

aweme_list = []

fetch_posts_aweme_id(data)

# with concurrent.futures.ThreadPoolExecutor() as executor:
#     executor.map(create_fictive_order, aweme_list)

print(len(aweme_list))
t2 = time.perf_counter()
print(f'Finished in {t2 - t1} second(s)')
