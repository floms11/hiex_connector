from ..base import HiExConnectorBase
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

        :return: ResponseList[Pair]
        """
        resp = await self.get_async_request('pairs/list', {
            'currency1': currency1,
            'currency2': currency2,
        })
        from ..types import ResponseList
        from ..magic_async_types import Pair
        pairs = ResponseList()
        pairs.is_all = resp['is_all']
        for pair in resp['pairs']:
            pairs.append(Pair(self, **pair))
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
        from ..magic_async_types import User
        resp = await self.get_async_request('user/get', {
            'auth_key': auth_key,
        })
        return User(self, auth_key, **resp['user'])

    async def user_referrals_list(self, auth_key, limit=None, offset=None):
        """
        Завантажити список рефералів

        :param auth_key: Ключ користувача
        :param limit: Скільки рефералів завантажувати
        :param offset: Починати з рядку

        :return: list
        """
        from ..types import ResponseList, Referral
        resp = await self.get_async_request('user/referrals/list', {
            'auth_key': auth_key,
            'limit': limit,
            'offset': offset,
        })
        referrals = ResponseList()
        referrals.is_all = resp['is_all']
        for referral in resp['referrals']:
            referrals.append(Referral(**referral))
        return referrals

    async def user_logout(self, auth_key):
        """
        Розлогінити користувача (деактивувати auth_key в системі)

        :param auth_key: Ключ користувача

        :return: User
        """
        await self.get_async_request('user/logout', {
            'auth_key': auth_key,
        })
        return True

    async def user_kyc_get(self, auth_key, method, option=None, return_url=None):
        """
        Отримати лінк для проходження KYC (верифікації)

        :param auth_key: Ключ користувача
        :param method: Спосіб проходження верифікації
        :param option: Додатковий параметр верифікації
        :param return_url: URL куди повернуто користувача після проходження KYC

        :return: Verification
        """
        from ..types import Verification
        resp = await self.get_async_request('user/kyc/get', {
            'auth_key': auth_key,
            'method': method,
            'option': option,
            'return_url': return_url,
        })
        return Verification(**resp['verification'])

    async def user_kyc_methods_list(self, auth_key):
        """
        Завантажити можливі способи проходження верифікації

        :param auth_key: Ключ користувача

        :return: ResponseList[VerificationService]
        """
        from ..types import ResponseList
        from ..types import VerificationService
        resp = await self.get_async_request('user/kyc/methods/list', {
            'auth_key': auth_key,
        })
        verification_services = ResponseList()
        verification_services.is_all = resp['is_all']
        for method in resp['methods']:
            verification_services.append(VerificationService(**method))
        return verification_services

    async def user_auth(self, email, referral_token=None):
        """
        Запит на авторизацію користувача

        :param email: Пошта користувача
        :param referral_token: Реферальний токен

        :return: Auth
        """
        from ..magic_async_types import Auth
        resp = await self.get_async_request('user/auth', {
            'email': email,
            'referral_token': referral_token,
        })
        return Auth(self, **resp['auth'])

    async def user_auth_code(self, auth_key, code):
        """
        Реєстрація коду авторизації

        :param auth_key: Ключ користувача
        :param code: Код, який користвувач отримав на пошту

        :return: Auth
        """
        from ..magic_async_types import Auth
        resp = await self.get_async_request('user/auth/code', {
            'auth_key': auth_key,
            'code': code,
        })
        return Auth(self, **resp['auth'])

    async def user_exchanges_list(self, auth_key, limit=None, offset=None, status_list=None, short_exchange_id=None):
        """
        Отримати список обмінів користувача (за вибіркою)

        :param auth_key: Ключ користувача
        :param limit: Скільки обмінів завантажувати
        :param offset: Починати з рядку
        :param status_list: Список статусів
        :param short_exchange_id: Перші символи з exchange_id


        :return: ResponseList[Exchange]
        """
        from ..types import ResponseList
        from ..magic_async_types import Exchange
        resp = await self.get_async_request('user/exchanges/list', {
            'auth_key': auth_key,
            'limit': limit,
            'offset': offset,
            'status_list': status_list,
            'short_exchange_id': short_exchange_id,
        })
        exchanges = ResponseList()
        exchanges.is_all = resp['is_all']
        for exchange in resp['exchanges']:
            exchanges.append(Exchange(self, auth_key, **exchange))
        return exchanges

    async def user_data_save(self, auth_key, **kwargs):
        """
        Запис даних додатку

        :param auth_key: Ключ користувача
        :param kwargs: Аргументи які потрібно зберегти

        :return:
        """
        data = kwargs
        data['auth_key'] = auth_key
        resp = await self.get_async_request('user/data/save', data)
        return resp['saved']

    async def exchange_create(self, currency1, currency2, address, tag=None, amount1=None, amount2=None, return_url=None):
        """
        Створити новий обмін

        :param currency1: Валюта яку купуємо
        :param currency2: Валюта яку продаємо
        :param address: Адреса на яку відправляємо currency2
        :param tag: Тег до адреси (якщо потрібен)
        :param amount1: Сума currency1
        :param amount2: Сума currency2
        :param return_url: URL на який користувач повернеться після оплати карткою

        :return: Exchange
        """
        from ..types import Exchange
        resp = await self.get_async_request('exchange/create', {
            'currency1': currency1,
            'currency2': currency2,
            'address': address,
            'tag': tag,
            'amount1': amount1,
            'amount2': amount2,
            'return_url': return_url,
        })
        return Exchange(**resp['exchange'])

    async def user_exchange_create(self, auth_key, currency1, currency2, address, tag=None, amount1=None, amount2=None, return_url=None):
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
        from ..magic_async_types import Exchange
        resp = await self.get_async_request('user/exchange/create', {
            'auth_key': auth_key,
            'currency1': currency1,
            'currency2': currency2,
            'address': address,
            'tag': tag,
            'amount1': amount1,
            'amount2': amount2,
            'return_url': return_url,
        })
        return Exchange(self, auth_key, **resp['exchange'])

    async def exchange_payment_get(self, auth_key, exchange_id):
        """
        Отримати реквізити для сплати обміну

        :param auth_key: Ключ користувача
        :param exchange_id: Номер обміну

        :return: Payment
        """
        from ..types import Payment
        resp = await self.get_async_request('exchange/payment/get', {
            'auth_key': auth_key,
            'exchange_id': exchange_id,
        })
        return Payment(**resp['payment'])

    async def exchange_get(self, exchange_id, auth_key=None):
        """
        Отримати інформацію по обміну

        :param exchange_id: Номер обміну
        :param auth_key: Ключ користувача

        :return: Exchange
        """
        resp = await self.get_async_request('exchange/get', {
            'exchange_id': exchange_id,
            'auth_key': auth_key,
        })
        if auth_key is None:
            from ..types import Exchange
            return Exchange(**resp['exchange'])
        else:
            from ..magic_async_types import Exchange
            return Exchange(self, auth_key, **resp['exchange'])

    async def exchange_cancel(self, exchange_id):
        """
        Відмінити обмін

        :param exchange_id: Номер обміну

        :return: Exchange
        """
        await self.get_async_request('exchange/cancel', {
            'exchange_id': exchange_id,
        })
        return True

    async def user_exchange_cancel(self, auth_key, exchange_id):
        """
        Відмінити обмін

        :param auth_key: Ключ користувача
        :param exchange_id: Номер обміну

        :return: Exchange
        """
        await self.get_async_request('user/exchange/cancel', {
            'auth_key': auth_key,
            'exchange_id': exchange_id,
        })
        return True

    async def application_exchanges_list(self, user_id=None, limit=None, offset=None, status_list=None, short_exchange_id=None):
        """
        Отримати список обмінів додатку (за вибіркою)

        :param user_id: Номер користувача
        :param limit: Скільки обмінів завантажувати
        :param offset: Починати з рядку
        :param status_list: Список статусів
        :param short_exchange_id: Перші символи з exchange_id


        :return: ResponseList[Exchange]
        """
        from ..types import ResponseList, Exchange
        resp = await self.get_async_request('application/exchanges/list', {
            'user_id': user_id,
            'limit': limit,
            'offset': offset,
            'status_list': status_list,
            'short_exchange_id': short_exchange_id,
        })
        exchanges = ResponseList()
        exchanges.is_all = resp['is_all']
        for exchange in resp['exchanges']:
            exchanges.append(Exchange(**exchange))
        return exchanges

    async def application_users_list(self, limit=None, offset=None):
        """
        Отримати список користувачів

        :param limit: Скільки користувачів завантажувати
        :param offset: Починати з рядку


        :return: ResponseList[User]
        """
        from ..types import ResponseList, User
        resp = await self.get_async_request('application/users/list', {
            'limit': limit,
            'offset': offset,
        })
        users = ResponseList()
        users.is_all = resp['is_all']
        for user in resp['users']:
            users.append(User(**user))
        return users

    async def application_stats_list(self, limit=None, offset=None):
        """
        Завантажити статистику (за вибіркою)

        :param limit: Кількість днів
        :param offset: Скільки останніх днів пропустити

        :return: ResponseList[Stat]
        """
        from ..types import ResponseList, Stat
        resp = await self.get_async_request('application/stats/list', {
            'limit': limit,
            'offset': offset,
        })
        stats = ResponseList()
        stats.is_all = resp['is_all']
        for stat in resp['stats']:
            stats.append(Stat(**stat))
        return stats

    async def application_get(self):
        """
        Отримати інформацію про додаток

        :return: Application
        """
        from ..magic_async_types import Application
        resp = await self.get_async_request('application/get', {})
        return Application(self, **resp['application'])

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

