import os
from configparser import ConfigParser
from os import path

BINANCE_API_KEY = 'BINANCE_API_KEY'
BINANCE_SECRET_KEY = 'BINANCE_SECRET_KEY'

NOTIFICATION_TOKEN = 'NOTIFICATION_TOKEN'
NOTIFICATION_PREFIX = 'NOTIFICATION_PREFIX'
NOTIFICATION_PERIOD = 'NOTIFICATION_PERIOD'


class TradeBotConf:
    def __init__(self, conf: ConfigParser = None) -> None:
        if not conf:
            self.binance = {'apiKey': os.environ.get(BINANCE_API_KEY), 'secretKey': os.environ.get(BINANCE_SECRET_KEY)}
            self.token = os.environ.get(NOTIFICATION_TOKEN)
            self.prefix = os.environ.get(NOTIFICATION_PREFIX)
            self.period = os.environ.get(NOTIFICATION_PERIOD)
        else:
            if conf.has_section('okx'):
                self.okx = {
                    'apiKey': conf['okx']['apiKey'],
                    'secretKey': conf['okx']['secretKey'],
                    'passphrase': conf['okx']['passphrase'],
                    'ws_private': conf['okx']['ws_private'],
                    'ws_public': conf['okx']['ws_public'],
                    'ws_business': conf['okx']['ws_business'],
                    'domain': conf['okx']['domain'],
                    'useServerTime': conf.getboolean('okx', 'useServerTime')}
            if conf.has_section('binance'):
                self.binance = {'apiKey': conf['binance']['apiKey'], 'secretKey': conf['binance']['secretKey']}
            if conf.has_section('dingding'):
                self.token = conf['dingding']['token']
                self.prefix = conf['dingding']['prefix']
                self.period = conf['dingding']['period']
            if conf.has_section('telegram'):
                self.token = conf['telegram']['token']
                self.period = conf['telegram']['period']

    @staticmethod
    def load():
        parser = ConfigParser()
        root_dir = os.path.abspath(os.curdir)
        conf_file = path.join(root_dir, 'app.conf')
        if path.exists(conf_file):
            parser.read(conf_file, encoding='UTF-8')
            return TradeBotConf(parser)
        else:
            return TradeBotConf()
