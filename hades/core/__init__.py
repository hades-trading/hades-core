import logging

from hades.core.model import Order, Position, Tick, Bar, Balance, Trade
from hades.core.strategy import Strategy, Exchange, Subscriber, ExchangeEnum
from hades.core.config import TradeBotConf
from hades.core.exchange import BinanceUMSubscriber, OkxSubscriber
from hades.core.executor import TradeExecutor
from hades.core.messager import Messenger, MessageFactory, MessageEnum

logging.basicConfig(filename='log.txt',
                    format='%(asctime)s - %(levelname)s - %(name)s - %(funcName)s - %(message)s',
                    level=logging.INFO)

logging.getLogger('okx.websocket.WsClientProtocol').setLevel(logging.ERROR)

__all__ = ['TradeBotConf',
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
           'Balance',
           'Messenger',
           'MessageEnum',
           'MessageFactory']
