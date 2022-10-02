from hiex_connector.base import HiExConnectorBase
from hiex_connector.types import *
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

    async def user_auth(self, email):
        """
        Запит на авторизацію користувача

        :param email: Пошта користувача

        :return: UserAuth
        """
        resp = await self.get_async_request('user/auth', {
            'email': email,
        })
        return UserAuth(**resp['auth'])

    async def user_auth_code(self, auth_key, code):
        """
        Реєстрація коду авторизації

        :param auth_key: Ключ користувача
        :param code: Код, який користвувач отримав на пошту

        :return: UserAuth
        """
        resp = await self.get_async_request('user/auth/code', {
            'auth_key': auth_key,
            'code': code,
        })
        return UserAuth(**resp['auth'])

    async def user_exchanges_history(self, auth_key, limit=None, start=None, group=None):
        """
        Отримати список обмінів користувача (за вибіркою)

        :param auth_key: Ключ користувача
        :param limit: Скільки обмінів завантажувати
        :param start: З якого обміну почати завантажувати
        :param group: Група обмінів (cancel, in_process, success)


        :return: list[Exchange]
        """
        resp = await self.get_async_request('user/exchanges/history', {
            'auth_key': auth_key,
            'limit': limit,
            'start': start,
            'group': group,
        })
        exchanges = []
        for exchange in resp['exchanges']:
            exchanges.append(Exchange(**exchange))
        return exchanges

    async def user_data_get(self, auth_key, param=None):
        """
        Отримання даних додатку

        :param auth_key: Ключ користувача
        :param param: Значення яке потрібно завантажити

        :return:
        """
        resp = await self.get_async_request('user/data/get', {
            'auth_key': auth_key,
            'param': param,
        })
        if param is not None:
            return resp[param]
        else:
            return resp['all']

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

    async def exchange_create(self, auth_key, currency1, currency2, address, tag=None, amount1=None, amount2=None):
        """
        Створити новий обмін

        :param auth_key: Ключ користувача
        :param currency1: Валюта яку купуємо
        :param currency2: Валюта яку продаємо
        :param address: Адреса на яку відправляємо currency2
        :param tag: Тег до адреси (якщо потрібен)
        :param amount1: Сума currency1
        :param amount2: Сума currency2

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

    async def exchange_details(self, auth_key, exchange_id):
        """
        Отримати інформацію по обміну

        :param auth_key: Ключ користувача
        :param exchange_id: Номер обміну

        :return: Exchange
        """
        resp = await self.get_async_request('exchange/details', {
            'auth_key': auth_key,
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

    async def application_exchanges_get(self, user_id=None, limit=None, start=None, group=None):
        """
        Отримати список обмінів додатку (за вибіркою)

        :param user_id: Номер користувача
        :param limit: Скільки обмінів завантажувати
        :param start: З якого обміну почати завантажувати
        :param group: Група обмінів (cancel, in_process, success)


        :return: list[Exchange]
        """
        resp = await self.get_async_request('application/exchanges/get', {
            'user_id': user_id,
            'limit': limit,
            'start': start,
            'group': group,
        })
        exchanges = []
        for exchange in resp['exchanges']:
            exchanges.append(Exchange(**exchange))
        return exchanges

    async def application_stats_get(self, start_time=None, end_time=None, count=None):
        """
        Завантажити статистику (за вибіркою)

        :param start_time: З якого часу завантажувати (в UNIX time)
        :param end_time: До якого часу завантажувати (в UNIX time)
        :param count: Кількість днів

        :return: list[Stat]
        """
        resp = await self.get_async_request('application/stats/get', {
            'start_time': start_time,
            'end_time': end_time,
            'count': count,
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

