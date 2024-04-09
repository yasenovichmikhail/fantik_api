import requests
import json
from config.config import TestData
from pprint import *


class LoginUsers:

    def __init__(self, username, password, sec_id):
        self.username = username
        self.password = password
        self.sec_id = sec_id

    def login_users(self):
        body = {"tiktokAccountUsername": self.username,
                "rawPassword": self.password,
                "secUserId": self.sec_id}

        headers = {'accept': 'application/json'}

        response = requests.post(f'{TestData.BASE_URL}' + f'{TestData.USER_LOGIN_PATH}', headers=headers, json=body)
        return response.json()['jwt']


l = LoginUsers(TestData.USER_NAME, TestData.PASSWORD, TestData.SEC_ID)
