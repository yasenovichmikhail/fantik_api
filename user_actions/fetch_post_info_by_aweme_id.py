from orders_actions.check_order_fulfill import fetch_post_data
from pprint import pprint

post_info = fetch_post_data('7391167344136965381')
pprint(post_info)
