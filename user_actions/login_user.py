import requests
import json
from config.config import TestData
from pprint import *
from dataclasses import dataclass


@dataclass
class LoginUsers:
    username: str
    password: str
    sec_id: str

    def login_users(self):
        body = {"tiktokAccountUsername": self.username,
                "rawPassword": self.password,
                "secUserId": self.sec_id}

        headers = {'accept': 'application/json'}

        response = requests.post(f'{TestData.BASE_URL}' + f'{TestData.USER_LOGIN_PATH}', headers=headers, json=body)
        if response.status_code == 200:
            print(f'Status code: {response.status_code}', f'User was successfully logged in', sep='\n')
            return response.json()['jwt']
        elif response.status_code == 403:
            print(f'Status code: {response.status_code}', f'Username/password mismatch', sep='\n')
        else:
            print(f'Something went wrong, status code: {response.status_code}')


if __name__ == '__main__':
    login = LoginUsers(TestData.USER_NAME, TestData.PASSWORD, TestData.SEC_ID)
    print(login.login_users())
