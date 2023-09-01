from .base import *


class AsyncApplication(AsyncBase, Application):
    async def reload(self):
        """
        Оновити інформацію про додаток

        :return: bool
        """
        o = await self.connector.application_get()
        super().__init__(**o.get_dict())
        return True

    async def stats(self, limit=Empty, offset=Empty):
        """
        Завантажити статистику (за вибіркою)

        :param limit: Кількість днів
        :param offset: Починати з рядку

        :return:
        """
        return await self.connector.application_stats_list(limit, offset)

    async def exchanges(self, limit=Empty, offset=Empty, user_id=Empty, status_list=Empty, short_exchange_id=Empty):
        """
        Отримати історію обмінів додатку

        :param limit: Скільки обмінів завантажувати
        :param offset Починати з рядку
        :param user_id: ID користувача
        :param status_list: Список статусів
        :param short_exchange_id: Перші символи з exchange_id

        :return:
        """
        return await self.connector.application_exchanges_list(limit, offset, user_id, status_list, short_exchange_id)

    async def users(self, limit=Empty, offset=Empty):
        """
        Отримати користувачів додатку

        :param limit: Скільки обмінів завантажувати
        :param offset Починати з рядку

        :return:
        """
        return await self.connector.application_users_list(limit, offset)

    async def interest_set(self, interest):
        """
        Змінити % від обмінів

        :param interest: % від обмінів

        :return: Decimal
        """
        return await self.connector.application_interest_set(interest)
