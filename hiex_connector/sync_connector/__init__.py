from hiex_connector.base import HiExConnectorBase
from hiex_connector.types import *


class HiExConnector(HiExConnectorBase):
    def admin_coins_list(self):
        resp = self.get_request('admin/coins/list', {})
        coins = []
        for coin in resp['coins']:
            coins.append(Coin(**coin))
        return coins

    def admin_exchange_update(self, exchange_id, step: int = None):
        resp = self.get_request('admin/exchange/update', {
            'exchange_id': exchange_id,
            'step': step,
        })
        return Exchange(**resp['exchange'])

    def admin_exchanges_list(self):
        resp = self.get_request('admin/exchanges/list', {
        })
        exchanges = []
        for exchange in resp['exchanges']:
            exchanges.append(Exchange(**exchange))
        return exchanges

    def admin_logs_list(self):
        resp = self.get_request('admin/logs/list', {
        })
        logs = []
        for log in resp['logs']:
            logs.append(Log(**log))
        return logs

    def admin_log_get(self, name):
        resp = self.get_request('admin/log/get', {
            'name': name
        })
        return resp
