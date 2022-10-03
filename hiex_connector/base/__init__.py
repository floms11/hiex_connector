from decimal import Decimal
import os
import requests
import hashlib
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
        text = self.get_request_text(method, data)
        return self._get_valid_response(text)

    def get_request_text(self, method, data):
        r = requests.post(f'{self.__basic_url}{method}', json=self._pre_request_data(data))
        time.sleep(0.05)
        return r.text

    async def get_async_request(self, method, data):
        text = await self.get_async_request_text(method, data)
        return self._get_valid_response(text)

    async def get_async_request_text(self, method, data):
        headers = {
            'Content-type': 'application/json',
        }
        async with aiohttp.ClientSession() as session:
            async with session.post(
                    f'{self.__basic_url}{method}',
                    json=self._pre_request_data(data),
                    headers=headers,
                    allow_redirects=True
            ) as resp:
                text = await resp.text()
                await asyncio.sleep(0.05)
                return text

    def _pre_request_data(self, data):
        new_data = {}
        for key in data:
            if data[key] is not None:
                new_data[key] = data[key]
        new_data['public_key'] = self.__public_key
        new_data['timestamp'] = time.time()
        new_data['hash'] = self._get_hash(new_data)
        return new_data

    def _get_valid_response(self, response):
        data = simplejson.loads(response)
        self.check_version(data['version'])
        resp_hash = self._get_hash(data)
        if resp_hash != data['hash']:
            raise ProcessingError(f'No verify hash {resp_hash}!={data["hash"]}')
        if data['code'] < 0:
            code = data['code']
            detail = ''
            if 'detail' in data:
                detail = data['detail']
            raise ResponseError(detail, code)
        return data

    def _get_hash_data_string(self, _data):
        string_hash = ''
        if isinstance(_data, list):
            data = {i: _data[i] for i in range(len(_data))}
        else:
            data = _data
        for key, value in data.items():
            if key != 'hash':
                if type(value) in (list, dict, tuple):
                    string_hash += str(key) + self._get_hash_data_string(value)
                else:
                    string_hash += str(key) + str(value)
        return string_hash

    def _get_hash(self, _data):
        string_hash = self._get_hash_data_string(_data)
        string_hash += self.__private_key
        hash_object = hashlib.sha512(string_hash.encode())
        hex_dig = hash_object.hexdigest()
        return hex_dig

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
