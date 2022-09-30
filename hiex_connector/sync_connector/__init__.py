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

    def admin_exchanges_list(self, application_id=None, user_id=None, limit=None, start=None, group=None):
        resp = self.get_request('admin/exchanges/list', {
            'application_id': application_id,
            'user_id': user_id,
            'limit': limit,
            'start': start,
            'group': group,
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

    def admin_logs_get(self, name):
        resp = self.get_request_text('admin/logs/get', {
            'name': name
        })
        return resp

    def admin_stats_get(self, application_id=None, start_time=None, end_time=None, count=None):
        resp = self.get_request('admin/stats/get', {
            'application_id': application_id,
            'start_time': start_time,
            'end_time': end_time,
            'count': count,
        })
        stats = []
        for stat in resp['stats']:
            stats.append(Stat(**stat))
        return stats

    def admin_applications_list(self):
        resp = self.get_request('admin/applications/list', {
        })
        applications = []
        for application in resp['applications']:
            applications.append(Application(**application))
        return applications

    def admin_application_create(self, name, available_methods, interest):
        resp = self.get_request('admin/application/create', {
            'name': name,
            'available_methods': available_methods,
            'interest': interest,
        })
        return Application(**resp['application'])

    def admin_application_details(self, application_id):
        resp = self.get_request('admin/application/details', {
            'application_id': application_id,
        })
        return Application(**resp['application'])

    def admin_application_delete(self, application_id):
        self.get_request('admin/application/delete', {
            'application_id': application_id,
        })
        return True

    def admin_application_update(self, application_id, available_methods=None, balance=None, interest=None, update_keys=None, name=None, notification_url=None):
        resp = self.get_request('admin/application/update', {
            'application_id': application_id,
            'available_methods': available_methods,
            'balance': balance,
            'interest': interest,
            'update_keys': update_keys,
            'name': name,
            'notification_url': notification_url,
        })
        return Application(**resp['application'])

    def admin_pairs_list(self, currency1=None, currency2=None):
        resp = self.get_request('admin/pairs/list', {
            'currency1': currency1,
            'currency2': currency2,
        })
        pairs = []
        for pair in resp['pairs']:
            pairs.append(Pair(**pair))
        return pairs

    def admin_pair_create(self, currency1, currency2, comment, kyc_required, swap_deposit, active=None, interest=None, max_amount1=None, max_amount2=None, min_amount1=None, min_amount2=None):
        resp = self.get_request('admin/pair/create', {
            'currency1': currency1,
            'currency2': currency2,
            'comment': comment,
            'kyc_required': kyc_required,
            'swap_deposit': swap_deposit,
            'active': active,
            'interest': interest,
            'max_amount1': max_amount1,
            'max_amount2': max_amount2,
            'min_amount1': min_amount1,
            'min_amount2': min_amount2,
        })
        return Pair(**resp['pair'])

    def admin_pair_update(self, currency1, currency2, active=None, comment=None, interest=None, max_amount1=None, max_amount2=None, min_amount1=None, min_amount2=None, kyc_required=None, swap_deposit=None):
        resp = self.get_request('admin/pair/update', {
            'currency1': currency1,
            'currency2': currency2,
            'active': active,
            'comment': comment,
            'interest': interest,
            'max_amount1': max_amount1,
            'max_amount2': max_amount2,
            'min_amount1': min_amount1,
            'min_amount2': min_amount2,
            'kyc_required': kyc_required,
            'swap_deposit': swap_deposit,
        })
        return Pair(**resp['pair'])

    def admin_pair_delete(self, currency1=None, currency2=None):
        self.get_request('admin/pair/delete', {
            'currency1': currency1,
            'currency2': currency2,
        })
        return True

    def admin_user_details(self, user_id=None, email=None):
        resp = self.get_request('admin/user/details', {
            'user_id': user_id,
            'email': email,
        })
        return User(**resp['user'])

    def admin_setting(self, **kwargs):
        resp = self.get_request('admin/setting', kwargs)
        return resp['hisettings']
