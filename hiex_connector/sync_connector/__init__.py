from hiex_connector.base import HiExConnectorBase


class HiExConnector(HiExConnectorBase):
    def admin_coins_list(self):
        return self.get_request('admin/coins/list')
