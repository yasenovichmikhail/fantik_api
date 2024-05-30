from dataclasses import dataclass
from config.config import *


@dataclass()
class UsersAuth:
    user_id: int
    username: str

    def user_auth(self):
        try:
            body = {"userId": self.user_id,
                    "username": self.username}

            headers = {'accept': 'application/json'}

            response = requests.post(f'{BASE_URL}' + f'{POST_USERS_AUTH_PATH}', headers=headers,
                                     json=body)
            if response.status_code == 200:
                print(f'Status code: {response.status_code}', f'Jwt was successfully updated', sep='\n')
                return response.json()['jwt']
            elif response.status_code == 403:
                print(f'Status code: {response.status_code}', f'Forbidden', sep='\n')
            else:
                print(f'Something went wrong, status code: {response.status_code}')
        except BaseExceptions:
            print('Error occurred:\n', traceback.format_exc())


user = UsersAuth(USER_ID, USER_NAME)
print(user.user_auth())
