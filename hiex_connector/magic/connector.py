from hiex_connector.async_connector import AsyncHiExConnector
from hiex_connector.magic import types


class AsyncHiEx:
    __connector: AsyncHiExConnector

    def __init__(self, private_key, public_key):
        self.__connector = AsyncHiExConnector(private_key, public_key)

    async def pairs_list(self, currency1=None, currency2=None):
        o = await self.__connector.pairs_list(currency1, currency2)
        return [types.Pair(self.__connector, **i.get_dict()) for i in o]

    async def user_get(self, auth_key):
        o = await self.__connector.user_get(auth_key)
        return types.User(self.__connector, auth_key, **o.get_dict())

    async def user_auth(self, email):
        o = await self.__connector.user_auth(email)
        return types.UserAuth(self.__connector, **o.get_dict())

    async def user_auth_code(self, auth_key, code):
        o = await self.__connector.user_auth_code(auth_key, code)
        return types.UserAuth(self.__connector, **o.get_dict())

    async def user_exchanges_history(self, auth_key, limit=None, start=None, group=None):
        o = await self.__connector.user_exchanges_history(auth_key, limit, start, group)
        return [types.Exchange(self.__connector, auth_key, **i.get_dict()) for i in o]

    async def user_data_get(self, auth_key, param=None):
        return await self.__connector.user_data_get(auth_key, param)

    async def user_data_set(self, auth_key, **kwargs):
        return await self.__connector.user_data_set(auth_key, **kwargs)

    async def exchange_create(self, auth_key, currency1, currency2, address, tag=None, amount1=None, amount2=None):
        o = await self.__connector.exchange_create(auth_key, currency1, currency2, address, tag, amount1, amount2)
        return types.Exchange(self.__connector, auth_key, **o.get_dict())

    async def exchange_confirm(self, auth_key, exchange_id):
        o = await self.__connector.exchange_confirm(auth_key, exchange_id)
        return types.Exchange(self.__connector, auth_key, **o.get_dict())

    async def exchange_details(self, auth_key, exchange_id):
        o = await self.__connector.exchange_details(auth_key, exchange_id)
        return types.Exchange(self.__connector, auth_key, **o.get_dict())

    async def exchange_cancel(self, auth_key, exchange_id):
        return await self.__connector.exchange_cancel(auth_key, exchange_id)

    async def application_exchanges_get(self, user_id=None, limit=None, start=None, group=None):
        """
        Отут ВАЖЛИВО. Тип звичайний
        :param user_id:
        :param limit:
        :param start:
        :param group:
        :return:
        """
        return await self.__connector.application_exchanges_get(user_id, limit, start, group)

    async def application_stats_get(self, start_time=None, end_time=None, count=None):
        o = await self.__connector.application_stats_get(start_time, end_time, count)
        return [types.Stat(self.__connector, **i.get_dict()) for i in o]

    async def application_details(self):
        o = await self.__connector.application_details()
        return types.Application(self.__connector, **o.get_dict())

    async def application_interest_set(self, interest):
        return await self.__connector.application_interest_set(interest)
