from ..base import HiExConnectorBase
from ..types import Empty, ResponseList
from decimal import Decimal


class HiExConnector(HiExConnectorBase):
    """
    Синхронна бібліотека для роботи з api.hiex.io
    """
    def currencies_list(self):
        """
        Отримати список валют

        :return: ResponseList[Currency]
        """
        resp = self.get_request('currencies/list', {})
        from ..types.sync_types import SyncCurrency
        currencies = ResponseList()
        currencies.is_all = resp['is_all']
        for currency in resp['currencies']:
            currencies.append(SyncCurrency(connector=self, **currency))
        return currencies

    def pairs_list(self, currency1=Empty, currency2=Empty, search1=Empty, search2=Empty):
        """
        Отримати список валютних пар

        :param currency1: Валюта яку купуємо
        :param currency2: Валюта яку продаємо
        :param search1: Пошук валют які купуємо
        :param search2: Пошук валют які продаємо

        :return: ResponseList[Pair]
        """
        resp = self.get_request('pairs/list', {
            'currency1': currency1,
            'currency2': currency2,
            'search1': search1,
            'search2': search2,
        })
        from ..types.sync_types import SyncPair
        pairs = ResponseList()
        pairs.is_all = resp['is_all']
        for pair in resp['pairs']:
            pairs.append(SyncPair(connector=self, **pair))
        return pairs

    def pair_amount(self, currency1, currency2, amount1=Empty, amount2=Empty):
        """
        Порахувати суми обміну

        :param currency1: Валюта яку купуємо
        :param currency2: Валюта яку продаємо
        :param amount1: Сума в currency1
        :param amount2: Сума в currency2

        :return: list[amount1, amount2, rate]
        """
        resp = self.get_request('pair/amount', {
            'currency1': currency1,
            'currency2': currency2,
            'amount1': amount1,
            'amount2': amount2,
        })
        return Decimal(resp['amount1']), Decimal(resp['amount2']), Decimal(resp['rate'])

    def exchange_create(
            self, currency1, currency2, address, tag=Empty, amount1=Empty, amount2=Empty, return_url=Empty,
            beneficiary_first_name=Empty, beneficiary_last_name=Empty, beneficiary_tin=Empty, beneficiary_phone=Empty,
            validation=Empty,
    ):
        """
        Створити новий обмін

        :param currency1: Валюта яку купуємо
        :param currency2: Валюта яку продаємо
        :param address: Адреса на яку відправляємо currency2
        :param tag: Тег до адреси (якщо потрібен)
        :param amount1: Сума currency1
        :param amount2: Сума currency2
        :param return_url: URL на який користувач повернеться після оплати карткою
        :param beneficiary_first_name: Інформація по запиту мерчанта. Ім'я отримувача
        :param beneficiary_last_name: Інформація по запиту мерчанта. Прізвище отримувача
        :param beneficiary_tin: Інформація по запиту мерчанта. Номер платника податку отримувача
        :param beneficiary_phone: Інформація по запиту мерчанта. Номер телефону отримувача
        :param validation: Тільки перевірити, чи можливо створити такий обмін

        :return: Exchange
        """
        from ..types.sync_types import SyncExchange
        resp = self.get_request('exchange/create', {
            'currency1': currency1,
            'currency2': currency2,
            'address': address,
            'tag': tag,
            'amount1': amount1,
            'amount2': amount2,
            'return_url': return_url,
            'beneficiary_first_name': beneficiary_first_name,
            'beneficiary_last_name': beneficiary_last_name,
            'beneficiary_tin': beneficiary_tin,
            'beneficiary_phone': beneficiary_phone,
            'validation': validation,
        })
        return SyncExchange(connector=self, **resp['exchange']) if resp['exchange'] else None

    def exchange_payment_get(self, exchange_id):
        """
        Отримати реквізити для сплати обміну

        :param exchange_id: Номер обміну

        :return: Payment
        """
        from ..types.sync_types import SyncPayment
        resp = self.get_request('exchange/payment/get', {
            'exchange_id': exchange_id,
        })
        return SyncPayment(connector=self, **resp['payment'])

    def exchange_get(self, exchange_id, auth_key=None):
        """
        Отримати інформацію по обміну

        :param exchange_id: Номер обміну

        :return: Exchange
        """
        resp = self.get_request('exchange/get', {
            'exchange_id': exchange_id,
        })
        if auth_key is None:
            from ..types.sync_types import SyncExchange
            return SyncExchange(connector=self, **resp['exchange'])
        else:
            from ..types.sync_types import SyncExchangeWithAuthKey
            return SyncExchangeWithAuthKey(connector=self, auth_key=auth_key, **resp['exchange'])

    def exchange_cancel(self, exchange_id):
        """
        Відмінити обмін

        :param exchange_id: Номер обміну

        :return: Exchange
        """
        self.get_request('exchange/cancel', {
            'exchange_id': exchange_id,
        })
        return True

    def exchanges_list(self, limit=Empty, offset=Empty, status_list=Empty, short_exchange_id=Empty):
        """
        Отримати список обмінів

        :param limit: Скільки обмінів завантажувати
        :param offset: Починати з рядку
        :param status_list: Список статусів
        :param short_exchange_id: Перші символи з exchange_id


        :return: ResponseList[Exchange]
        """
        from ..types.sync_types import SyncExchange
        resp = self.get_request('exchanges/list', {
            'limit': limit,
            'offset': offset,
            'status_list': status_list,
            'short_exchange_id': short_exchange_id,
        })
        exchanges = ResponseList()
        exchanges.is_all = resp['is_all']
        for exchange in resp['exchanges']:
            exchanges.append(SyncExchange(connector=self, **exchange))
        return exchanges

    def application_exchanges_list(self, limit=Empty, offset=Empty, user_id=Empty, status_list=Empty, short_exchange_id=Empty):
        """
        Отримати список обмінів

        :param limit: Скільки обмінів завантажувати
        :param offset: Починати з рядку
        :param user_id: ID користувача
        :param status_list: Список статусів
        :param short_exchange_id: Перші символи з exchange_id


        :return: ResponseList[Exchange]
        """
        from ..types.sync_types import SyncExchange
        resp = self.get_request('application/exchanges/list', {
            'limit': limit,
            'offset': offset,
            'user_id': user_id,
            'status_list': status_list,
            'short_exchange_id': short_exchange_id,
        })
        exchanges = ResponseList()
        exchanges.is_all = resp['is_all']
        for exchange in resp['exchanges']:
            exchanges.append(SyncExchange(connector=self, **exchange))
        return exchanges

    def application_users_list(self, limit=Empty, offset=Empty):
        """
        Отримати список користувачів

        :param limit: Скільки обмінів завантажувати
        :param offset: Починати з рядку


        :return: ResponseList[User]
        """
        from ..types.sync_types import SyncUser
        resp = self.get_request('application/users/list', {
            'limit': limit,
            'offset': offset,
        })
        users = ResponseList()
        users.is_all = resp['is_all']
        for user in resp['users']:
            users.append(SyncUser(connector=self, **user))
        return users

    def application_stats_list(self, limit=Empty, offset=Empty):
        """
        Завантажити статистику (за вибіркою)

        :param limit: Кількість днів
        :param offset: Скільки останніх днів пропустити

        :return: ResponseList[Stat]
        """
        from ..types.sync_types import SyncStat
        resp = self.get_request('application/stats/list', {
            'limit': limit,
            'offset': offset,
        })
        stats = ResponseList()
        stats.is_all = resp['is_all']
        for stat in resp['stats']:
            stats.append(SyncStat(connector=self, **stat))
        return stats

    def application_get(self):
        """
        Отримати інформацію про додаток

        :return: Application
        """
        from ..types.sync_types import SyncApplication
        resp = self.get_request('application/get', {})
        return SyncApplication(connector=self, **resp['application'])

    def application_interest_set(self, interest):
        """
        Змінити % від обмінів

        :param interest: % від обмінів

        :return: Decimal
        """
        resp = self.get_request('application/interest/set', {
            'interest': interest,
        })
        return Decimal(resp['interest'])

    def user_get(self, auth_key):
        """
        Завантажити користувача

        :param auth_key: Ключ користувача

        :return: User
        """
        from ..types.sync_types import SyncUserWithAuthKey
        resp = self.get_request('user/get', {
            'auth_key': auth_key,
        })
        return SyncUserWithAuthKey(connector=self, auth_key=auth_key, **resp['user'])

    def user_referrals_list(self, auth_key, limit=Empty, offset=Empty):
        """
        Завантажити список рефералів

        :param auth_key: Ключ користувача
        :param limit: Скільки рефералів завантажувати
        :param offset: Починати з рядку

        :return: list
        """
        from ..types.sync_types import SyncReferral
        resp = self.get_request('user/referrals/list', {
            'auth_key': auth_key,
            'limit': limit,
            'offset': offset,
        })
        referrals = ResponseList()
        referrals.is_all = resp['is_all']
        for referral in resp['referrals']:
            referrals.append(SyncReferral(connector=self, **referral))
        return referrals

    def user_logout(self, auth_key):
        """
        Розлогінити користувача (деактивувати auth_key в системі)

        :param auth_key: Ключ користувача

        :return: User
        """
        self.get_request('user/logout', {
            'auth_key': auth_key,
        })
        return True

    def user_kyc_get(self, auth_key, method, option=Empty, return_url=Empty):
        """
        Отримати лінк для проходження KYC (верифікації)

        :param auth_key: Ключ користувача
        :param method: Спосіб проходження верифікації
        :param option: Додатковий параметр верифікації
        :param return_url: URL куди повернуто користувача після проходження KYC

        :return: Verification
        """
        from ..types.sync_types import SyncVerification
        resp = self.get_request('user/kyc/get', {
            'auth_key': auth_key,
            'method': method,
            'option': option,
            'return_url': return_url,
        })
        return SyncVerification(connector=self, **resp['verification'])

    def user_kyc_methods_list(self, auth_key):
        """
        Завантажити можливі способи проходження верифікації

        :param auth_key: Ключ користувача

        :return: ResponseList[VerificationService]
        """
        from ..types.sync_types import SyncVerificationService
        resp = self.get_request('user/kyc/methods/list', {
            'auth_key': auth_key,
        })
        verification_services = ResponseList()
        verification_services.is_all = resp['is_all']
        for method in resp['methods']:
            verification_services.append(SyncVerificationService(connector=self, **method))
        return verification_services

    def user_auth(self, email, referral_token=Empty):
        """
        Запит на авторизацію користувача

        :param email: Пошта користувача
        :param referral_token: Реферальний токен

        :return: Auth
        """
        from ..types.sync_types import SyncAuth
        resp = self.get_request('user/auth', {
            'email': email,
            'referral_token': referral_token,
        })
        return SyncAuth(connector=self, **resp['auth'])

    def user_auth_code(self, auth_key, code):
        """
        Реєстрація коду авторизації

        :param auth_key: Ключ користувача
        :param code: Код, який користвувач отримав на пошту

        :return: Auth
        """
        from ..types.sync_types import SyncAuth
        resp = self.get_request('user/auth/code', {
            'auth_key': auth_key,
            'code': code,
        })
        return SyncAuth(connector=self, **resp['auth'])

    def user_exchange_create(
            self, auth_key, currency1, currency2, address, tag=Empty, amount1=Empty, amount2=Empty, return_url=Empty,
            beneficiary_first_name=Empty, beneficiary_last_name=Empty, beneficiary_tin=Empty, beneficiary_phone=Empty,
            validation=Empty,
    ):
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
        :param beneficiary_first_name: Інформація по запиту мерчанта. Ім'я отримувача
        :param beneficiary_last_name: Інформація по запиту мерчанта. Прізвище отримувача
        :param beneficiary_tin: Інформація по запиту мерчанта. Номер платника податку отримувача
        :param beneficiary_phone: Інформація по запиту мерчанта. Номер телефону отримувача
        :param validation: Тільки перевірити, чи можливо створити такий обмін

        :return: Exchange
        """
        from ..types.sync_types import SyncExchangeWithAuthKey
        resp = self.get_request('user/exchange/create', {
            'auth_key': auth_key,
            'currency1': currency1,
            'currency2': currency2,
            'address': address,
            'tag': tag,
            'amount1': amount1,
            'amount2': amount2,
            'return_url': return_url,
            'beneficiary_first_name': beneficiary_first_name,
            'beneficiary_last_name': beneficiary_last_name,
            'beneficiary_tin': beneficiary_tin,
            'beneficiary_phone': beneficiary_phone,
            'validation': validation,
        })
        return SyncExchangeWithAuthKey(connector=self, auth_key=auth_key, **resp['exchange']) if resp['exchange'] else None

    def user_exchanges_list(self, auth_key, limit=Empty, offset=Empty, status_list=Empty, short_exchange_id=Empty):
        """
        Отримати список обмінів користувача (за вибіркою)

        :param auth_key: Ключ користувача
        :param limit: Скільки обмінів завантажувати
        :param offset: Починати з рядку
        :param status_list: Список статусів
        :param short_exchange_id: Перші символи з exchange_id


        :return: ResponseList[Exchange]
        """
        from ..types.sync_types import SyncExchangeWithAuthKey
        resp = self.get_request('user/exchanges/list', {
            'auth_key': auth_key,
            'limit': limit,
            'offset': offset,
            'status_list': status_list,
            'short_exchange_id': short_exchange_id,
        })
        exchanges = ResponseList()
        exchanges.is_all = resp['is_all']
        for exchange in resp['exchanges']:
            exchanges.append(SyncExchangeWithAuthKey(connector=self, auth_key=auth_key, **exchange))
        return exchanges

    def user_data_save(self, auth_key, **kwargs):
        """
        Запис даних додатку

        :param auth_key: Ключ користувача
        :param kwargs: Аргументи які потрібно зберегти

        :return:
        """
        data = kwargs
        data['auth_key'] = auth_key
        resp = self.get_request('user/data/save', data)
        return resp['saved']

    def user_exchange_cancel(self, auth_key, exchange_id):
        """
        Відмінити обмін

        :param auth_key: Ключ користувача
        :param exchange_id: Номер обміну

        :return: Exchange
        """
        self.get_request('user/exchange/cancel', {
            'auth_key': auth_key,
            'exchange_id': exchange_id,
        })
        return True

