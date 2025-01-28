from config.config import *
import pandas as pd
import requests
from bs4 import BeautifulSoup as bs


def usd_converter(convert_from, amount, convert_to='USD'):
    url = f"https://www.xe.com/currencyconverter/convert/?Amount={amount}&From={convert_from}&To={convert_to}"
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                             '(KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36'}
    page = requests.get(url=url, headers=headers)
    return bs(page.text, 'html.parser')


def get_exchange(data):
    currency_container = data.findAll('p', class_='sc-a3e7ffd7-1 bnLtQr')
    for price in currency_container:
        usd = price.text.split()[0]
        if len(usd) > 3:
            usd = usd.replace(',', '')
            return round(float(usd), 2)
        else:
            return round(float(usd), 2)


def get_all_app_purchases_by_country(date_from, date_to, app_id, conn):
    select_all_purchases = f"""select tu.country_iso,
        SUM(price) cnt
    from tm_consumable_purchases tcp
             join tm_consumable_products t on t.consumable_product_id = tcp.consumable_product_id
             join tm_users tu on tcp.user_id = tu.user_id
    where transaction_date between '{date_from}' AND '{date_to}'
        and t.app_settings_id = {app_id}
        and payment_status_id = 2
    group by tu.country_iso
    order by cnt desc"""

    try:
        result = pd.read_sql(select_all_purchases, conn)
        return result
    except OperationalError as e:
        print(f"The error '{e}' occurred")


def get_all_revenue(date_from, date_to, app_id, conn):
    total = 0
    df_dict = get_all_app_purchases_by_country(date_from=date_from,
                                               date_to=date_to,
                                               app_id=app_id,
                                               conn=conn).to_dict(orient='list')
    currency_lst = df_dict['country_iso']
    all_sum_lst = df_dict['cnt']
    all_sum_dict = dict(zip(currency_lst, all_sum_lst))
    for key, value in all_sum_dict.items():
        print(f"{key}: {value}$")
        price = float(value)
        total += price
    print(f'Total amount: {total}$')


get_all_revenue(date_from=GENERATE_DATE1,
                date_to=GENERATE_DATE2,
                app_id=FAMETOK_ID,
                conn=DB_PROD_CONNECTION)
