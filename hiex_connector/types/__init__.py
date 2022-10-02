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


class Coin(BaseType):
    currency_code: str

    def __init__(self, **kwargs):
        self.currency_code = kwargs['currency_code']


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
    user_id: int
    status: int
    amount1: Decimal
    amount2: Decimal
    currency1: str
    currency2: str
    address: str
    tag: str
    payment: Payment
    created_at: int
    closed_at: int

    def __init__(self, **kwargs):
        self.exchange_id = kwargs['exchange_id']
        self.user_id = kwargs['user_id']
        self.status = kwargs['status']
        self.amount1 = Decimal(kwargs['amount1'])
        self.amount2 = Decimal(kwargs['amount2'])
        self.currency1 = kwargs['currency1']
        self.currency2 = kwargs['currency2']
        self.address = kwargs['address']
        self.tag = kwargs['tag']
        self.payment = Payment(**kwargs['payment'])
        self.created_at = kwargs['created_at']
        self.closed_at = kwargs['closed_at']


class Pair(BaseType):
    currency1: str
    currency2: str
    min_amount1: Decimal
    max_amount1: Decimal
    min_amount2: Decimal
    max_amount2: Decimal
    price: Decimal
    comment: str

    def __init__(self, **kwargs):
        self.currency1 = kwargs['currency1']
        self.currency2 = kwargs['currency2']
        self.min_amount1 = Decimal(kwargs['min_amount1'])
        self.max_amount1 = Decimal(kwargs['max_amount1'])
        self.min_amount2 = Decimal(kwargs['min_amount2'])
        self.max_amount2 = Decimal(kwargs['max_amount2'])
        self.price = Decimal(kwargs['price'])
        self.comment = kwargs['comment']


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

    def __init__(self, **kwargs):
        self.user_id = kwargs['user_id']
        self.kyc = kwargs['kyc']
        self.email = kwargs['email']
        self.name = kwargs['name']
        self.lastname = kwargs['lastname']


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


class Application(BaseType):
    application_id: int
    name: str
    public_key: str
    interest: Decimal
    balance: Decimal
    notification_url: str

    def __init__(self, **kwargs):
        self.application_id = kwargs['application_id']
        self.name = kwargs['name']
        self.public_key = kwargs['public_key']
        self.interest = Decimal(kwargs['interest'])
        self.balance = Decimal(kwargs['balance'])
        self.notification_url = kwargs['notification_url']
