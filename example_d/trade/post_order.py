from binance_d import RequestClient
from binance_d.constant.test import *
from binance_d.base.printobject import *
from binance_d.model.constant import *

request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
# print(request_client.change_position_mode(dualSidePosition=True))
result = request_client.post_order(symbol="BTCUSD_200925", side=OrderSide.SELL, ordertype=OrderType.LIMIT, price=8001.1, quantity=10, positionSide="LONG", timeInForce=TimeInForce.GTC)

PrintBasic.print_obj(result)
