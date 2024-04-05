
import requests
from sqlite3 import OperationalError
import pandas as pd
import schedule
from config.config import TestData
from sqlalchemy import text

conn = TestData.DB_DEV_CONNECTION

active_orders_query = """select tuo.order_id
from tm_order_execution_progresses toep
         join tm_user_orders tuo on tuo.order_id = toep.order_id
where tuo.order_status_id = 1
  and tuo.is_fictive = 'false'
  and tuo.action_type_id != 5
order by tuo.start_date asc"""

increase_order_price = """update tm_order_prices
set create_price = 3
where action_type_id = 1
"""

decrease_order_price = """update tm_order_prices
set create_price = 2
where action_type_id = 1
"""

get_current_price = """select create_price
from tm_order_prices
where action_type_id = 1
"""


def get_active_orders(query, connect):
    try:
        result = len(pd.read_sql(query, connect))
        return result
    except OperationalError as e:
        print(f"The error '{e}' occurred")


def change_order_price(query, connect):
    try:
        with connect.connect() as connection:
            connection.execute(text(query))
            connection.commit()
            print("Price has been changed")
    except OperationalError as e:
        print(f"The error '{e}' occurred")


def create_message(amount):
    text_message = f'There are {amount} active orders at the moment'
    return text_message


def send_msg(message):
    token = TestData.TG_TOKEN
    chat_id = TestData.TG_CHAT_ID
    url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + message
    results = requests.get(url_req)
    print(results.json())


def get_current_order_price(query, connect):
    try:
        result = pd.read_sql(query, connect)
        return result.iloc[0]['create_price']
    except OperationalError as e:
        print(f"The error '{e}' occurred")


def job():
    orders = get_active_orders(active_orders_query, conn)
    if orders > 100:
        message = create_message(orders)
        send_msg(message)


current_price = get_current_order_price(get_current_price, conn)
print(current_price)
# r = get_active_orders(active_orders_query, conn)
# schedule.every(5).minutes.do(job)
# schedule.every(5).to(10).days.do(job)
# schedule.every().hour.do(job, message='things')
# schedule.every().day.at("10:30").do(job)

# while True:
#     schedule.run_pending()
