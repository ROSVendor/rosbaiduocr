# encoding=utf-8

from __future__ import with_statement

import urlparse
from requests import get, post
import rospy, json, sys


class APIURL:
    FREE = 'http://apis.baidu.com/apistore/idlocr/ocr'
    ENTERPRISE = 'http://apis.baidu.com/idl_baidu/baiduocrpay/idlocrpaid'


class Configuration(object):
    def __init__(self,
                 url,
                 fromdevice='pc',
                 clientip='10.10.10.10',
                 detecttype='Recognize',
                 languagetype='CHN_ENG'):
        self.fromdevice = fromdevice
        self.clientip = clientip
        self.detecttype = detecttype
        self.languagetype = languagetype
        self.imagetype = 2
        self.files = {'image': ('ocr.jpg', self.trans_img(url))}

    def config(self, apikey):
        data = dict(self.__dict__)
        for key in data.keys():
            if type(key) != str:
                del data[key]
        header = {'apikey': apikey}
        return header, data, self.files

    @staticmethod
    def trans_img(url):
        pr = urlparse.urlparse(url)
        # TODO handle IOErrors
        if pr.scheme == 'file':
            return open(pr.path, 'rb')
        elif pr.scheme in ['http', 'https']:
            return get(url).content
        else:
            raise RuntimeError("url not accessible")


class Result(object):
    __slots__ = ['word', 'top', 'left', 'width', 'height']

    def __init__(self, item):
        self.word = item['word']
        rect = item['rect']
        self.height = rect['height']
        self.width = rect['width']
        self.top = rect['top']
        self.left = rect['left']


class ResultSet(object):
    __slots__ = ['errNum', 'errMsg', 'querySign', 'retData', 'retResult']

    def __init__(self, ret):
        self.errNum = ret['errNum']
        self.errMsg = ret['errMsg']
        self.querySign = ret['querySign']
        self.retData = ret['retData']
        self.retResult = list(map(Result, ret['retData']))

    @property
    def contents(self):
        return ''.join(map(lambda x: x.word, self.retResult))

    @property
    def content_segments(self):
        return map(lambda x: x.word, self.retResult)

    @property
    def error_detail(self):
        return format_error_code(self.errNum)


err_codes = dict()


def __init__(self):
    global err_codes
    err_codes[300101] = "User's request is expired"
    err_codes[300102] = "User call overrun per day"
    err_codes[300103] = "Service call overrun per second"
    err_codes[300104] = "Service call overrun per day"
    err_codes[300201] = "URL cannot be resolved"
    err_codes[300202] = "Missing apikey"
    err_codes[300203] = "Apikey or secretkey is NULL"
    err_codes[300204] = "Apikey does not exist	apikey"
    err_codes[300205] = "Api does not exist	api"
    err_codes[300206] = "Api out of service	api"
    err_codes[300301] = "Internal error"
    err_codes[300302] = "Sorry,The system is busy. Please try again late"


def format_error_code(code):
    description = err_codes.get(code)
    if description is None:
        return None
    return "%d: %s" % (code, description)


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

    @staticmethod
    def load(file_name):
        with open(file_name) as fd:
            conf = json.load(fd)
            return BaiduOCRClient(**conf)
        raise rospy.ServiceException('Cannot load \'%s\'' % file_name)

