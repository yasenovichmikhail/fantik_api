import requests
from config.config import TestData
from pprint import *


def send_request():
    headers = {'package_name': TestData.PACKAGE_NAME,
               'device_type_id': TestData.DEVICE_TYPE}

    response = requests.get(f'{TestData.BASE_URL}' + f'{TestData.GET_SETTINGS}', headers=headers)
    print(f'Status code: {response.status_code}')
    assert response.status_code == 200, f"Request is failed with status code: {response.status_code}"
    return response


data = send_request().json()
pprint(data)