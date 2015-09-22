# encoding=utf-8

import urlparse

class Configuration(object):
    def __init__(self,
                 url,
                 fromdevice='pc',
                 clientip='10.10.10.10',
                 detecttype='LocateRecognize',
                 languagetype='CHN_ENG'):
        self.fromdevice   = fromdevice
        self.clientip     = clientip
        self.detecttype   = detecttype
        self.languagetype = languagetype
        self.imagetype    = 2
        self.image        = Configuration.trans_img(url)

    def dump(self):
        return self.__dict__

    @staticmethod
    def trans_img(url):
        pr = urlparse.urlparse(url)


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
