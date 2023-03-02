class ResponseError(Exception):
    code: int = 0
    param: str = 'None'
    detail: str = ''
    message: str = ''

    def __init__(self, detail: str = None, code: int = None, param: str = None):
        if detail:
            self.message = self.detail = detail
        if code:
            self.code = code
        if param:
            self.param = param

    def __str__(self):
        return f"{self.__class__.__name__}, {self.code}, {self.param}, {self.detail}"


class ProcessingError(Exception):
    message: str = ''

    def __init__(self, message: str = None):
        if message:
            self.message = message

    def __str__(self):
        return f"{self.__class__.__name__}, {self.message}"


class VersionError(Exception):
    message: str = ''

    def __init__(self, message: str = None):
        if message:
            self.message = message

    def __str__(self):
        return f"{self.__class__.__name__}, {self.message}"
