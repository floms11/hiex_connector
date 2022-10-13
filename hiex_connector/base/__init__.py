from decimal import Decimal
import os
import requests
import hashlib
import hmac
import simplejson
import time
import asyncio
import aiohttp
from ..version import __version__
from ..exceptions import *


class HiExConnectorBase:
    __private_key: str = ''
    __public_key: str = ''
    __basic_url: str = 'https://api.hiex.io/'

    def __init__(self, private_key, public_key):
        self.__private_key = private_key
        self.__public_key = public_key

    def get_request(self, method, data):
        text, headers = self.get_request_data(method, data)
        return self._get_valid_response(text, headers)

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
        time.sleep(0.05)
        return r.text, r.headers

    async def get_async_request(self, method, data):
        text, headers = await self.get_async_request_data(method, data)
        return self._get_valid_response(text, headers)

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
                await asyncio.sleep(0.05)
                return text, resp.headers

    @staticmethod
    def _pre_request_data(data):
        new_data = {}
        for key in data:
            if data[key] is not None:
                new_data[key] = data[key]
        return simplejson.dumps(new_data)

    def _get_valid_response(self, body, headers):
        self.check_version(headers['X-APP-VERSION'])
        sign = self._get_sign(body, headers['X-APP-TIMESTAMP'])
        resp_sign = headers['X-APP-SIGNATURE']
        if resp_sign != sign:
            raise ProcessingError(f'No verify hash {resp_sign}!={sign}')

        data = simplejson.loads(body)
        if data['code'] < 0:
            code = data['code']
            detail = ''
            if 'detail' in data:
                detail = data['detail']
            raise ResponseError(detail, code)
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
        _version = Decimal(f"{version_nums[0]}.{version_nums[1]}")
        _api_version = Decimal(__version__)
        if _api_version >= _version:
            return True
        else:
            raise VersionError(f'Бібліотека застаріла. {_version}>{_api_version}')
