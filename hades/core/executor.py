from hades.core import Strategy, BinanceUMSubscriber, OkxSubscriber, Subscriber, ExchangeEnum
from hades.core.backtesting import BackTestingSubscriber


class TradeExecutor:
    def __init__(self, strategy: Strategy, exchange: ExchangeEnum = ExchangeEnum.Binance) -> None:
        self.strategy = strategy
        self.exchange = exchange
        self.subscriber = self.__get_subscriber(self.exchange)

    async def execute(self):
        await self.subscriber.run()

    def __get_subscriber(self, exchange: ExchangeEnum) -> Subscriber:
        if exchange == ExchangeEnum.Binance:
            return BinanceUMSubscriber(self.strategy)
        elif exchange == ExchangeEnum.OKX:
            return OkxSubscriber(self.strategy)
        elif exchange == ExchangeEnum.BackTesting:
            return BackTestingSubscriber(self.strategy)
        raise ValueError('current exchange does not support')

    def stop(self):
        self.subscriber.stop()
