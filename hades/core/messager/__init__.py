from hades.core import TradeBotConf
from hades.core.messager.base import MessageEnum, Messenger
from hades.core.messager.dingding import DingDingMessenger
from hades.core.messager.telegram import TelegramMessenger


class MessageFactory:
    @staticmethod
    def build_messenger(enum: MessageEnum, conf: TradeBotConf) -> Messenger:
        if enum == MessageEnum.DingDing:
            return DingDingMessenger(conf)
        elif enum == MessageEnum.Telegram:
            return TelegramMessenger(conf)
        raise ValueError('current messenger does not support')


__all__ = ['MessageFactory', 'MessageEnum', 'Messenger']
