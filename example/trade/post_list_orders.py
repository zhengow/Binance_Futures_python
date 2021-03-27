from binance_f import RequestClient
from binance_f.constant.test import *
from binance_f.base.printobject import *
from binance_f.model.constant import *

request_client = RequestClient(api_key=g_api_key, secret_key=g_secret_key)
batchOrders = [
        {
            "symbol":"BNBUSDT",
            "side": OrderSide.BUY,
            "type": OrderType.LIMIT,
            "quantity": "1",
            "price": "100",
            "timeInForce": TimeInForce.GTC
        },
        {
            "symbol":"BNBUSDT",
            "side": OrderSide.SELL,
            "type": OrderType.LIMIT,
            "quantity": "1",
            "price": "500",
            "timeInForce": TimeInForce.GTC
        },
    ]
result = request_client.post_list_orders(batchOrders=batchOrders)

PrintList.print_object_list(result)
