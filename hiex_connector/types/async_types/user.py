from .base import *


class AsyncUser(AsyncBase, User):
    pass


class AsyncUserWithAuthKey(BaseWithAuthKey, AsyncUser):
    async def reload(self):
        """
        Оновити інформацію про користувача

        :return: bool
        """
        o = await self.connector.user_get(self.auth_key)
        super().__init__(**o.get_dict())
        return True

    async def referrals(self, limit=Empty, offset=Empty):
        """
        Завантажити список рефералів

        :param limit: Скільки рефералів завантажувати
        :param offset: Починати з рядку

        :return: list
        """
        return await self.connector.user_referrals_list(self.auth_key, limit, offset)

    async def logout(self):
        """
        Розлогінити користувача (деактивувати auth_key в системі)

        :return: bool
        """
        return await self.connector.user_logout(self.auth_key)

    async def kyc_get(self, method, option=Empty, return_url=Empty):
        """
        Отримати лінк для проходження KYC (верифікації)

        :return: Verification
        """
        return await self.connector.user_kyc_get(self.auth_key, method, option, return_url)

    async def kyc_methods_list(self):
        """
        Завантажити можливі способи проходження верифікації

        :return: ResponseList[VerificationService]
        """
        return await self.connector.user_kyc_methods_list(self.auth_key)

    async def exchanges(self, limit=Empty, offset=Empty, status_list=Empty, short_exchange_id=Empty):
        """
        Отримати історію обмінів користувача

        :param limit: Скільки обмінів завантажувати
        :param offset Починати з рядку
        :param status_list: Список статусів
        :param short_exchange_id: Перші символи з exchange_id

        :return:
        """
        return await self.connector.user_exchanges_list(self.auth_key, limit, offset, status_list, short_exchange_id)

    async def exchange(self, exchange_id):
        """
        Завантажити обмін

        :param exchange_id: Номер обміну

        :return: Exchange
        """
        return await self.connector.exchange_get(exchange_id, auth_key=self.auth_key)

    async def exchange_create(
            self, pair: Pair, address: str, tag: str = Empty, amount1: Decimal = Empty, amount2: Decimal = Empty, return_url: str = Empty,
            beneficiary_first_name=Empty, beneficiary_last_name=Empty, beneficiary_tin=Empty, beneficiary_phone=Empty,
    ):
        """
        Створити новий обмін

        :param pair: Валютна пара
        :param address: Адреса на яку потрібно отримати кошти
        :param tag: Тег до адреси (якщо потрібен)
        :param amount1: Сума currency1
        :param amount2: Сума currency2
        :param return_url: URL на який користувач повернеться після оплати карткою
        :param beneficiary_first_name: Інформація по запиту мерчанта. Ім'я отримувача
        :param beneficiary_last_name: Інформація по запиту мерчанта. Прізвище отримувача
        :param beneficiary_tin: Інформація по запиту мерчанта. Номер платника податку отримувача
        :param beneficiary_phone: Інформація по запиту мерчанта. Номер телефону отримувача

        :return: Exchange
        """
        return await self.connector.user_exchange_create(
            self.auth_key,
            pair.currency1.code,
            pair.currency2.code,
            address,
            tag,
            amount1,
            amount2,
            return_url,
            beneficiary_first_name,
            beneficiary_last_name,
            beneficiary_tin,
            beneficiary_phone,
        )

    async def data_save(self, **kwargs):
        """
        Записати дані користувача на серверах hiex.io

        :param kwargs: Зміні які потрібно записати

        :return: bool
        """
        await self.connector.user_data_save(self.auth_key, **kwargs)
        return True
