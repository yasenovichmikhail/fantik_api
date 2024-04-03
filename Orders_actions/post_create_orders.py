import requests
from Config.config import TestData
import json
from pprint import *


def get_jwt_token(response):
    for key, value in response.items():
        return str(value)


def login_users():
    body = {
        "tiktokAccountUsername": TestData.USER_NAME,
        "rawPassword": TestData.PASSWORD,
        "secUserId": TestData.SEC_ID
    }

    headers = {'accept': 'application/json'}

    response = requests.post(f'{TestData.BASE_URL}' + f'{TestData.USER_LOGIN}', headers=headers, json=body).json()
    return get_jwt_token(response)


def create_orders(jwt_token):

    headers = {
        'accept': 'application/json',
        'Authorization1': jwt_token
    }

    body = {
        "actionTypeId": 1,
        "awemeId": "7211120373851540742",
        "shortLink": "",
        "actionsAmount": 100,
        "orderDurationHours": 12,
        "orderName": "test",
        "rewardId": None
    }

    response = requests.post(f'{TestData.BASE_URL}' + f'{TestData.ORDERS_CREATE}', headers=headers, json=body)
    return print(f'Status code: {response.status_code}')


jwt = login_users()

create_orders(jwt)