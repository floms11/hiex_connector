from aiohttp.web import run_app
from aiohttp.web_app import Application
from aiohttp.web_request import Request
from aiohttp.web_response import json_response

from ..async_connector import AsyncHiExConnector
from ..types import Exchange, User


class AsyncHiExNotifications:
    """
    Клас створений для обробки подій (сповіщень) від hiex.io
    Для використання достаньо ініціювати клас, передавши асинхронний конектор та обробники,
    які створені на основі AsyncHiExBaseUpdate

    Також є можливість використувати користувацький сервер.
    Для виклику обробників достатньо викликати update_user_handlers під час події
    """
    connector: AsyncHiExConnector
    handlers: list
    host: str
    port: int
    url: str

    def __init__(
            self,
            connector,
            handlers: list,
            host: str = '0.0.0.0',
            port: int = 8265,
            url: str = '/'):
        if isinstance(connector, AsyncHiExConnector):
            self.connector = connector
        else:
            ValueError('connector not AsyncHiExConnector')
        self.host = host
        self.port = port
        self.url = url
        self.handlers = handlers

        app = Application()
        app.router.add_get(self.url, self.app_handler)
        app.router.add_post(self.url, self.app_handler)
        run_app(app, host=self.host, port=self.port)

    async def app_handler(self, request: Request):
        await self.update_user_handlers(self.connector, await request.text(), request.headers, *self.handlers)
        return json_response({"ok": True})

    @staticmethod
    async def update_user_handlers(connector: AsyncHiExConnector, request_data: str, headers, *handlers):
        data = connector.get_valid_response(request_data, headers)
        for handler in handlers:
            if data['method'] == 'exchange_update' and issubclass(handler, AsyncHiExExchangeUpdate):
                exchange = Exchange(**data['exchange'])
                h = handler(connector, exchange)
                await h.handle()
            elif data['method'] == 'user_kyc_reviewed' and issubclass(handler, AsyncHiExUserKYCReviewed):
                user = User(**data['user'])
                h = handler(connector, user)
                await h.handle()


class AsyncHiExBaseUpdate:
    connector: AsyncHiExConnector

    def __init__(self, connector: AsyncHiExConnector):
        self.connector = connector

    async def handle(self):
        pass


class AsyncHiExExchangeUpdate(AsyncHiExBaseUpdate):
    exchange: Exchange

    def __init__(self, connector: AsyncHiExConnector, exchange: Exchange):
        super().__init__(connector)
        self.exchange = exchange

    async def handle(self):
        pass


class AsyncHiExUserKYCReviewed(AsyncHiExBaseUpdate):
    user: User

    def __init__(self, connector: AsyncHiExConnector, user: User):
        super().__init__(connector)
        self.user = user

    async def handle(self):
        pass
