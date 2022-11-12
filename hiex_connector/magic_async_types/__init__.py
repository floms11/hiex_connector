from decimal import Decimal

from ..async_connector import AsyncHiExConnector
from .. import types


class Pair(types.Pair):
    __connector: AsyncHiExConnector

    def __init__(self, connector: AsyncHiExConnector, **kwargs):
        super().__init__(**kwargs)
        self.__connector = connector

    async def amount(self, amount1=None, amount2=None):
        """
        Порахувати суми обміну

        :param amount1: Сума в currency1
        :param amount2: Сума в currency2

        :return: list[amount1, amount2]
        """
        return await self.__connector.pair_amount(self.currency1.code, self.currency2.code, amount1, amount2)


class User(types.User):
    __connector: AsyncHiExConnector
    __auth_key: str

    def __init__(self, connector: AsyncHiExConnector, auth_key: str, **kwargs):
        super().__init__(**kwargs)
        self.__connector = connector
        self.__auth_key = auth_key

    async def reload(self):
        """
        Оновити інформацію про користувача

        :return: bool
        """
        o = await self.__connector.user_get(self.__auth_key)
        super().__init__(**o.get_dict())
        return True

    async def referrals(self, limit=None, offset=None):
        """
        Завантажити список рефералів

        :param limit: Скільки рефералів завантажувати
        :param offset: Починати з рядку

        :return: list
        """
        return await self.__connector.user_referrals_list(self.__auth_key, limit, offset)

    async def logout(self):
        """
        Розлогінити користувача (деактивувати auth_key в системі)

        :return: bool
        """
        return await self.__connector.user_logout(self.__auth_key)

    async def kyc_link(self):
        """
        Отримати лінк для проходження KYC (верифікації)

        :param auth_key: Ключ користувача

        :return: str
        """
        return await self.__connector.user_kyc_get(self.__auth_key)

    async def exchanges(self, limit=None, offset=None, group=None):
        """
        Отримати історію обмінів користувача

        :param limit: Скільки обмінів завантажувати
        :param offset Починати з рядку
        :param group: Група обмінів (cancel, in_process, success)
        :return:
        """
        return await self.__connector.user_exchanges_list(self.__auth_key, limit, offset, group)

    async def exchange(self, exchange_id):
        """
        Завантажити обмін

        :param exchange_id: Номер обміну
        :return: Exchange
        """
        return await self.__connector.exchange_get(exchange_id, auth_key=self.__auth_key)

    async def exchange_create(self, pair: Pair, address: str, tag: str = None, amount1: Decimal = None, amount2: Decimal = None, return_url: str = None):
        """
        Створити новий обмін

        :param pair: Валютна пара
        :param address: Адреса на яку потрібно отримати кошти
        :param tag: Тег до адреси (якщо потрібен)
        :param amount1: Сума currency1
        :param amount2: Сума currency2
        :param return_url: URL на який користувач повернеться після оплати карткою
        :return: Exchange
        """
        return await self.__connector.exchange_create(
            self.__auth_key,
            pair.currency1.code,
            pair.currency2.code,
            address,
            tag,
            amount1,
            amount2,
            return_url,
        )

    async def data_save(self, **kwargs):
        """
        Записати дані користувача на серверах hiex.io

        :param kwargs: Зміні які потрібно записати
        :return: bool
        """
        await self.__connector.user_data_save(self.__auth_key, **kwargs)
        return True


class Auth(types.Auth):
    __connector: AsyncHiExConnector

    def __init__(self, connector: AsyncHiExConnector, **kwargs):
        super().__init__(**kwargs)
        self.__connector = connector

    async def code(self, code=None):
        """
        Реєстрація коду авторизації

        :param code: Код з email
        :return:
        """
        o = await self.__connector.user_auth_code(self.auth_key, code)
        super().__init__(**o.get_dict())

    async def user(self):
        """
        Завантажити користувача

        :return: User
        """
        return await self.__connector.user_get(self.auth_key)


class Exchange(types.Exchange):
    __connector: AsyncHiExConnector
    __auth_key: str

    def __init__(self, connector: AsyncHiExConnector, auth_key: str, **kwargs):
        super().__init__(**kwargs)
        self.__connector = connector
        self.__auth_key = auth_key

    async def user(self):
        """
        Завантажити користувача

        :return: User
        """
        return await self.__connector.user_get(self.__auth_key)

    async def reload(self):
        """
        Оновити інформацію обміну

        :return: bool
        """
        o = await self.__connector.exchange_get(self.exchange_id)
        super().__init__(**o.get_dict())
        return True

    async def confirm(self):
        """
        Підтвердити обмін

        :return: bool
        """
        o = await self.__connector.exchange_confirm(self.__auth_key, self.exchange_id)
        super().__init__(**o.get_dict())
        return True

    async def cancel(self):
        """
        Відмінити обмін

        :return: bool
        """
        return await self.__connector.exchange_cancel(self.__auth_key, self.exchange_id)


class Application(types.Application):
    __connector: AsyncHiExConnector

    def __init__(self, connector: AsyncHiExConnector, **kwargs):
        super().__init__(**kwargs)
        self.__connector = connector

    async def reload(self):
        """
        Оновити інформацію про додаток

        :return: bool
        """
        o = await self.__connector.application_get()
        super().__init__(**o.get_dict())
        return True

    async def exchanges(self, user_id=None, limit=None, offset=None, group=None):
        """
        Отримати список обмінів додатку (за вибіркою)

        :param user_id: Номер користувача
        :param limit: Скільки обмінів завантажувати
        :param offset: Починати з рядку
        :param group: Група обмінів (cancel, in_process, success)
        :return:
        """
        return await self.__connector.application_exchanges_list(user_id, limit, offset, group)

    async def users(self, limit=None, offset=None):
        """
        Отримати список користувачів додатку

        :param limit: Скільки користувачів завантажувати
        :param offset: Починати з рядку
        :return:
        """
        return await self.__connector.application_users_list(limit, offset)

    async def stats(self, limit=None, offset=None):
        """
        Завантажити статистику (за вибіркою)

        :param limit: Кількість днів
        :param offset: Починати з рядку

        :return:
        """
        return await self.__connector.application_stats_list(limit, offset)

    async def interest_set(self, interest):
        """
        Змінити % від обмінів

        :param interest: % від обмінів

        :return: Decimal
        """
        return await self.__connector.application_interest_set(interest)

