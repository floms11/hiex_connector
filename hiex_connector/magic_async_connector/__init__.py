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

    async def user_kyc_get(self, auth_key):
        """
        Отримати лінк для проходження KYC (верифікації)

        :param auth_key: Ключ користувача

        :return: str
        """
        return await self.__connector.user_kyc_get(auth_key)

    async def user_auth(self, email):
        """
        Запит на авторизацію користувача

        :param email: Пошта користувача

        :return: Auth
        """
        o = await self.__connector.user_auth(email)
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

    async def user_exchanges_history(self, auth_key, limit=None, start=None, group=None):
        """
        Отримати список обмінів користувача (за вибіркою)

        :param auth_key: Ключ користувача
        :param limit: Скільки обмінів завантажувати
        :param start: З якого обміну почати завантажувати
        :param group: Група обмінів (cancel, in_process, success)


        :return: list[Exchange]
        """
        o = await self.__connector.user_exchanges_history(auth_key, limit, start, group)
        return [magic_async_types.Exchange(self.__connector, auth_key, **i.get_dict()) for i in o]

    async def user_data_get(self, auth_key, param=None):
        """
        Отримання даних додатку

        :param auth_key: Ключ користувача
        :param param: Значення яке потрібно завантажити

        :return:
        """
        return await self.__connector.user_data_get(auth_key, param)

    async def user_data_set(self, auth_key, **kwargs):
        """
        Запис даних додатку

        :param auth_key: Ключ користувача
        :param kwargs: Аргументи які потрібно зберегти

        :return:
        """
        return await self.__connector.user_data_set(auth_key, **kwargs)

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
        o = await self.__connector.exchange_create(auth_key, currency1, currency2, address, tag, amount1, amount2)
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

    async def exchange_details(self, auth_key, exchange_id):
        """
        Отримати інформацію по обміну

        :param auth_key: Ключ користувача
        :param exchange_id: Номер обміну

        :return: Exchange
        """
        o = await self.__connector.exchange_details(auth_key, exchange_id)
        return magic_async_types.Exchange(self.__connector, auth_key, **o.get_dict())

    async def exchange_cancel(self, auth_key, exchange_id):
        """
        Відмінити обмін

        :param auth_key: Ключ користувача
        :param exchange_id: Номер обміну

        :return: Exchange
        """
        return await self.__connector.exchange_cancel(auth_key, exchange_id)

    async def application_exchanges_get(self, user_id=None, limit=None, start=None, group=None):
        """
        Отримати список обмінів додатку (за вибіркою)
        Нюанс: цей метод повертає ЗВИЧАЙНИЙ тип Exchange

        :param user_id: Номер користувача
        :param limit: Скільки обмінів завантажувати
        :param start: З якого обміну почати завантажувати
        :param group: Група обмінів (cancel, in_process, success)


        :return: list[Exchange]
        """
        return await self.__connector.application_exchanges_get(user_id, limit, start, group)

    async def application_stats_get(self, start_time=None, end_time=None, count=None):
        """
        Завантажити статистику (за вибіркою)

        :param start_time: З якого часу завантажувати (в UNIX time)
        :param end_time: До якого часу завантажувати (в UNIX time)
        :param count: Кількість днів

        :return: list[Stat]
        """
        o = await self.__connector.application_stats_get(start_time, end_time, count)
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
