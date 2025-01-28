from config.config import *
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


def get_all_purchases_by_country(date_from, date_to, pattern, package_name, conn):
    select_all_purchases = f"""select tcp.currency_iso, SUM(price)
    from tm_consumable_purchases tcp
    where transaction_date between '{date_from}' AND '{date_to}'
    and tcp.user_id in (select user_id
                      from tm_logons
                      where install_referrer
                          like '%%{pattern}%%'
                        and package_name = '{package_name}')
    and payment_status_id = 2
    and tcp.consumable_product_id not in (62, 63, 64, 65, 66, 67, 68)
    group by tcp.currency_iso"""

    try:
        result = pd.read_sql(select_all_purchases, conn)
        return result
    except OperationalError as e:
        print(f"The error '{e}' occurred")


def get_all_revenue(date_from, date_to, pattern, package_name, conn):
    total = 0
    df_dict = get_all_purchases_by_country(date_from=date_from,
                                           date_to=date_to,
                                           pattern=pattern,
                                           package_name=package_name,
                                           conn=conn).to_dict(orient='list')
    currency_lst = df_dict['currency_iso']
    all_sum_lst = df_dict['sum']
    all_sum_dict = dict(zip(currency_lst, all_sum_lst))
    for key, value in all_sum_dict.items():
        if key != 'USD':
            price = get_exchange(usd_converter(key, value))
            print(f'{value} {key} = {price}$')
            total += price
        else:
            price = round(float(value), 2)
            total += price
            print(f'{price} USD = {price}$')
    total = round(total, 2)
    print(f'Total amount: {total}$')


get_all_revenue(date_from=GENERATE_DATE1,
                date_to=GENERATE_DATE2,
                pattern='E_C_P',
                package_name=FANTIK_PACKAGE_NAME_PROD,
                conn=DB_PROD_CONNECTION)
