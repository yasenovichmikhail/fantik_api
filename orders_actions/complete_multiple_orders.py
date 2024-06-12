import pandas as pd

from orders_actions.post_orders_execution_complete import orders_execution_complete
from orders_actions.post_orders_execution_complete import complete_orders
from user_actions.login_user import LoginUsers
from config.config import *


def fetch_last_active_orders(user_id, amount):
    select_last_active_orders = f"""
    select order_id
    from tm_user_orders
    where user_id = {user_id}
    and order_status_id = 1
    order by order_id
    limit {amount};
    """
    df = pd.read_sql(select_last_active_orders, DB_DEV_CONNECTION)
    orders_list = df['order_id'].values.tolist()
    return orders_list


orders = fetch_last_active_orders(user_id=2328, amount=10)
login = LoginUsers(username=USER_NAME, password=PASSWORD, sec_id=SEC_ID)
jwt = login.login_users()
