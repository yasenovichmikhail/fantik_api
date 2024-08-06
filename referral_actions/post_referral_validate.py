import requests
from config.config import *
from user_actions.login_user import LoginUsers
from pprint import *


def referral_validate(referral_type, promo_code, base_url):
    try:

        body = {
            "context": referral_type,
            "token": promo_code
        }

        response = requests.post(f'{base_url}' + f'{REFERRAL_VALIDATE_PATH}',
                                 json=body)
        if response.status_code == 200:
            print(f'Status code: {response.status_code}', sep='\n')
            return response.json()
        else:
            print(f'Something went wrong, status code: {response.status_code}')
            print('Error occurred:\n', traceback.format_exc())
    except BaseExceptions:
        print('Error occurred:\n', traceback.format_exc())


def main(referral_type, promo_code, base_url):
    result = referral_validate(referral_type=referral_type,
                               promo_code=promo_code,
                               base_url=base_url)
    pprint(result)


if __name__ == '__main__':
    main(referral_type=REFERRAL_TYPE,
         promo_code='0e10-26a4e79a-f3bc',
         base_url=BASE_URL_DEV)
