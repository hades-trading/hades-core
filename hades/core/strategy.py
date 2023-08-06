import asyncio
import logging
from enum import Enum
from typing import List, Optional

from hades.core import Balance, Tick, Bar, Order, Position, Trade


class ExchangeEnum(Enum):
    BackTesting = 0
    OKX = 1
    Binance = 2


class Exchange:
    def get_positions(self) -> List[Position]:
        """
        Returns: positions
        """
        pass

    def get_balance(self) -> List[Balance]:
        """
        Returns: account balance
        """
        pass

    def get_orders(self) -> List[Order]:
        """

        Returns:  orders

        """
        pass

    def place_buy_order(self, symbol: str, size: float, price: float) -> Order:
        """
        Args:
            symbol: symbol
            size: size
            price: entry price
        Returns: Order
        """
        pass

    def place_sell_order(self, symbol: str, size: float, price: float) -> Order:
        """
        Args:
               symbol: symbol
            size: size
            price: entry price
        Returns: Order
        """
        pass

    def cancel_order(self, order_id: str, symbol: str) -> Order:
        """
        Args:
            order_id: order_id
            symbol: symbol
        Returns: Order
        """
        pass

    def close_position(self, symbol: str):
        """
        Args:
            symbol: symbol
        Returns: close all positions
        """
        pass

    # get latest 100 bar
    def get_candlesticks(self, symbol: str, bar: str = '1m', limit: int = 100) -> List[Bar]:
        """
        Args:
            symbol: symbol
            bar: bar type
            limit: limit
        Returns: a collection of bars
        """
        pass

    def get_trades(self, symbol: str) -> List[Trade]:
        """
        Args:
            symbol: symbol
        Returns: latest trades
        """
        pass


class Strategy:
    def __init__(self, strategy_id: str, symbols: List[str], instrument_type: str, klines: List[str]) -> None:
        self.strategy_id = strategy_id
        self.symbols = symbols
        self.instrument_type = instrument_type
        self.klines = klines
        self.balance: List[Balance] = []
        self.exchange: Optional[Exchange] = None
        # local state
        self.positions: List[Position] = []
        self.ticks: List[Tick] = []
        self.bars = {}

    def on_init_exchange(self, exchange: Exchange):
        self.exchange = exchange

    def on_tick(self, ticks: List[Tick]):
        self.ticks.extend(ticks)
        if len(self.ticks) % 100 == 0:
            logging.info(f'ticks to {len(self.ticks)}')
        if len(self.ticks) > 10000:
            self.ticks = self.ticks[-5000:]

    def on_bar(self, bars: List[Bar]) -> None:
        """
        Args:
            bars: a collection of bars
        """
        pass

    def on_order_status(self, orders: List[Order]) -> None:
        """
        Args:
            orders: latest orders
        """
        pass

    def on_balance_status(self, balance: List[Balance]):
        self.balance.clear()
        self.balance.extend(balance)

    def on_position_status(self, positions: List[Position]):
        self.positions.clear()
        self.positions.extend(positions)


class Subscriber:
    def __init__(self, strategy: Strategy) -> None:
        self.strategy = strategy
        self.exchange: Exchange = self.get_exchange()
        self.strategy.on_init_exchange(self.exchange)

    def on_tick(self, ticks: List[Tick]):
        self.strategy.on_tick(ticks)

    def on_bar(self, bars: List[Bar]):
        self.strategy.on_bar(bars)

    def on_order_status(self, orders: List[Order]):
        self.strategy.on_order_status(orders)

    def on_balance_status(self, balance: List[Balance]):
        self.strategy.on_balance_status(balance)

    def on_position_status(self, positions: List[Position]):
        self.strategy.on_position_status(positions)

    def run(self) -> asyncio.Task:
        """
        Returns: task
        """
        pass

    def stop(self) -> None:
        """
        Returns:
        """
        pass

    def get_exchange(self) -> Exchange:
        """
        Returns:
        """
        pass
