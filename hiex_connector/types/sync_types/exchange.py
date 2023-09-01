from .base import *


class SyncExchange(SyncBase, Exchange):
    def reload(self):
        """
        Оновити інформацію обміну

        :return: bool
        """
        o = self.connector.exchange_get(self.exchange_id)
        super().__init__(**o.get_dict())
        return True

    def payment(self):
        """
        Отримати реквізити для сплати обміну

        :return: Payment
        """
        return self.connector.exchange_payment_get(self.exchange_id)

    def cancel(self):
        """
        Відмінити обмін

        :return: bool
        """
        return self.connector.exchange_cancel(self.exchange_id)


class SyncExchangeWithAuthKey(BaseWithAuthKey, SyncExchange):
    def reload(self):
        """
        Оновити інформацію обміну

        :return: bool
        """
        o = self.connector.exchange_get(self.exchange_id, auth_key=self.auth_key)
        super().__init__(**o.get_dict())
        return True

    def user(self):
        """
        Завантажити користувача

        :return: User
        """
        return self.connector.user_get(self.auth_key)

    def cancel(self):
        """
        Відмінити обмін

        :return: bool
        """
        return self.connector.user_exchange_cancel(self.auth_key, self.exchange_id)
