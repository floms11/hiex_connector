from ..base import HiExConnectorBase
from ..types import *
from decimal import Decimal


class AsyncHiExConnector(HiExConnectorBase):
    """
    Асинхронна бібліотека для роботи з api.hiex.io
    """
    async def pairs_list(self, currency1=None, currency2=None):
        """
        Отримати список валютних пар

        :param currency1: Валюта яку купуємо
        :param currency2: Валюта яку продаємо

        :return: list[Pair]
        """
        resp = await self.get_async_request('pairs/list', {
            'currency1': currency1,
            'currency2': currency2,
        })
        pairs = []
        for pair in resp['pairs']:
            pairs.append(Pair(**pair))
        return pairs

    async def pair_amount(self, currency1, currency2, amount1=None, amount2=None):
        """
        Порахувати суми обміну

        :param currency1: Валюта яку купуємо
        :param currency2: Валюта яку продаємо
        :param amount1: Сума в currency1
        :param amount2: Сума в currency2

        :return: list[amount1, amount2]
        """
        resp = await self.get_async_request('pair/amount', {
            'currency1': currency1,
            'currency2': currency2,
            'amount1': amount1,
            'amount2': amount2,
        })
        return Decimal(resp['amount1']), Decimal(resp['amount2'])

    async def user_get(self, auth_key):
        """
        Завантажити користувача

        :param auth_key: Ключ користувача

        :return: User
        """
        resp = await self.get_async_request('user/get', {
            'auth_key': auth_key,
        })
        return User(**resp['user'])

    async def user_logout(self, auth_key):
        """
        Розлогінити користувача (деактивувати auth_key в системі)

        :param auth_key: Ключ користувача

        :return: User
        """
        resp = await self.get_async_request('user/logout', {
            'auth_key': auth_key,
        })
        return True

    async def user_kyc_get(self, auth_key):
        """
        Отримати лінк для проходження KYC (верифікації)

        :param auth_key: Ключ користувача

        :return: str
        """
        resp = await self.get_async_request('user/kyc/get', {
            'auth_key': auth_key,
        })
        return resp['kyc_url']

    async def user_auth(self, email):
        """
        Запит на авторизацію користувача

        :param email: Пошта користувача

        :return: Auth
        """
        resp = await self.get_async_request('user/auth', {
            'email': email,
        })
        return Auth(**resp['auth'])

    async def user_auth_code(self, auth_key, code):
        """
        Реєстрація коду авторизації

        :param auth_key: Ключ користувача
        :param code: Код, який користвувач отримав на пошту

        :return: Auth
        """
        resp = await self.get_async_request('user/auth/code', {
            'auth_key': auth_key,
            'code': code,
        })
        return Auth(**resp['auth'])

    async def user_exchanges_history(self, auth_key, limit=None, offset=None, group=None):
        """
        Отримати список обмінів користувача (за вибіркою)

        :param auth_key: Ключ користувача
        :param limit: Скільки обмінів завантажувати
        :param offset: Починати з рядку
        :param group: Група обмінів (cancel, in_process, success)


        :return: list[Exchange]
        """
        resp = await self.get_async_request('user/exchanges/history', {
            'auth_key': auth_key,
            'limit': limit,
            'offset': offset,
            'group': group,
        })
        exchanges = []
        for exchange in resp['exchanges']:
            exchanges.append(Exchange(**exchange))
        return exchanges

    async def user_data_get(self, auth_key):
        """
        Отримання даних додатку

        :param auth_key: Ключ користувача

        :return:
        """
        resp = await self.get_async_request('user/data/get', {
            'auth_key': auth_key,
        })
        return resp['data']

    async def user_data_set(self, auth_key, **kwargs):
        """
        Запис даних додатку

        :param auth_key: Ключ користувача
        :param kwargs: Аргументи які потрібно зберегти

        :return:
        """
        data = kwargs
        data['auth_key'] = auth_key
        resp = await self.get_async_request('user/data/set', data)
        return resp['saved']

    async def exchange_create(self, auth_key, currency1, currency2, address, tag=None, amount1=None, amount2=None, return_url=None):
        """
        Створити новий обмін

        :param auth_key: Ключ користувача
        :param currency1: Валюта яку купуємо
        :param currency2: Валюта яку продаємо
        :param address: Адреса на яку відправляємо currency2
        :param tag: Тег до адреси (якщо потрібен)
        :param amount1: Сума currency1
        :param amount2: Сума currency2
        :param return_url: URL на який користувач повернеться після оплати карткою

        :return: Exchange
        """
        resp = await self.get_async_request('exchange/create', {
            'auth_key': auth_key,
            'currency1': currency1,
            'currency2': currency2,
            'address': address,
            'tag': tag,
            'amount1': amount1,
            'amount2': amount2,
            'return_url': return_url,
        })
        return Exchange(**resp['exchange'])

    async def exchange_confirm(self, auth_key, exchange_id):
        """
        Підтвердження обміну

        :param auth_key: Ключ користувача
        :param exchange_id: Номер обміну

        :return: Exchange
        """
        resp = await self.get_async_request('exchange/confirm', {
            'auth_key': auth_key,
            'exchange_id': exchange_id,
        })
        return Exchange(**resp['exchange'])

    async def exchange_details(self, exchange_id):
        """
        Отримати інформацію по обміну

        :param exchange_id: Номер обміну

        :return: Exchange
        """
        resp = await self.get_async_request('exchange/details', {
            'exchange_id': exchange_id,
        })
        return Exchange(**resp['exchange'])

    async def exchange_cancel(self, auth_key, exchange_id):
        """
        Відмінити обмін

        :param auth_key: Ключ користувача
        :param exchange_id: Номер обміну

        :return: Exchange
        """
        await self.get_async_request('exchange/cancel', {
            'auth_key': auth_key,
            'exchange_id': exchange_id,
        })
        return True

    async def application_exchanges_get(self, user_id=None, limit=None, offset=None, group=None):
        """
        Отримати список обмінів додатку (за вибіркою)

        :param user_id: Номер користувача
        :param limit: Скільки обмінів завантажувати
        :param offset: Починати з рядку
        :param group: Група обмінів (cancel, in_process, success)


        :return: list[Exchange]
        """
        resp = await self.get_async_request('application/exchanges/get', {
            'user_id': user_id,
            'limit': limit,
            'offset': offset,
            'group': group,
        })
        exchanges = []
        for exchange in resp['exchanges']:
            exchanges.append(Exchange(**exchange))
        return exchanges

    async def application_stats_get(self, limit=None, offset=None):
        """
        Завантажити статистику (за вибіркою)

        :param limit: Кількість днів
        :param offset: Скільки останніх днів пропустити

        :return: list[Stat]
        """
        resp = await self.get_async_request('application/stats/get', {
            'limit': limit,
            'offset': offset,
        })
        stats = []
        for stat in resp['stats']:
            stats.append(Stat(**stat))
        return stats

    async def application_details(self):
        """
        Отримати інформацію про додаток

        :return: Application
        """
        resp = await self.get_async_request('application/details', {})
        return Application(**resp['application'])

    async def application_interest_set(self, interest):
        """
        Змінити % від обмінів

        :param interest: % від обмінів

        :return: Decimal
        """
        resp = await self.get_async_request('application/interest/set', {
            'interest': interest,
        })
        return Decimal(resp['interest'])

