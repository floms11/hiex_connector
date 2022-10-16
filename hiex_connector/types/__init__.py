from decimal import Decimal


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
    use_tag: bool
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
        self.use_tag = kwargs['use_tag']
        self.kyc_required = kwargs['kyc_required']
        self.min_deposit = Decimal(kwargs['min_deposit'])
        self.max_deposit = Decimal(kwargs['max_deposit'])
        self.min_withdrawal = Decimal(kwargs['min_withdrawal'])
        self.max_withdrawal = Decimal(kwargs['max_withdrawal'])
        self.fee_withdrawal = Decimal(kwargs['fee_withdrawal'])
        self.round_ndigits = kwargs['round_ndigits']


class Payment(BaseType):
    payment_address: str
    payment_tag: str
    payment_amount: Decimal
    payment_url: str

    def __init__(self, **kwargs):
        self.payment_address = kwargs['payment_address']
        self.payment_tag = kwargs['payment_tag']
        self.payment_amount = Decimal(kwargs['payment_amount'])
        self.payment_url = kwargs['payment_url']


class Exchange(BaseType):
    exchange_id: int
    application_id: int
    user_id: int
    status: int
    step: int
    is_fail: bool
    amount1: Decimal
    amount2: Decimal
    currency1: Currency
    currency2: Currency
    address: str
    tag: str
    created_at: int
    closed_at: int
    application_income: Decimal
    application_interest: Decimal
    error_count: int
    payment: Payment
    merchant_data = {}

    def __init__(self, **kwargs):
        self.exchange_id = kwargs['exchange_id']
        self.application_id = kwargs['application_id']
        self.user_id = kwargs['user_id']
        self.status = kwargs['status']
        self.step = kwargs['step']
        self.is_fail = kwargs['is_fail']
        self.amount1 = Decimal(kwargs['amount1'])
        self.amount2 = Decimal(kwargs['amount2'])
        self.address = kwargs['address']
        self.tag = kwargs['tag']
        self.created_at = kwargs['created_at']
        self.closed_at = kwargs['closed_at']
        self.application_income = Decimal(kwargs['application_income'])
        self.application_interest = Decimal(kwargs['application_interest'])
        self.error_count = kwargs['error_count']
        self.merchant_data = kwargs['merchant_data']

        if isinstance(kwargs['currency1'], Currency):
            self.currency1 = kwargs['currency1']
        else:
            self.currency1 = Currency(**kwargs['currency1'])
        if isinstance(kwargs['currency2'], Currency):
            self.currency2 = kwargs['currency2']
        else:
            self.currency2 = Currency(**kwargs['currency2'])

        if isinstance(kwargs['payment'], Payment):
            self.payment = kwargs['payment']
        else:
            self.payment = Payment(**kwargs['payment'])


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
    swap_deposit: bool
    last_update: int

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


class Stat(BaseType):
    day: str
    exchanges_created_count: int
    exchanges_success_count: int
    application_income: Decimal

    def __init__(self, **kwargs):
        self.day = kwargs['day']
        self.exchanges_created_count = kwargs['exchanges_created_count']
        self.exchanges_success_count = kwargs['exchanges_success_count']
        self.application_income = Decimal(kwargs['application_income'])


class User(BaseType):
    user_id: int
    kyc: bool
    email: str
    name: str
    lastname: str
    created_at: int
    applications_data = {}

    def __init__(self, **kwargs):
        self.user_id = kwargs['user_id']
        self.kyc = kwargs['kyc']
        self.email = kwargs['email']
        self.name = kwargs['name']
        self.lastname = kwargs['lastname']
        self.created_at = kwargs['created_at']
        self.applications_data = kwargs['applications_data']


class UserAuth(BaseType):
    allow: bool
    auth_key: str
    application_id: int
    code_attempt: int

    def __init__(self, **kwargs):
        self.allow = kwargs['allow']
        self.auth_key = kwargs['auth_key']
        self.application_id = kwargs['application_id']
        self.code_attempt = kwargs['code_attempt']


class Log(BaseType):
    name: str
    filesize: int

    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.filesize = kwargs['filesize']


class Application(BaseType):
    application_id: int
    name: str
    private_key: str
    public_key: str
    interest: Decimal
    balance: Decimal
    notification_url: str
    available_methods: list

    def __init__(self, **kwargs):
        self.application_id = kwargs['application_id']
        self.name = kwargs['name']
        self.private_key = kwargs['private_key']
        self.public_key = kwargs['public_key']
        self.interest = Decimal(kwargs['interest'])
        self.balance = Decimal(kwargs['balance'])
        self.notification_url = kwargs['notification_url']
        self.available_methods = kwargs['available_methods']
