from abc import ABCMeta, abstractmethod

import aiohttp
import requests


class Adapter(metaclass=ABCMeta):
    def __init__(self, authentication_key: str, *, pro=False):
        self.base_url_free = 'https://api-free.deepl.com/'
        self.base_url_pro = 'https://api.deepl.com/'
        self.api_version = 'v2'
        self.auth_key = authentication_key
        self.pro = pro

    @abstractmethod
    def request(self, method, path, payload={}, **kwargs):
        raise NotImplementedError()

    @abstractmethod
    def get_translated_text(self, payload):
        raise NotImplementedError()

    @abstractmethod
    def get_usage(self):
        raise NotImplementedError()

    @abstractmethod
    def get_supported_languages(self):
        raise NotImplementedError()


class RequestsAdapter(Adapter):
    def request(self, method, path, payload={}, **kwargs):
        headers = {'content-type': 'x-www-form-urlencoded'}
        payload['auth_key'] = self.auth_key

        url = self.base_url_pro if self.pro else self.base_url_free
        url += self.api_version + path

        resp = requests.request(method, url, params=payload, headers=headers)
        return resp.json()

    def get_translated_text(self, payload):
        data = self.request('POST', '/translate', payload)
        return data['translations'][0]['text']

    def get_usage(self):
        data = self.request('POST', '/usage')
        return data

    def get_supported_languages(self):
        data = self.request('POST', '/languages')
        return data


class AiohttpAdapter(Adapter):

    async def request(self, method, path, payload={}, **kwargs):
        headers = {'content-type': 'x-www-form-urlencoded'}
        payload['auth_key'] = self.auth_key

        url = self.base_url_pro if self.pro else self.base_url_free
        url += self.api_version + path

        async with aiohttp.request(
                method, url, params=payload, headers=headers) as resp:
            return await resp.json()

    async def get_translated_text(self, payload):
        data = await self.request('POST', '/translate', payload)
        return data['translations'][0]['text']

    async def get_usage(self):
        data = await self.request('POST', '/usage')
        return data

    async def get_supported_languages(self):
        data = await self.request('POST', '/languages')
        return data
