import telegram

from hades.core import TradeBotConf
from hades.core.messager.base import Messenger


class TelegramMessenger(Messenger):
    def __init__(self, conf: TradeBotConf) -> None:
        super().__init__(conf)
        self.bot = telegram.Bot(conf.token)

    async def _send_message(self, text) -> bool:
        await self.bot.send_message(text)
        return True
