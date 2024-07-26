
from config.config import *


def get_settings(base_url, package_name, device_type):
    try:
        headers = {'package_name': package_name,
                   'device_type_id': device_type}

        response = requests.get(f'{base_url}' + f'{GET_SETTINGS_PATH}', headers=headers)
        print(f'Status code: {response.status_code}')
        assert response.status_code == 200, f"Request is failed with status code: {response.status_code}"
        return pprint(response.json())
    except BaseExceptions:
        print('Error occurred:\n', traceback.format_exc())


def main(base_url, package_name, device_type):
    get_settings(base_url, package_name, device_type)


if __name__ == '__main__':
    main(BASE_URL_PROD, PACKAGE_NAME_PROD, DEVICE_TYPE)

