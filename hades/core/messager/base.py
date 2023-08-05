import logging
from datetime import datetime
from enum import Enum

from hades.core import TradeBotConf


class Messenger:
    def __init__(self, conf: TradeBotConf) -> None:
        self.start, self.end = conf.period.split('-')
        self.last_notify = None

    def _send_message(self, text: str) -> bool:
        """
        Args:
            text: text message
        Returns:
        """
        pass

    def notify(self, text: str) -> bool:
        now = datetime.utcnow()
        if int(self.start) <= now.hour < int(self.end):
            return self._send_message(text)
        else:
            logging.info(f'message = {text} not sent')

    def notify_with_interval(self, text, minute: int = 5) -> bool:
        now = datetime.utcnow()
        if not self.last_notify or (now - self.last_notify).seconds >= minute * 60:
            self.last_notify = now
            return self.notify(text)


class MessageEnum(Enum):
    DingDing = 1
    Telegram = 2
