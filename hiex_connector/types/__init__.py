from decimal import Decimal


class BaseType:
    code: int

    def __init__(self, code):
        self.code = code

    def __repr__(self):
        return (
            f"<{self.__class__.__name__} values: "
            + ";".join([f"{key}={self[key]}" for key in self.__dict__.keys()])
            + ">"
        )

    def __getitem__(self, item):
        return getattr(self, item)


class ResponseException(BaseType):
    detail: str

    def __init__(self, code, detail=''):
        super().__init__(code)
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
        self.min_deposit = kwargs['min_deposit']
        self.max_deposit = kwargs['max_deposit']
        self.min_withdrawal = kwargs['min_withdrawal']
        self.max_withdrawal = kwargs['max_withdrawal']
        self.round_ndigits = kwargs['round_ndigits']
