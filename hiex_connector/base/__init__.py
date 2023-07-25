from decimal import Decimal
import os
import requests
import hashlib
import hmac
import simplejson
import time
import aiohttp
from contextvars import ContextVar
from ..version import __version__
from ..exceptions import *
from ..types import Empty


class HiExConnectorBase:
    __private_key: str = ''
    __public_key: str = ''
    __basic_url: str = 'https://api.hiex.io/'
    __lang: str = None
    __lang_context_var: ContextVar = None

    def __init__(self, private_key, public_key, base_url=None, lang=None, lang_context_var: ContextVar = None):
        self.__private_key = private_key
        self.__public_key = public_key
        if base_url is not None:
            self.__basic_url = base_url
        self.__lang = lang
        self.__lang_context_var = lang_context_var

    def get_request(self, method, data):
        text, headers = self.get_request_data(method, data)
        return self.get_valid_response(text, headers)

    def get_request_data(self, method, data):
        data = self._pre_request_data(data)
        timestamp = str(time.time())
        r = requests.post(
            f'{self.__basic_url}{method}',
            data=data,
            headers={
                'Content-type': 'application/json',
                'X-APP-PUBLIC-KEY': self.__public_key,
                'X-APP-TIMESTAMP': timestamp,
                'X-APP-SIGNATURE': self._get_sign(data, timestamp),
            }
        )
        return r.text, r.headers

    async def get_async_request(self, method, data):
        text, headers = await self.get_async_request_data(method, data)
        return self.get_valid_response(text, headers)

    async def get_async_request_data(self, method, data):
        data = self._pre_request_data(data)
        timestamp = str(time.time())
        headers = {
            'Content-type': 'application/json',
            'X-APP-PUBLIC-KEY': self.__public_key,
            'X-APP-TIMESTAMP': timestamp,
            'X-APP-SIGNATURE': self._get_sign(data, timestamp),
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(
                    f'{self.__basic_url}{method}',
                    data=data,
                    headers=headers,
                    allow_redirects=True
            ) as resp:
                text = await resp.text()
                return text, resp.headers

    def _pre_request_data(self, data):
        lang = None
        if self.__lang:
            lang = self.__lang
        if self.__lang_context_var:
            _lang = self.__lang_context_var.get()
            if _lang:
                lang = _lang
        new_data = {}
        for key in data:
            if data[key] is not Empty:
                new_data[key] = data[key]
        new_data['lang'] = lang
        return simplejson.dumps(new_data)

    def get_valid_response(self, body, headers):
        self.check_version(headers['X-APP-VERSION'])
        sign = self._get_sign(body, headers['X-APP-TIMESTAMP'])
        resp_sign = headers['X-APP-SIGNATURE']
        if resp_sign != sign:
            raise ProcessingError(f'No verify hash {resp_sign}!={sign}')

        data = simplejson.loads(body)
        if data['code'] < 0:
            code = data['code']
            param = data['param']
            detail = ''
            if 'detail' in data:
                detail = data['detail']
            raise ResponseError(detail, code, param)
        return data

    def _get_sign(self, body, timestamp):
        if type(body) == str:
            body = body.encode('utf-8')
        if type(timestamp) == str:
            timestamp = timestamp.encode('utf-8')
        return hmac.new(
            self.__private_key.encode('utf-8'),
            body + timestamp,
            digestmod=hashlib.sha256
        ).hexdigest()

    @staticmethod
    def get_version_api():
        dir = os.path.dirname(os.path.abspath(__file__)) + '/../'
        with open(f"{dir}.apiversion", "r") as f:
            return Decimal(f.read())

    @staticmethod
    def check_version(version):
        version_num = version.split('_')[1]
        version_nums = version_num.split('.')
        api_version_nums = __version__.split('.')
        _version = Decimal(f"{version_nums[0]}.{version_nums[1]}")
        _api_version = Decimal(f"{api_version_nums[0]}.{api_version_nums[1]}")
        if _api_version >= _version:
            return True
        else:
            raise VersionError(f'Бібліотека застаріла. {_version}>{_api_version}')
