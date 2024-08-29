import pandas as pd

from fetch_sec_id import fetch_sec_id, fetch_user_data
from config.config import *


def get_sec_id(username):
    sec_id = fetch_sec_id(fetch_user_data(username))
    return sec_id


def get_user_id(sec_id, conn):
    select_user_id = f"""Select
    user_id from tm_users
    where sec_user_id = '{sec_id}'
    and user_status_id = 1 
    """
    result = pd.read_sql(select_user_id, conn)
    return result.iloc[0]['user_id']


def get_user_status(user_id, conn):
    select_user_status = f"""Select
    user_status_id from tm_users
    where user_id = {user_id}
    and user_status_id = 1
    """
    result = pd.read_sql(select_user_status, conn)
    return result.iloc[0]['user_status_id']


def main(username, conn):
    sec_id = get_sec_id(username=username)
    user_id = get_user_id(sec_id=sec_id,
                          conn=conn)
    user_status_id = get_user_status(user_id=user_id,
                                     conn=conn)
    return user_status_id


print(main(username='jimmymacnaxer', conn=DB_PROD_CONNECTION))

# print(get_user_id(get_sec_id('jimmymacnaxer'), DB_PROD_CONNECTION))



