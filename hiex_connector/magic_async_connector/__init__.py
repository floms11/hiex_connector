from ..async_connector import AsyncHiExConnector
from .. import magic_async_types


class AsyncHiExMagic:
    """
    Асинхронна (магічна) бібліотека для роботи з api.hiex.io
    """
    __connector: AsyncHiExConnector

    def __init__(self, private_key, public_key):
        self.__connector = AsyncHiExConnector(private_key, public_key)

    def get_connector(self):
        return self.__connector

    async def pairs_list(self, currency1=None, currency2=None):
        """
        Отримати список валютних пар

        :param currency1: Валюта яку купуємо
        :param currency2: Валюта яку продаємо

        :return: list[Pair]
        """
        o = await self.__connector.pairs_list(currency1, currency2)
        return [magic_async_types.Pair(self.__connector, **i.get_dict()) for i in o]

    async def user_get(self, auth_key):
        """
        Завантажити користувача

        :param auth_key: Ключ користувача

        :return: User
        """
        o = await self.__connector.user_get(auth_key)
        return magic_async_types.User(self.__connector, auth_key, **o.get_dict())

    async def user_referrals(self, auth_key, limit=None, offset=None):
        """
        Завантажити список рефералів

        :param auth_key: Ключ користувача
        :param limit: Скільки рефералів завантажувати
        :param offset: Починати з рядку

        :return: list
        """
        return await self.__connector.user_referrals(auth_key, limit, offset)

    async def user_logout(self, auth_key):
        """
        Розлогінити користувача (деактивувати auth_key в системі)

        :param auth_key: Ключ користувача

        :return: User
        """
        return await self.__connector.user_logout(auth_key)

    async def user_kyc_get(self, auth_key):
        """
        Отримати лінк для проходження KYC (верифікації)

        :param auth_key: Ключ користувача

        :return: str
        """
        return await self.__connector.user_kyc_get(auth_key)

    async def user_auth(self, email, referral_token=None):
        """
        Запит на авторизацію користувача

        :param email: Пошта користувача
        :param referral_token: Реферальний токен

        :return: Auth
        """
        o = await self.__connector.user_auth(email, referral_token)
        return magic_async_types.Auth(self.__connector, **o.get_dict())

    async def user_auth_code(self, auth_key, code):
        """
        Реєстрація коду авторизації

        :param auth_key: Ключ користувача
        :param code: Код, який користвувач отримав на пошту

        :return: Auth
        """
        o = await self.__connector.user_auth_code(auth_key, code)
        return magic_async_types.Auth(self.__connector, **o.get_dict())

    async def user_exchanges_history(self, auth_key, limit=None, offset=None, group=None):
        """
        Отримати список обмінів користувача (за вибіркою)

        :param auth_key: Ключ користувача
        :param limit: Скільки обмінів завантажувати
        :param offset: Починати з рядку
        :param group: Група обмінів (cancel, in_process, success)


        :return: list[Exchange]
        """
        o = await self.__connector.user_exchanges_history(auth_key, limit, offset, group)
        return [magic_async_types.Exchange(self.__connector, auth_key, **i.get_dict()) for i in o]

    async def user_data_get(self, auth_key):
        """
        Отримання даних додатку

        :param auth_key: Ключ користувача

        :return:
        """
        return await self.__connector.user_data_get(auth_key)

    async def user_data_set(self, auth_key, **kwargs):
        """
        Запис даних додатку

        :param auth_key: Ключ користувача
        :param kwargs: Аргументи які потрібно зберегти

        :return:
        """
        return await self.__connector.user_data_set(auth_key, **kwargs)

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
        o = await self.__connector.exchange_create(auth_key, currency1, currency2, address, tag, amount1, amount2, return_url)
        return magic_async_types.Exchange(self.__connector, auth_key, **o.get_dict())

    async def exchange_confirm(self, auth_key, exchange_id):
        """
        Підтвердження обміну

        :param auth_key: Ключ користувача
        :param exchange_id: Номер обміну

        :return: Exchange
        """
        o = await self.__connector.exchange_confirm(auth_key, exchange_id)
        return magic_async_types.Exchange(self.__connector, auth_key, **o.get_dict())

    async def exchange_details(self, exchange_id, auth_key=None):
        """
        Отримати інформацію по обміну.
        Важливо! Для магічного exchange_details потрібен auth_key.
        Це потрібно для підтвердження і відміни обмінів
        Якщо магічний тип не використовується, то auth_key=None

        :param auth_key: Ключ користувача
        :param exchange_id: Номер обміну

        :return: Exchange
        """
        if auth_key:
            o = await self.__connector.exchange_details(exchange_id)
            return magic_async_types.Exchange(self.__connector, auth_key, **o.get_dict())
        else:
            return await self.__connector.exchange_details(exchange_id)

    async def exchange_cancel(self, auth_key, exchange_id):
        """
        Відмінити обмін

        :param auth_key: Ключ користувача
        :param exchange_id: Номер обміну

        :return: Exchange
        """
        return await self.__connector.exchange_cancel(auth_key, exchange_id)

    async def application_exchanges_get(self, user_id=None, limit=None, offset=None, group=None):
        """
        Отримати список обмінів додатку (за вибіркою)
        Нюанс: цей метод повертає ЗВИЧАЙНИЙ тип Exchange

        :param user_id: Номер користувача
        :param limit: Скільки обмінів завантажувати
        :param offset: Починати з рядку
        :param group: Група обмінів (cancel, in_process, success)


        :return: list[Exchange]
        """
        return await self.__connector.application_exchanges_get(user_id, limit, offset, group)

    async def application_stats_get(self, limit=None, offset=None):
        """
        Завантажити статистику (за вибіркою)

        :param limit: Кількість днів
        :param offset: Скільки останніх днів пропустити

        :return: list[Stat]
        """
        o = await self.__connector.application_stats_get(limit, offset)
        return [magic_async_types.Stat(self.__connector, **i.get_dict()) for i in o]

    async def application_details(self):
        """
        Отримати інформацію про додаток

        :return: Application
        """
        o = await self.__connector.application_details()
        return magic_async_types.Application(self.__connector, **o.get_dict())

    async def application_interest_set(self, interest):
        """
        Змінити % від обмінів

        :param interest: % від обмінів

        :return: Decimal
        """
        return await self.__connector.application_interest_set(interest)
