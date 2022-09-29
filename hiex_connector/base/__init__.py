import time
import requests
import hashlib


class HiExConnectorBase:
    __private_key: str = ''
    __public_key: str = ''
    __basic_url: str = 'https://api.hiex.io/'

    def __init__(self, private_key, public_key):
        self.__private_key = private_key
        self.__public_key = public_key

    def get_hash_data_string(self, _data):
        string_hash = ''
        if isinstance(_data, list):
            data = {i: _data[i] for i in range(len(_data))}
        else:
            data = _data
        for key, value in data.items():
            if key != 'hash':
                if type(value) in (list, dict, tuple):
                    string_hash += str(key) + self.get_hash_data_string(value)
                else:
                    string_hash += str(key) + str(value)
        return string_hash

    def get_hash(self, _data):
        string_hash = self.get_hash_data_string(_data)
        string_hash += self.__private_key
        hash_object = hashlib.sha512(string_hash.encode())
        hex_dig = hash_object.hexdigest()
        return hex_dig

    def get_request(self, method, data={}):
        data['public_key'] = self.__public_key
        data['timestamp'] = time.time()
        data['hash'] = self.get_hash(data)
        req = requests.post(f'{self.__basic_url}{method}', json=data)
        resp = req.json()
        resp_hash = self.get_hash(resp)
        if resp_hash == resp['hash']:
            return resp
        else:
            return False
