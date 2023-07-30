import requests

from hades.core import TradeBotConf
from hades.core.messager.base import Messenger


class DingDingMessenger(Messenger):
    def __init__(self, conf: TradeBotConf) -> None:
        super().__init__(conf)

        self.prefix = conf.prefix
        self.url = f'https://oapi.dingtalk.com/robot/send?access_token={conf.token}'
        self.session = requests.session()
        self.session.headers.update({
            'Content-Type': 'application/json',
        })

    def _send_message(self, text) -> bool:
        data = {
            'msgtype': 'text',
            'text': {
                'content': f'{self.prefix} {text}'
            }
        }
        response = self.session.post(self.url, json=data)
        return 'errmsg' in response.json() and response.json()['errmsg'] == 'ok'
