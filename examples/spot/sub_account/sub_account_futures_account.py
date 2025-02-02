#!/usr/bin/env python

import logging
from binance.spot import Spot as Client
from binance.lib.utils import config_logging

config_logging(logging, logging.DEBUG)

api_key = ""
api_secret = ""

spot_client = Client(api_key, api_secret)
logging.info(
    spot_client.sub_account_futures_account(
        email="alice@test.com",
        futuresType=1,  # 1:USDT Margined Futures, 2:COIN Margined Futures
    )
)
