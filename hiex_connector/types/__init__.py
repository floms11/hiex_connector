from decimal import Decimal


class BaseType:
    def __getitem__(self, item):
        return self.values[item]

    def __getattr__(self, item):
        return self.values[item]


class Coin(BaseType):
    code: str
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
        self.code = kwargs['code']
        self.deposit_merchant = kwargs['deposit_merchant']
        self.withdrawal_merchant = kwargs['withdrawal_merchant']
        self.use_tag = kwargs['use_tag']
        self.kyc_required = kwargs['kyc_required']
        self.min_deposit = kwargs['min_deposit']
        self.max_deposit = kwargs['max_deposit']
        self.min_withdrawal = kwargs['min_withdrawal']
        self.max_withdrawal = kwargs['max_withdrawal']
        self.round_ndigits = kwargs['round_ndigits']
