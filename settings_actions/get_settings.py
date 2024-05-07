
from config.config import *


def get_settings():
    try:
        headers = {'package_name': TestData.PACKAGE_NAME,
                   'device_type_id': TestData.DEVICE_TYPE}

        response = requests.get(f'{TestData.BASE_URL}' + f'{TestData.GET_SETTINGS_PATH}', headers=headers)
        print(f'Status code: {response.status_code}')
        assert response.status_code == 200, f"Request is failed with status code: {response.status_code}"
        return response
    except BaseExceptions:
        print('Error occurred:\n', traceback.format_exc())


data = get_settings().json()
pprint(data)
