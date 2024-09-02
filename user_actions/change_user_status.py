import pandas as pd
from sqlalchemy import text
from fetch_sec_id import fetch_sec_id, fetch_user_data
from config.config import *


def get_sec_id(username):
    sec_id = fetch_sec_id(fetch_user_data(username))
    return sec_id


def delete_user(sec_id, conn):
    change_user_status = f"""Update
        tm_users set user_status_id = 2
        where sec_user_id = '{sec_id}'
        and user_status_id = 1"""
    try:
        with conn.connect() as conn:
            conn.execute(text(change_user_status))
            conn.commit()
    except OperationalError as e:
        print(f"The error '{e}' occurred")


def main(username, conn):
    sec_id = get_sec_id(username=username)
    delete_user(sec_id=sec_id, conn=conn)
    print(f"User {username} has been deleted")


main(username='pes', conn=DB_DEV_CONNECTION)



