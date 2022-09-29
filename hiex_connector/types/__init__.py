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
