from dataclasses import dataclass
from config.config import *


@dataclass
class LoginUsers:
    username: str
    password: str
    sec_id: str

    def login_users(self, base_url):
        try:
            body = {"tiktokAccountUsername": self.username,
                    "rawPassword": self.password,
                    "secUserId": self.sec_id}

            headers = {'accept': 'application/json'}

            response = requests.post(f'{base_url}' + f'{USER_LOGIN_PATH}', headers=headers, json=body)
            if response.status_code == 200:
                print(f'User was successfully logged in', sep='\n')
                return response.json()['jwt']
            elif response.status_code == 403:
                print(f'Status code: {response.status_code}', f'Username/password mismatch', sep='\n')
            else:
                print(f'Something went wrong, status code: {response.status_code}')
        except BaseExceptions:
            print('Error occurred:\n', traceback.format_exc())


if __name__ == '__main__':
    login = LoginUsers(USER_NAME, PASSWORD, SEC_ID)
    print(login.login_users(base_url=BASE_URL_DEV))
