from .base import *


class AsyncExchange(AsyncBase, Exchange):
    async def reload(self):
        """
        Оновити інформацію обміну

        :return: bool
        """
        o = await self.connector.exchange_get(self.exchange_id)
        super().__init__(**o.get_dict())
        return True

    async def payment(self):
        """
        Отримати реквізити для сплати обміну

        :return: Payment
        """
        return await self.connector.exchange_payment_get(self.exchange_id)

    async def cancel(self):
        """
        Відмінити обмін

        :return: bool
        """
        return await self.connector.exchange_cancel(self.exchange_id)


class AsyncExchangeWithAuthKey(BaseWithAuthKey, AsyncExchange):
    async def reload(self):
        """
        Оновити інформацію обміну

        :return: bool
        """
        o = await self.connector.exchange_get(self.exchange_id, auth_key=self.auth_key)
        super().__init__(**o.get_dict())
        return True

    async def user(self):
        """
        Завантажити користувача

        :return: User
        """
        return await self.connector.user_get(self.auth_key)

    async def cancel(self):
        """
        Відмінити обмін

        :return: bool
        """
        return await self.connector.user_exchange_cancel(self.auth_key, self.exchange_id)
