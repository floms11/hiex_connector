from hiex_connector.base import HiExConnectorBase
from hiex_connector.types import *


class HiExConnector(HiExConnectorBase):
    def admin_coins_list(self):
        resp = self.get_request('admin/coins/list', {})
        coins = []
        for coin in resp['coins']:
            coins.append(Coin(**coin))
        return coins
