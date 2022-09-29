import time
import requests
import hashlib
import simplejson


class HiExConnectorBase:
    __private_key: str = ''
    __public_key: str = ''
    __basic_url: str = 'https://api.hiex.io/'

    def __init__(self, private_key, public_key):
        self.__private_key = private_key
        self.__public_key = public_key

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

    def _get_request(self, method, data={}):
        data['public_key'] = self.__public_key
        data['timestamp'] = time.time()
        data['hash'] = self._get_hash(data)
        req = requests.post(f'{self.__basic_url}{method}', json=data)
        return req.text

    def get_request(self, method, data={}):
        resp = self._get_request(method, data)
        resp = simplejson.loads(resp)
        resp_hash = self._get_hash(resp)
        if resp_hash != resp['hash']:
            raise Exception('No verify hash')
        if resp['code'] < 0:
            code = resp['code']
            detail = ''
            if 'detail' in resp:
                detail = resp['detail']
            raise Exception(f'Server error. Code={code}. Detail={detail}')
        return resp
