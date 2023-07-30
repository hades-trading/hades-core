from typing import List

from hades.core import Exchange, Position, Balance, Order, Trade, Bar


class BackTestingExchange(Exchange):
    def get_positions(self) -> List[Position]:
        pass

    def get_balance(self) -> Balance:
        pass

    def get_orders(self) -> List[Order]:
        pass

    def place_buy_order(self, symbol: str, size: float, price: float) -> Order:
        pass

    def place_sell_order(self, symbol: str, size: float, price: float) -> Order:
        pass

    def cancel_order(self, orderId: str, symbol: str) -> Order:
        pass

    def close_position(self, symbol: str):
        pass

    # get latest 100 bar
    def get_candlesticks(self, symbol: str, bar: str = '1m', limit: int = 100) -> List[Bar]:
        pass

    def get_trades(self, symbol: str) -> List[Trade]:
        pass
