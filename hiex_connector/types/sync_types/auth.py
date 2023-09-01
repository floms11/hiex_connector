from .base import *


class SyncAuth(SyncBase, Auth):
    def code(self, code=Empty):
        """
        Реєстрація коду авторизації

        :param code: Код з email

        :return:
        """
        o = self.connector.user_auth_code(self.auth_key, code)
        super().__init__(**o.get_dict())

    def user(self):
        """
        Завантажити користувача

        :return: User
        """
        return self.connector.user_get(self.auth_key)
