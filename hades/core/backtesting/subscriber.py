from typing import List

from hades.core import Subscriber, Strategy, Exchange, Bar


class BackTestingExchange(Exchange):
    pass


class BackTestingSubscriber(Subscriber):
    def __init__(self, strategy: Strategy) -> None:
        super().__init__(strategy)

    def get_exchange(self) -> Exchange:
        return BackTestingExchange()

    def on_bar(self, bars: List[Bar]):
        super().on_bar(bars)
