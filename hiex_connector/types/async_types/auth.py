from .base import *


class AsyncAuth(AsyncBase, Auth):
    async def code(self, code=Empty):
        """
        Реєстрація коду авторизації

        :param code: Код з email

        :return:
        """
        o = await self.connector.user_auth_code(self.auth_key, code)
        super().__init__(**o.get_dict())

    async def user(self):
        """
        Завантажити користувача

        :return: User
        """
        return await self.connector.user_get(self.auth_key)
