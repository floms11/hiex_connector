from ..base import HiExConnectorBase
from ..types import *


class HiExConnector(HiExConnectorBase):
    """
    Синхронна бібліотека для роботи з api.hiex.io
    """
    def admin_currencies_list(self):
        """
        Отримати список монет, які зараз підтримує система

        :return: Currency
        """
        resp = self.get_request('admin/currencies/list', {})
        currencies = ResponseList()
        currencies.is_all = resp['is_all']
        for currency in resp['currencies']:
            currencies.append(Currency(**currency))
        return currencies

    def admin_exchange_update(self, exchange_id, status: int = Empty):
        """
        Редагувати обмін

        :param exchange_id: Номер обміну
        :param status: Статус який потрібно встановити на обмін

        :return: Exchange
        """
        resp = self.get_request('admin/exchange/update', {
            'exchange_id': exchange_id,
            'status': status,
        })
        return Exchange(**resp['exchange'])

    def admin_exchange_get(self, exchange_id):
        """
        Отримати обмін

        :param exchange_id: Номер обміну

        :return: Exchange
        """
        resp = self.get_request('admin/exchange/get', {
            'exchange_id': exchange_id,
        })
        return Exchange(**resp['exchange'])

    def admin_exchanges_list(self, application_id=Empty, user_id=Empty, limit=Empty, offset=Empty, status_list=Empty, short_exchange_id=Empty):
        """
        Отримати список обмінів (за вибіркою)

        :param application_id: Номер додатку
        :param user_id: Номер користувача
        :param limit: Скільки обмінів завантажувати
        :param offset: Починати з рядку
        :param status_list: Статуси обмінів
        :param short_exchange_id: Перші символи з exchange_id

        :return: list[Exchange]
        """
        resp = self.get_request('admin/exchanges/list', {
            'application_id': application_id,
            'user_id': user_id,
            'limit': limit,
            'offset': offset,
            'status_list': status_list,
            'short_exchange_id': short_exchange_id,
        })
        exchanges = ResponseList()
        exchanges.is_all = resp['is_all']
        for exchange in resp['exchanges']:
            exchanges.append(Exchange(**exchange))
        return exchanges

    def admin_payment_get(self, payment_id):
        """
        Отримати обмін

        :param payment_id: Ідентифікатор оплати

        :return: Payment
        """
        resp = self.get_request('admin/payment/get', {
            'payment_id': payment_id,
        })
        return Payment(**resp['payment'])

    def admin_withdrawal_get(self, withdrawal_id):
        """
        Отримати виплату

        :param withdrawal_id: Ідентифікатор виплати

        :return: Withdrawal
        """
        resp = self.get_request('admin/withdrawal/get', {
            'withdrawal_id': withdrawal_id,
        })
        return Withdrawal(**resp['withdrawal'])

    def admin_logs_list(self):
        """
        Отримати список логів

        :return: list[Log]
        """
        resp = self.get_request('admin/logs/list', {
        })
        logs = ResponseList()
        logs.is_all = resp['is_all']
        for log in resp['logs']:
            logs.append(Log(**log))
        return logs

    def admin_logs_get(self, name):
        """
        Завантажити лог (за ім'ям)

        :param name: Ім'я логу

        :return: str
        """
        resp = self.get_request_data('admin/logs/get', {
            'name': name
        })
        return resp[0]

    def admin_stats_list(self, application_id=Empty, limit=Empty, offset=Empty):
        """
        Завантажити статистику (за вибіркою)

        :param application_id: Номер додатку
        :param limit: Кількість днів
        :param offset: Скільки останніх днів пропустити

        :return: list[Stat]
        """
        resp = self.get_request('admin/stats/list', {
            'application_id': application_id,
            'limit': limit,
            'offset': offset,
        })
        stats = ResponseList()
        stats.is_all = resp['is_all']
        for stat in resp['stats']:
            stats.append(Stat(**stat))
        return stats

    def admin_applications_list(self, user_id=Empty, limit=Empty, offset=Empty):
        """
        Завантажити список додатків у системі

        :param user_id: ID власника додатку
        :param limit: Скільки обмінів завантажувати
        :param offset: Починати з рядку

        :return: list[Application]
        """
        resp = self.get_request('admin/applications/list', {
            'user_id': user_id,
            'limit': limit,
            'offset': offset,
        })
        applications = ResponseList()
        applications.is_all = resp['is_all']
        for application in resp['applications']:
            applications.append(Application(**application))
        return applications

    def admin_application_create(self, name, available_methods, interest, user_id):
        """
        Створити новий додаток

        :param name: Ім'я додатку
        :param available_methods: Список методів, які будуть доступні додатку
        :param interest: % від обмінів
        :param user_id: ID власника додатку

        :return: Application
        """
        resp = self.get_request('admin/application/create', {
            'name': name,
            'available_methods': available_methods,
            'interest': interest,
            'user_id': user_id,
        })
        return Application(**resp['application'])

    def admin_application_get(self, application_id):
        """
        Завантажити інформацію додатку

        :param application_id: Номер додатку

        :return: Application
        """
        resp = self.get_request('admin/application/get', {
            'application_id': application_id,
        })
        return Application(**resp['application'])

    def admin_application_delete(self, application_id):
        """
        Видалити додаток

        :param application_id: Номер додатку

        :return: bool
        """
        self.get_request('admin/application/delete', {
            'application_id': application_id,
        })
        return True

    def admin_application_update(self, application_id, available_methods=Empty, balance=Empty, interest=Empty, update_keys=Empty, name=Empty, notification_url=Empty, user_id=Empty):
        """
        Редагувати додаток

        :param application_id: Номер додатку
        :param available_methods: Список методів, які будуть доступні додатку
        :param balance: Кількість грошей на рахунку додатку
        :param interest: % від обмінів
        :param update_keys: True, якщо потрібно згенерувати нові ключі
        :param name: Ім'я додатку
        :param notification_url: URL для отримання сповіщень
        :param user_id: ID власника додатку

        :return: Application
        """
        resp = self.get_request('admin/application/update', {
            'application_id': application_id,
            'available_methods': available_methods,
            'balance': balance,
            'interest': interest,
            'update_keys': update_keys,
            'name': name,
            'notification_url': notification_url,
            'user_id': user_id,
        })
        return Application(**resp['application'])

    def admin_pairs_list(self, currency1=Empty, currency2=Empty):
        """
        Отримати список доступних пар обміну

        :param currency1: Валюта яку купуємо
        :param currency2: Валюта яку продаємо

        :return: list[Pair]
        """
        resp = self.get_request('admin/pairs/list', {
            'currency1': currency1,
            'currency2': currency2,
        })
        pairs = ResponseList()
        pairs.is_all = resp['is_all']
        for pair in resp['pairs']:
            pairs.append(Pair(**pair))
        return pairs

    def admin_pair_create(self, currency1, currency2, kyc_required, swap_deposit, active=Empty, interest=Empty, max_amount1=Empty, max_amount2=Empty, min_amount1=Empty, min_amount2=Empty, swap_service_info: str = Empty):
        """
        Створити валютну пару

        :param currency1: Валюта яку купуємо
        :param currency2: Валюта яку продаємо
        :param kyc_required: Чи потрібен KYC для обміну
        :param swap_deposit: Чи потрібно робити автоматичний обмін
        :param active: Чи активний обмін
        :param interest: % нашого інтересу
        :param max_amount1: Максимальна сума депозиту
        :param max_amount2: Максимальна сума виплати
        :param min_amount1: Мінімальна сума депозиту
        :param min_amount2: Мінімальна сума виплати
        :param swap_service_info: Інформація про валюти обміну

        :return: Pair
        """
        resp = self.get_request('admin/pair/create', {
            'currency1': currency1,
            'currency2': currency2,
            'swap_service_info': swap_service_info,
            'kyc_required': kyc_required,
            'swap_deposit': swap_deposit,
            'active': active,
            'interest': interest,
            'max_amount1': max_amount1,
            'max_amount2': max_amount2,
            'min_amount1': min_amount1,
            'min_amount2': min_amount2,
        })
        return Pair(**resp['pair'])

    def admin_pair_update(self, currency1, currency2, active=Empty, interest=Empty, max_amount1=Empty, max_amount2=Empty, min_amount1=Empty, min_amount2=Empty, kyc_required=Empty, swap_deposit=Empty, swap_service_info: str = Empty):
        """
        Змінити валютну пару

        :param currency1: Валюта яку купуємо
        :param currency2: Валюта яку продаємо
        :param active: Чи активний обмін
        :param interest: % нашого інтересу
        :param max_amount1: Максимальна сума депозиту
        :param max_amount2: Максимальна сума виплати
        :param min_amount1: Мінімальна сума депозиту
        :param min_amount2: Мінімальна сума виплати
        :param kyc_required: Чи потрібен KYC для обміну
        :param swap_deposit: Чи потрібно робити автоматичний обмін
        :param swap_service_info: Інформація про валюти обміну

        :return: Pair
        """
        resp = self.get_request('admin/pair/update', {
            'currency1': currency1,
            'currency2': currency2,
            'swap_service_info': swap_service_info,
            'active': active,
            'interest': interest,
            'max_amount1': max_amount1,
            'max_amount2': max_amount2,
            'min_amount1': min_amount1,
            'min_amount2': min_amount2,
            'kyc_required': kyc_required,
            'swap_deposit': swap_deposit,
        })
        return Pair(**resp['pair'])

    def admin_pair_delete(self, currency1=Empty, currency2=Empty):
        """
        Видалити валютну пару

        :param currency1: Валюта яку купуємо
        :param currency2: Валюта яку продаємо

        :return: bool
        """
        self.get_request('admin/pair/delete', {
            'currency1': currency1,
            'currency2': currency2,
        })
        return True

    def admin_users_list(self, limit=Empty, offset=Empty):
        """
        Отримати список користувачів (за вибіркою)

        :param limit: Скільки обмінів завантажувати
        :param offset: Починати з рядку

        :return: list[User]
        """
        resp = self.get_request('admin/users/list', {
            'limit': limit,
            'offset': offset,
        })
        users = ResponseList()
        users.is_all = resp['is_all']
        for user in resp['users']:
            users.append(User(**user))
        return users

    def admin_user_get(self, user_id=Empty, email=Empty):
        """
        Отримати інформацію про користувача

        :param user_id: Номер користувача
        :param email: Пошта користувача

        :return: User
        """
        resp = self.get_request('admin/user/get', {
            'user_id': user_id,
            'email': email,
        })
        return User(**resp['user'])

    def admin_user_referrals_list(self, user_id, limit=Empty, offset=Empty):
        """
        Отримати інформацію про рефералів користувача

        :param user_id: Номер користувача
        :param limit: Скільки обмінів завантажувати
        :param offset: Починати з рядку

        :return: list[Referral]
        """
        resp = self.get_request('admin/user/referrals/list', {
            'user_id': user_id,
            'limit': limit,
            'offset': offset,
        })
        referrals = ResponseList()
        referrals.is_all = resp['is_all']
        for referral in resp['referrals']:
            referrals.append(Referral(**referral))
        return referrals

    def admin_user_auth_applications_list(self, user_id):
        """
        Отримати список додатків, з якими взаємодіяв користувач

        :param user_id: Номер користувача

        :return: list[Application]
        """
        resp = self.get_request('admin/user/auth/applications/list', {
            'user_id': user_id,
        })
        applications = ResponseList()
        applications.is_all = resp['is_all']
        for application in resp['applications']:
            applications.append(Application(**application))
        return applications

    def admin_user_update(self, user_id, email=Empty, first_name=Empty, last_name=Empty, kyc=Empty, balance=Empty):
        """
        Змінити інформацію про користувача

        :param user_id: Номер користувача
        :param email: Нова пошта
        :param first_name: Нове ім'я
        :param last_name: Нове прізвище
        :param kyc: KYC
        :param balance: Баланс

        :return: User
        """
        resp = self.get_request('admin/user/update', {
            'user_id': user_id,
            'email': email,
            'first_name': first_name,
            'last_name': last_name,
            'kyc': kyc,
            'balance': balance,
        })
        return User(**resp['user'])

    def admin_setting(self, **kwargs):
        """
        Завантажити/змінити налаштування системи

        :param kwargs: Параметри які потрібно змінити

        :return: dict
        """
        resp = self.get_request('admin/setting', kwargs)
        return resp['hisettings']

    def admin_user_auth_list(self, user_id=Empty, application_id=Empty, limit=Empty, offset=Empty):
        """
        Отримати відправлені коди авторизації

        :param user_id: Номер користувача
        :param application_id: Номер користувача
        :param limit: Скільки обмінів завантажувати
        :param offset: Починати з рядку

        :return: list[UserAuth]
        """
        resp = self.get_request('admin/user/auth/list', {
            'user_id': user_id,
            'application_id': application_id,
            'limit': limit,
            'offset': offset,
        })
        user_auth_list = ResponseList()
        user_auth_list.is_all = resp['is_all']
        for user_auth in resp['user_auth_list']:
            user_auth_list.append(UserAuth(**user_auth))
        return user_auth_list

    def admin_withdrawals_list(self, short_withdrawal_id=Empty, limit=Empty, offset=Empty):
        """
        Отримати список виплат

        :param short_withdrawal_id: Короткий ID виплати
        :param limit: Скільки виплат завантажувати
        :param offset: Починати з рядку

        :return: list[Withdrawal]
        """
        resp = self.get_request('admin/withdrawals/list', {
            'short_withdrawal_id': short_withdrawal_id,
            'limit': limit,
            'offset': offset,
        })
        withdrawals = ResponseList()
        withdrawals.is_all = resp['is_all']
        for withdrawal in resp['withdrawals']:
            withdrawals.append(Withdrawal(**withdrawal))
        return withdrawals

    def admin_withdrawal_create(
            self, currency, address, amount, tag=Empty, description=Empty,
            beneficiary_first_name=Empty, beneficiary_last_name=Empty, beneficiary_tin=Empty, beneficiary_phone=Empty,
    ):
        """
        Створити нову виплату

        :param currency: Код валюти
        :param address: Адреса для виплати
        :param amount: Сума виплати
        :param tag: Тег для виплати
        :param description: Опис виплати
        :param beneficiary_first_name: Ім'я отримувача
        :param beneficiary_last_name: Прізвище отримувача
        :param beneficiary_tin: ЄДРПОУ отримувача
        :param beneficiary_phone: Телефон отримувача

        :return: Withdrawal
        """
        resp = self.get_request('admin/withdrawal/create', {
            'currency': currency,
            'address': address,
            'amount': amount,
            'tag': tag,
            'description': description,
            'beneficiary_first_name': beneficiary_first_name,
            'beneficiary_last_name': beneficiary_last_name,
            'beneficiary_tin': beneficiary_tin,
            'beneficiary_phone': beneficiary_phone,
        })
        return Withdrawal(**resp['withdrawal'])
