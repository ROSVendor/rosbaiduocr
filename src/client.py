# encoding=utf-8

from requests import post
from protocol import APIURL, Configuration, ResultSet


class BaiduOCRClient:
    def __init__(self, api_key, api_url):
        self.api_key = api_key
        self.api_url = api_url

    def recognize(self, file_url):
        conf = Configuration(file_url)
        headers, data, files = conf.config(self.api_key)
        raw_response = post(self.api_url, headers=headers, data=data, files=files)
        response = raw_response.json() if raw_response else None
        return response
