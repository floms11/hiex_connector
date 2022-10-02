from decimal import Decimal

from hiex_connector.async_connector import AsyncHiExConnector
from hiex_connector import types


class Pair(types.Pair):
    __connector: AsyncHiExConnector

    def __init__(self, connector: AsyncHiExConnector, **kwargs):
        super().__init__(**kwargs)
        self.__connector = connector


class User(types.User):
    __connector: AsyncHiExConnector
    __auth_key: str

    def __init__(self, connector: AsyncHiExConnector, auth_key: str, **kwargs):
        super().__init__(**kwargs)
        self.__connector = connector
        self.__auth_key = auth_key

    async def reload(self):
        o = await self.__connector.user_get(self.__auth_key)
        super().__init__(**o.get_dict())
        return True

    async def exchanges_history(self, limit=None, start=None, group=None):
        o = await self.__connector.user_exchanges_history(self.__auth_key, limit, start, group)
        return [Exchange(self.__connector, self.__auth_key, **i.get_dict()) for i in o]

    async def exchange(self, exchange_id):
        o = await self.__connector.exchange_details(self.__auth_key, exchange_id)
        return Exchange(self.__connector, self.__auth_key, **o.get_dict())

    async def exchange_create(self, pair: Pair, address: str, tag: str = None, amount1: Decimal = None, amount2: Decimal = None):
        o = await self.__connector.exchange_create(
            self.__auth_key,
            pair.currency1,
            pair.currency2,
            address,
            tag,
            amount1,
            amount2,
        )
        return Exchange(self.__connector, self.__auth_key, **o.get_dict())

    async def data_set(self, **kwargs):
        await self.__connector.user_data_set(self.__auth_key, **kwargs)
        return True

    async def data_get(self, key=None):
        return await self.__connector.user_data_get(self.__auth_key, key)


class UserAuth(types.UserAuth):
    __connector: AsyncHiExConnector

    def __init__(self, connector: AsyncHiExConnector, **kwargs):
        super().__init__(**kwargs)
        self.__connector = connector

    async def code(self, code=None):
        o = await self.__connector.user_auth_code(self.auth_key, code)
        super().__init__(**o.get_dict())

    async def user(self):
        o = await self.__connector.user_get(self.auth_key)
        return User(self.__connector, self.auth_key, **o.get_dict())


class Exchange(types.Exchange):
    __connector: AsyncHiExConnector
    __auth_key: str

    def __init__(self, connector: AsyncHiExConnector, auth_key: str, **kwargs):
        super().__init__(**kwargs)
        self.__connector = connector
        self.__auth_key = auth_key

    async def user(self):
        o = await self.__connector.user_get(self.__auth_key)
        return User(self.__connector, self.__auth_key, **o.get_dict())

    async def reload(self):
        o = await self.__connector.exchange_details(self.__auth_key, self.exchange_id)
        super().__init__(**o.get_dict())
        return True

    async def confirm(self):
        o = await self.__connector.exchange_confirm(self.__auth_key, self.exchange_id)
        super().__init__(**o.get_dict())
        return True

    async def cancel(self):
        return await self.__connector.exchange_cancel(self.__auth_key, self.exchange_id)


class Application(types.Application):
    __connector: AsyncHiExConnector

    def __init__(self, connector: AsyncHiExConnector, **kwargs):
        super().__init__(**kwargs)
        self.__connector = connector


class Stat(types.Stat):
    __connector: AsyncHiExConnector

    def __init__(self, connector: AsyncHiExConnector, **kwargs):
        super().__init__(**kwargs)
        self.__connector = connector
