from ..base import HiExConnectorBase
from ..types import *


class HiExConnector(HiExConnectorBase):
    """
    Синхронна бібліотека для роботи з api.hiex.io
    """
    def admin_coins_list(self):
        """
        Отримати список монет, які зараз підтримує система

        :return: Currency
        """
        resp = self.get_request('admin/coins/list', {})
        coins = []
        for coin in resp['coins']:
            coins.append(Currency(**coin))
        return coins

    def admin_exchange_update(self, exchange_id, step: int = None):
        """
        Редагувати обмін

        :param exchange_id: Номер обміну
        :param step: Крок який потрібно встановити на обмін

        :return: Exchange
        """
        resp = self.get_request('admin/exchange/update', {
            'exchange_id': exchange_id,
            'step': step,
        })
        return Exchange(**resp['exchange'])

    def admin_exchange_get(self, exchange_id):
        """
        Отримати обмін

        :param exchange_id: Номер обміну

        :return: Exchange
        """
        resp = self.get_request('admin/exchange/get', {
            'exchange_id': exchange_id,
        })
        return Exchange(**resp['exchange'])

    def admin_exchanges_list(self, application_id=None, user_id=None, limit=None, offset=None, group=None):
        """
        Отримати список обмінів (за вибіркою)

        :param application_id: Номер додатку
        :param user_id: Номер користувача
        :param limit: Скільки обмінів завантажувати
        :param offset: Починати з рядку
        :param group: Група обмінів (fail, cancel, in_process, success)

        :return: list[Exchange]
        """
        resp = self.get_request('admin/exchanges/list', {
            'application_id': application_id,
            'user_id': user_id,
            'limit': limit,
            'offset': offset,
            'group': group,
        })
        exchanges = []
        for exchange in resp['exchanges']:
            exchanges.append(Exchange(**exchange))
        return exchanges

    def admin_logs_list(self):
        """
        Отримати список логів

        :return: list[Log]
        """
        resp = self.get_request('admin/logs/list', {
        })
        logs = []
        for log in resp['logs']:
            logs.append(Log(**log))
        return logs

    def admin_logs_get(self, name):
        """
        Завантажити лог (за ім'ям)

        :param name: Ім'я логу

        :return: str
        """
        resp = self.get_request_data('admin/logs/get', {
            'name': name
        })
        return resp[0]

    def admin_stats_get(self, application_id=None, limit=None, offset=None):
        """
        Завантажити статистику (за вибіркою)

        :param application_id: Номер додатку
        :param limit: Кількість днів
        :param offset: Скільки останніх днів пропустити

        :return: list[Stat]
        """
        resp = self.get_request('admin/stats/get', {
            'application_id': application_id,
            'limit': limit,
            'offset': offset,
        })
        stats = []
        for stat in resp['stats']:
            stats.append(Stat(**stat))
        return stats

    def admin_applications_list(self):
        """
        Завантажити список додатків у системі

        :return: list[Application]
        """
        resp = self.get_request('admin/applications/list', {
        })
        applications = []
        for application in resp['applications']:
            applications.append(Application(**application))
        return applications

    def admin_application_create(self, name, available_methods, interest):
        """
        Створити новий додаток

        :param name: Ім'я додатку
        :param available_methods: Список методів, які будуть доступні додатку
        :param interest: % від обмінів

        :return: Application
        """
        resp = self.get_request('admin/application/create', {
            'name': name,
            'available_methods': available_methods,
            'interest': interest,
        })
        return Application(**resp['application'])

    def admin_application_details(self, application_id):
        """
        Завантажити інформацію додатку

        :param application_id: Номер додатку

        :return: Application
        """
        resp = self.get_request('admin/application/details', {
            'application_id': application_id,
        })
        return Application(**resp['application'])

    def admin_application_delete(self, application_id):
        """
        Видалити додаток

        :param application_id: Номер додатку

        :return: bool
        """
        self.get_request('admin/application/delete', {
            'application_id': application_id,
        })
        return True

    def admin_application_update(self, application_id, available_methods=None, balance=None, interest=None, update_keys=None, name=None, notification_url=None):
        """
        Редагувати додаток

        :param application_id: Номер додатку
        :param available_methods: Список методів, які будуть доступні додатку
        :param balance: Кількість грошей на рахунку додатку
        :param interest: % від обмінів
        :param update_keys: True, якщо потрібно згенерувати нові ключі
        :param name: Ім'я додатку
        :param notification_url: URL для отримання сповіщень

        :return: Application
        """
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
        """
        Отримати список доступних пар обміну

        :param currency1: Валюта яку купуємо
        :param currency2: Валюта яку продаємо

        :return: list[Pair]
        """
        resp = self.get_request('admin/pairs/list', {
            'currency1': currency1,
            'currency2': currency2,
        })
        pairs = []
        for pair in resp['pairs']:
            pairs.append(Pair(**pair))
        return pairs

    def admin_pair_create(self, currency1, currency2, comment, kyc_required, swap_deposit, active=None, interest=None, max_amount1=None, max_amount2=None, min_amount1=None, min_amount2=None):
        """
        Створити валютну пару

        :param currency1: Валюта яку купуємо
        :param currency2: Валюта яку продаємо
        :param comment: Коротний коментар
        :param kyc_required: Чи потрібен KYC для обміну
        :param swap_deposit: Чи потрібно робити автоматичний обмін
        :param active: Чи активний обмін
        :param interest: % нашого інтересу
        :param max_amount1: Максимальна сума депозиту
        :param max_amount2: Максимальна сума виплати
        :param min_amount1: Мінімальна сума депозиту
        :param min_amount2: Мінімальна сума виплати

        :return: Pair
        """
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
        """
        Змінити валютну пару

        :param currency1: Валюта яку купуємо
        :param currency2: Валюта яку продаємо
        :param active: Чи активний обмін
        :param comment: Коротний коментар
        :param interest: % нашого інтересу
        :param max_amount1: Максимальна сума депозиту
        :param max_amount2: Максимальна сума виплати
        :param min_amount1: Мінімальна сума депозиту
        :param min_amount2: Мінімальна сума виплати
        :param kyc_required: Чи потрібен KYC для обміну
        :param swap_deposit: Чи потрібно робити автоматичний обмін

        :return: Pair
        """
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
        """
        Видалити валютну пару

        :param currency1: Валюта яку купуємо
        :param currency2: Валюта яку продаємо

        :return: bool
        """
        self.get_request('admin/pair/delete', {
            'currency1': currency1,
            'currency2': currency2,
        })
        return True

    def admin_user_details(self, user_id=None, email=None):
        """
        Отримати інформацію про користувача

        :param user_id: Номер користувача
        :param email: Пошта користувача

        :return: User
        """
        resp = self.get_request('admin/user/details', {
            'user_id': user_id,
            'email': email,
        })
        return User(**resp['user'])

    def admin_user_update(self, user_id=None, email=None, name=None, lastname=None, kyc=None):
        """
        Змінити інформацію про користувача

        :param user_id: Номер користувача
        :param email: Нова пошта
        :param name: Нове ім'я
        :param lastname: Нове прізвище
        :param kyc: KYC

        :return: User
        """
        resp = self.get_request('admin/user/update', {
            'user_id': user_id,
            'email': email,
            'name': name,
            'lastname': lastname,
            'kyc': kyc,
        })
        return User(**resp['user'])

    def admin_setting(self, **kwargs):
        """
        Завантажити/змінити налаштування системи

        :param kwargs: Параметри які потрібно змінити

        :return: dict
        """
        resp = self.get_request('admin/setting', kwargs)
        return resp['hisettings']
