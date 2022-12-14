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
    use_tag: bool = False
    img: str = None

    def __init__(self, **kwargs):
        self.code = kwargs['code']
        self.use_tag = kwargs['use_tag']
        self.img = kwargs['img']


class Payment(BaseType):
    address: str
    address_qr: str
    tag: str
    amount: Decimal
    url: str

    def __init__(self, **kwargs):
        self.address = kwargs['address']
        self.address_qr = kwargs['address_qr']
        self.tag = kwargs['tag']
        self.amount = Decimal(kwargs['amount'])
        self.url = kwargs['url']


class Exchange(BaseType):
    exchange_id: str
    user_id: int
    status: int
    amount1: Decimal
    amount2: Decimal
    currency1: Currency
    currency2: Currency
    address: str
    tag: str
    created_at: int
    closed_at: int

    def __init__(self, **kwargs):
        self.exchange_id = kwargs['exchange_id']
        self.user_id = kwargs['user_id']
        self.status = kwargs['status']
        self.amount1 = Decimal(kwargs['amount1'])
        self.amount2 = Decimal(kwargs['amount2'])
        self.address = kwargs['address']
        self.tag = kwargs['tag']
        self.created_at = kwargs['created_at']
        self.closed_at = kwargs['closed_at']

        if isinstance(kwargs['currency1'], Currency):
            self.currency1 = kwargs['currency1']
        else:
            self.currency1 = Currency(**kwargs['currency1'])
        if isinstance(kwargs['currency2'], Currency):
            self.currency2 = kwargs['currency2']
        else:
            self.currency2 = Currency(**kwargs['currency2'])


class Pair(BaseType):
    currency1: Currency
    currency2: Currency
    min_amount1: Decimal
    max_amount1: Decimal
    min_amount2: Decimal
    max_amount2: Decimal
    price_factor: Decimal
    price: Decimal
    kyc_required: bool
    comment: str

    def __init__(self, **kwargs):
        self.min_amount1 = Decimal(kwargs['min_amount1'])
        self.max_amount1 = Decimal(kwargs['max_amount1'])
        self.min_amount2 = Decimal(kwargs['min_amount2'])
        self.max_amount2 = Decimal(kwargs['max_amount2'])
        self.price_factor = Decimal(kwargs['price_factor'])
        self.price = Decimal(kwargs['price'])
        self.kyc_required = kwargs['kyc_required']
        self.comment = kwargs['comment']

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
    balance: Decimal
    referral_token: str
    referral_id: int
    referrals_count: int
    referrals_sum_amount: Decimal
    data: dict = {}

    def __init__(self, **kwargs):
        self.user_id = kwargs['user_id']
        self.kyc = kwargs['kyc']
        self.email = kwargs['email']
        self.name = kwargs['name']
        self.lastname = kwargs['lastname']
        self.balance = Decimal(kwargs['balance'])
        self.referral_token = kwargs['referral_token']
        self.referral_id = kwargs['referral_id']
        self.referrals_count = kwargs['referrals_count']
        self.referrals_sum_amount = Decimal(kwargs['referrals_sum_amount'])
        self.data = kwargs['data']


class Auth(BaseType):
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
    user_id: int
    name: str
    public_key: str
    interest: Decimal
    balance: Decimal
    notification_url: str

    def __init__(self, **kwargs):
        self.application_id = kwargs['application_id']
        self.user_id = kwargs['user_id']
        self.name = kwargs['name']
        self.public_key = kwargs['public_key']
        self.interest = Decimal(kwargs['interest'])
        self.balance = Decimal(kwargs['balance'])
        self.notification_url = kwargs['notification_url']


class Referral(BaseType):
    user_id: int
    email: str
    created_at: int
    amount: Decimal
    kyc: bool

    def __init__(self, **kwargs):
        self.user_id = kwargs['user_id']
        self.email = kwargs['email']
        self.created_at = kwargs['created_at']
        self.amount = Decimal(kwargs['amount'])
        self.kyc = kwargs['kyc']


class VerificationService(BaseType):
    name: str
    options: list

    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.options = kwargs['options']


class Verification(BaseType):
    method: str
    option: str
    url: str
    qr: str

    def __init__(self, **kwargs):
        self.method = kwargs['method']
        self.option = kwargs['option']
        self.url = kwargs['url']
        self.qr = kwargs['qr']
