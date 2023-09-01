from decimal import Decimal
from typing import Optional, Union
from pydantic import BaseModel


class ResponseList(list):
    is_all: bool = False


class Empty:
    def __init__(self):
        pass


class BaseType(BaseModel):
    class Config:
        arbitrary_types_allowed = True

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


class BaseWithAuthKey(BaseType):
    auth_key: str


class Currency(BaseType):
    code: str
    short_name: str
    name: str
    available_tag: bool
    round_ndigits: int
    img: Optional[str]


class AdditionalFields(BaseType):
    beneficiary_email: Optional[str]
    beneficiary_first_name: Optional[str]
    beneficiary_last_name: Optional[str]
    beneficiary_tin: Optional[str]
    beneficiary_phone: Optional[str]


class Payment(BaseType):
    currency: Union[Currency, dict]
    address: Optional[str]
    address_qr: Optional[str]
    tag: Optional[str]
    url: Optional[str]
    amount: Decimal

    def __post_init__(self):
        if not isinstance(self.currency, Currency):
            self.currency = Currency(**self.currency)


class Exchange(BaseType):
    exchange_id: str
    user_id: int
    status: int
    amount1: Decimal
    amount2: Decimal
    currency1: Union[Currency, dict]
    currency2: Union[Currency, dict]
    address: str
    tag: Optional[str]
    additional_fields: Union[AdditionalFields, dict]
    created_at: Optional[int]
    closed_at: Optional[int]

    def __post_init__(self):
        if not isinstance(self.currency1, Currency):
            self.currency1 = Currency(**self.currency1)
        if not isinstance(self.currency2, Currency):
            self.currency2 = Currency(**self.currency2)
        if not isinstance(self.additional_fields, AdditionalFields):
            self.additional_fields = AdditionalFields(**self.additional_fields)


class Pair(BaseType):
    currency1: Union[Currency, dict]
    currency2: Union[Currency, dict]
    min_amount1: Decimal
    max_amount1: Decimal
    min_amount2: Decimal
    max_amount2: Decimal
    price_factor: Decimal
    price: Decimal
    kyc_required: bool
    available_tag: bool
    additional_fields_list: Optional[list]
    comment: Optional[str]

    def __post_init__(self):
        if not isinstance(self.currency1, Currency):
            self.currency1 = Currency(**self.currency1)
        if not isinstance(self.currency2, Currency):
            self.currency2 = Currency(**self.currency2)


class Stat(BaseType):
    day: str
    exchanges_success_count: int
    exchanges_created_count: int
    exchanges_success_amount: Decimal
    application_income: Optional[Decimal]


class User(BaseType):
    user_id: int
    kyc: bool
    email: str
    first_name: Optional[str]
    last_name: Optional[str]
    balance: Decimal
    referral_token: Optional[str]
    referral_id: Optional[int]
    referrals_count: int
    referrals_sum_amount: Decimal
    referral_interest: Decimal
    created_at: int
    data: Optional[dict]

    def __post_init__(self):
        if self.data is None:
            self.data = {}


class Auth(BaseType):
    allow: bool
    auth_key: str
    application_id: int
    code_attempt: int


class Application(BaseType):
    application_id: int
    user_id: int
    name: str
    public_key: str
    interest: Decimal
    income: Decimal
    notification_url: Optional[str]


class Referral(BaseType):
    user_id: int
    email: str
    created_at: int
    amount: Decimal
    kyc: bool


class VerificationService(BaseType):
    name: str
    options: Optional[list]


class Verification(BaseType):
    method: str
    option: Optional[str]
    url: Optional[str]
    qr: Optional[str]
