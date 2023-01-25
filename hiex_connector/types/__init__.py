from decimal import Decimal


class ResponseList(list):
    is_all: bool = False


class BaseType:
    def __repr__(self):
        return (
            f"<{self.__class__.__name__} values: "
            + ";".join([f"{key}={self[key]}" for key in self.__dict__.keys()])
            + ">"
        )

    def __getitem__(self, item):
        return getattr(self, item)

    def get_dict(self):
        keys = self.__dict__.keys()
        return {key: self[key] for key in keys}


class Currency(BaseType):
    code: str
    img: str
    deposit_merchant: str
    withdrawal_merchant: str
    available_tag: bool
    kyc_required: bool
    min_deposit: Decimal
    max_deposit: Decimal
    min_withdrawal: Decimal
    max_withdrawal: Decimal
    fee_withdrawal: Decimal
    round_ndigits: int

    def __init__(self, **kwargs):
        self.code = kwargs['code']
        self.img = kwargs['img']
        self.deposit_merchant = kwargs['deposit_merchant']
        self.withdrawal_merchant = kwargs['withdrawal_merchant']
        self.available_tag = kwargs['available_tag']
        self.kyc_required = kwargs['kyc_required']
        self.min_deposit = Decimal(kwargs['min_deposit'])
        self.max_deposit = Decimal(kwargs['max_deposit'])
        self.min_withdrawal = Decimal(kwargs['min_withdrawal'])
        self.max_withdrawal = Decimal(kwargs['max_withdrawal'])
        self.fee_withdrawal = Decimal(kwargs['fee_withdrawal'])
        self.round_ndigits = kwargs['round_ndigits']


class AdditionalFields(BaseType):
    beneficiary_first_name: str
    beneficiary_last_name: str
    beneficiary_tin: str
    beneficiary_phone: str

    def __init__(self, **kwargs):
        self.beneficiary_first_name = kwargs['beneficiary_first_name']
        self.beneficiary_last_name = kwargs['beneficiary_last_name']
        self.beneficiary_tin = kwargs['beneficiary_tin']
        self.beneficiary_phone = kwargs['beneficiary_phone']


class Payment(BaseType):
    unique_id: str
    status: int
    currency: Currency
    address: str
    address_qr: str
    tag: str
    amount: Decimal
    available_amount: Decimal
    url: str
    merchant: str
    additional_fields: AdditionalFields
    data_create: dict
    data_status: dict
    created_at: int
    closed_at: int

    def __init__(self, **kwargs):
        self.unique_id = kwargs['unique_id']
        self.status = kwargs['status']
        self.address = kwargs['address']
        self.address_qr = kwargs['address_qr']
        self.tag = kwargs['tag']
        self.amount = Decimal(kwargs['amount'])
        self.available_amount = Decimal(kwargs['available_amount'])
        self.url = kwargs['url']
        self.merchant = kwargs['merchant']
        self.data_create = kwargs['data_create']
        self.data_status = kwargs['data_status']
        self.created_at = kwargs['created_at']
        self.closed_at = kwargs['closed_at']

        if isinstance(kwargs['currency'], Currency):
            self.currency = kwargs['currency']
        else:
            self.currency = Currency(**kwargs['currency'])

        if isinstance(kwargs['additional_fields'], AdditionalFields):
            self.additional_fields = kwargs['additional_fields']
        else:
            self.additional_fields = AdditionalFields(**kwargs['additional_fields'])


class Withdrawal(BaseType):
    unique_id: str
    status: int
    currency: Currency
    address: str
    tag: str
    amount: Decimal
    amount_processed: Decimal
    merchant: str
    additional_fields: AdditionalFields
    data_create: dict
    data_status: dict
    created_at: int

    def __init__(self, **kwargs):
        self.unique_id = kwargs['unique_id']
        self.status = kwargs['status']
        self.address = kwargs['address']
        self.tag = kwargs['tag']
        self.amount = Decimal(kwargs['amount'])
        self.amount_processed = Decimal(kwargs['amount_processed'])
        self.merchant = kwargs['merchant']
        self.data_create = kwargs['data_create']
        self.data_status = kwargs['data_status']
        self.created_at = kwargs['created_at']

        if isinstance(kwargs['currency'], Currency):
            self.currency = kwargs['currency']
        else:
            self.currency = Currency(**kwargs['currency'])

        if isinstance(kwargs['additional_fields'], AdditionalFields):
            self.additional_fields = kwargs['additional_fields']
        else:
            self.additional_fields = AdditionalFields(**kwargs['additional_fields'])


class Exchange(BaseType):
    exchange_id: str
    application_id: int
    user_id: int
    status: int
    amount1: Decimal
    amount2: Decimal
    amount_usdt: Decimal
    currency1: Currency
    currency2: Currency
    address: str
    tag: str
    additional_fields: AdditionalFields
    created_at: int
    closed_at: int
    referral_income: Decimal
    application_income: Decimal
    application_interest: Decimal
    return_url: str

    def __init__(self, **kwargs):
        self.exchange_id = kwargs['exchange_id']
        self.application_id = kwargs['application_id']
        self.user_id = kwargs['user_id']
        self.status = kwargs['status']
        self.amount1 = Decimal(kwargs['amount1'])
        self.amount2 = Decimal(kwargs['amount2'])
        self.amount_usdt = Decimal(kwargs['amount_usdt'])
        self.address = kwargs['address']
        self.tag = kwargs['tag']
        self.created_at = kwargs['created_at']
        self.closed_at = kwargs['closed_at']
        self.referral_income = Decimal(kwargs['referral_income']) if kwargs['referral_income'] else None
        self.application_income = Decimal(kwargs['application_income']) if kwargs['application_income'] else None
        self.application_interest = Decimal(kwargs['application_interest']) if kwargs['application_interest'] else None
        self.return_url = kwargs['return_url']

        if isinstance(kwargs['currency1'], Currency):
            self.currency1 = kwargs['currency1']
        else:
            self.currency1 = Currency(**kwargs['currency1'])

        if isinstance(kwargs['currency2'], Currency):
            self.currency2 = kwargs['currency2']
        else:
            self.currency2 = Currency(**kwargs['currency2'])

        if isinstance(kwargs['additional_fields'], AdditionalFields):
            self.additional_fields = kwargs['additional_fields']
        else:
            self.additional_fields = AdditionalFields(**kwargs['additional_fields'])


class Pair(BaseType):
    currency1: Currency
    currency2: Currency
    min_amount1: Decimal
    max_amount1: Decimal
    min_amount2: Decimal
    max_amount2: Decimal
    price_factor: Decimal
    price: Decimal
    comment: str
    active: bool
    interest: Decimal
    kyc_required: bool
    available_tag: bool
    additional_fields_list: list
    swap_deposit: bool
    last_update: int
    currency_swap_auxiliary: Currency = None

    def __init__(self, **kwargs):
        self.min_amount1 = Decimal(kwargs['min_amount1'])
        self.max_amount1 = Decimal(kwargs['max_amount1'])
        self.min_amount2 = Decimal(kwargs['min_amount2'])
        self.max_amount2 = Decimal(kwargs['max_amount2'])
        self.price_factor = Decimal(kwargs['price_factor'])
        self.price = Decimal(kwargs['price'])
        self.comment = kwargs['comment']
        self.active = kwargs['active']
        self.interest = Decimal(kwargs['interest'])
        self.kyc_required = kwargs['kyc_required']
        self.available_tag = kwargs['available_tag']
        self.additional_fields_list = kwargs['additional_fields_list']
        self.swap_deposit = kwargs['swap_deposit']
        self.last_update = kwargs['last_update']

        if isinstance(kwargs['currency1'], Currency):
            self.currency1 = kwargs['currency1']
        else:
            self.currency1 = Currency(**kwargs['currency1'])
        if isinstance(kwargs['currency2'], Currency):
            self.currency2 = kwargs['currency2']
        else:
            self.currency2 = Currency(**kwargs['currency2'])
        if kwargs['currency_swap_auxiliary'] is not None:
            if isinstance(kwargs['currency_swap_auxiliary'], Currency):
                self.currency_swap_auxiliary = kwargs['currency_swap_auxiliary']
            else:
                self.currency_swap_auxiliary = Currency(**kwargs['currency_swap_auxiliary'])


class Stat(BaseType):
    day: str
    exchanges_created_count: int
    exchanges_success_count: int
    exchanges_success_amount: Decimal
    application_income: Decimal

    def __init__(self, **kwargs):
        self.day = kwargs['day']
        self.exchanges_created_count = kwargs['exchanges_created_count']
        self.exchanges_success_count = kwargs['exchanges_success_count']
        self.exchanges_success_amount = kwargs['exchanges_success_amount']
        self.application_income = Decimal(kwargs['application_income'])


class User(BaseType):
    user_id: int
    kyc: bool
    email: str
    first_name: str
    last_name: str
    created_at: int
    balance: Decimal = 0
    referral_token: str = None
    referral_id: int = None
    application_id: int = None
    referrals_count: int = None
    referrals_sum_amount: Decimal = None
    data = {}

    def __init__(self, **kwargs):
        self.user_id = kwargs['user_id']
        self.kyc = kwargs['kyc']
        self.email = kwargs['email']
        self.first_name = kwargs['first_name']
        self.last_name = kwargs['last_name']
        self.created_at = kwargs['created_at']
        self.balance = Decimal(kwargs['balance'])
        self.referral_token = kwargs['referral_token']
        self.referral_id = kwargs['referral_id']
        self.application_id = kwargs['application_id']
        self.data = kwargs['data']
        self.referrals_count = kwargs['referrals_count']
        self.referrals_sum_amount = Decimal(kwargs['referrals_sum_amount'])


class Referral(BaseType):
    user_id: int
    email: str
    kyc: bool
    created_at: int
    amount: Decimal = 0

    def __init__(self, **kwargs):
        self.user_id = kwargs['user_id']
        self.email = kwargs['email']
        self.kyc = kwargs['kyc']
        self.created_at = kwargs['created_at']
        self.amount = Decimal(kwargs['amount'])


class UserAuth(BaseType):
    allow: bool
    auth_key: str
    application_id: int
    user_id: int
    code: int
    code_attempt: int

    def __init__(self, **kwargs):
        self.allow = kwargs['allow']
        self.auth_key = kwargs['auth_key']
        self.application_id = kwargs['application_id']
        self.user_id = kwargs['user_id']
        self.code = kwargs['code']
        self.code_attempt = kwargs['code_attempt']


class Log(BaseType):
    name: str
    filesize: int

    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.filesize = kwargs['filesize']


class Application(BaseType):
    application_id: int
    user_id: int
    name: str
    private_key: str
    public_key: str
    interest: Decimal
    balance: Decimal
    notification_url: str
    available_methods: list

    def __init__(self, **kwargs):
        self.application_id = kwargs['application_id']
        self.user_id = kwargs['user_id']
        self.name = kwargs['name']
        self.private_key = kwargs['private_key']
        self.public_key = kwargs['public_key']
        self.interest = Decimal(kwargs['interest'])
        self.balance = Decimal(kwargs['balance'])
        self.notification_url = kwargs['notification_url']
        self.available_methods = kwargs['available_methods']
