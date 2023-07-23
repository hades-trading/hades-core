import logging

from hades.core.config import TradeBotConf
from hades.core.messager import Messager
from hades.core.model import Order, Position, Tick, Bar, Balance, Trade
from hades.core.strategy import Strategy, Exchange, Subscriber, ExchangeEnum
from hades.core.exchange.binance import BinanceUMSubscriber
from hades.core.exchange.okx import OkxSubscriber
from hades.core.executor import TradeExecutor


logging.basicConfig(filename='log.txt',
                    format='%(asctime)s - %(levelname)s - %(name)s - %(funcName)s - %(message)s',
                    level=logging.INFO)

logging.getLogger('okx.websocket.WsClientProtocol').setLevel(logging.ERROR)

__all__ = ['TradeBotConf',
           'Messager',
           'Strategy',
           'Exchange',
           'Subscriber',
           'ExchangeEnum',
           'BinanceUMSubscriber',
           'OkxSubscriber',
           'TradeExecutor',
           'Order',
           'Position',
           'Tick',
           'Bar',
           'Trade',
           'Balance']

