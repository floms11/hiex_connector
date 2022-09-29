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


class ResponseException(BaseType):
    code: int
    detail: str

    def __init__(self, code, detail=''):
        self.code = code
        self.detail = detail


class Coin(BaseType):
    currency_code: str
    deposit_merchant: str
    withdrawal_merchant: str
    use_tag: bool
    kyc_required: bool
    min_deposit: Decimal
    max_deposit: Decimal
    min_withdrawal: Decimal
    max_withdrawal: Decimal
    round_ndigits: int

    def __init__(self, **kwargs):
        self.currency_code = kwargs['currency_code']
        self.deposit_merchant = kwargs['deposit_merchant']
        self.withdrawal_merchant = kwargs['withdrawal_merchant']
        self.use_tag = kwargs['use_tag']
        self.kyc_required = kwargs['kyc_required']
        self.min_deposit = Decimal(kwargs['min_deposit'])
        self.max_deposit = Decimal(kwargs['max_deposit'])
        self.min_withdrawal = Decimal(kwargs['min_withdrawal'])
        self.max_withdrawal = Decimal(kwargs['max_withdrawal'])
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
    currency1: str
    currency2: str
    address: str
    tag: str
    created_at: int
    closed_at: int
    application_income: Decimal
    application_interest: Decimal
    error_count: int
    payment: Payment
    merchant_data = None

    def __init__(self, **kwargs):
        self.exchange_id = kwargs['exchange_id']
        self.application_id = kwargs['application_id']
        self.user_id = kwargs['user_id']
        self.status = kwargs['status']
        self.step = kwargs['step']
        self.is_fail = kwargs['is_fail']
        self.amount1 = Decimal(kwargs['amount1'])
        self.amount2 = Decimal(kwargs['amount2'])
        self.currency1 = kwargs['currency1']
        self.currency2 = kwargs['currency2']
        self.address = kwargs['address']
        self.tag = kwargs['tag']
        self.created_at = kwargs['created_at']
        self.closed_at = kwargs['closed_at']
        self.application_income = Decimal(kwargs['application_income'])
        self.application_interest = Decimal(kwargs['application_interest'])
        self.error_count = kwargs['error_count']
        self.payment = Payment(**kwargs['payment'])
        self.merchant_data = kwargs['merchant_data']