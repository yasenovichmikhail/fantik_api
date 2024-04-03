
import requests
from sqlite3 import OperationalError
import pandas as pd
import schedule
from config.config import TestData

conn = TestData.DB_CONNECTION

active_orders_query = """select tuo.order_id
from tm_order_execution_progresses toep
         join tm_user_orders tuo on tuo.order_id = toep.order_id
where tuo.order_status_id = 1
  and tuo.is_fictive = 'false'
  and tuo.action_type_id != 5
order by tuo.start_date asc"""


def execute_query(query, connect):
    try:
        result = len(pd.read_sql(query, connect))
        return result
    except OperationalError as e:
        print(f"The error '{e}' occurred")


def create_message(amount):
    text_message = f'There are {amount} active orders at the moment'
    return text_message


def send_msg(text):
    token = "6798940758:AAFGjfkYlUhRUxP1ughIIloXf6NjwtYerPc"
    chat_id = "709543761"
    url_req = "https://api.telegram.org/bot" + token + "/sendMessage" + "?chat_id=" + chat_id + "&text=" + text
    results = requests.get(url_req)
    print(results.json())


def job():
    orders = execute_query(active_orders_query, conn)
    if orders < 700:
        message = create_message(orders)
        send_msg(message)


schedule.every(5).seconds.do(job)
# schedule.every(5).to(10).days.do(job)
# schedule.every().hour.do(job, message='things')
# schedule.every().day.at("10:30").do(job)

while True:
    schedule.run_pending()
