import json
from os import path
from unittest.mock import MagicMock

from hades.core import TradeBotConf
from hades.core.exchange.binance_ex import BinanceUMExchangeClient


def test_balance():
    conf = TradeBotConf.load()
    exchange = BinanceUMExchangeClient(conf)
    with open(path.join(path.dirname(__file__), 'balance.json'), 'r') as f:
        exchange.client.balance = MagicMock(return_value=json.loads(f.read()))

    response = exchange.get_balance()
    assert len(response) > 0


def test_position():
    conf = TradeBotConf.load()
    exchange = BinanceUMExchangeClient(conf)
    with open(path.join(path.dirname(__file__), 'position.json'), 'r') as f:
        exchange.client.account = MagicMock(return_value={'positions': json.loads(f.read())})

    response = exchange.get_positions()
    assert len(response) > 0


def test_klind():
    conf = TradeBotConf.load()
    exchange = BinanceUMExchangeClient(conf)
    with open(path.join(path.dirname(__file__), 'kline.json'), 'r') as f:
        exchange.client.klines = MagicMock(return_value=json.loads(f.read()))

    response = exchange.get_candlesticks(symbol='BTCUSDT', bar='1m')
    assert len(response) == 100


def test_trades():
    conf = TradeBotConf.load()
    exchange = BinanceUMExchangeClient(conf)
    with open(path.join(path.dirname(__file__), 'trade.json'), 'r') as f:
        exchange.client.get_account_trades = MagicMock(return_value=json.loads(f.read()))
    with open(path.join(path.dirname(__file__), 'mark_price.json'), 'r') as f:
        exchange.client.mark_price = MagicMock(return_value=json.loads(f.read()))
    response = exchange.get_trades(symbol='BTCUSDT')
    assert len(response) == 2
