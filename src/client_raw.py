#!/usr/bin/env python
# encoding=utf-8

import roslib
roslib.load_manifest('rosbaiduocr')

from rosvendor.core.generator.client import client_proxy
from rosbaiduocr.srv import *

@client_proxy('BaiduOCRRaw', BaiduOCRRaw)
def baiduocr_raw():
    pass

if __name__ == '__main__':
    res = baiduocr_raw(BaiduOCRRawRequest('http://apistore.baidu.com/idlapi/img_demo_data/ocr/LocateRecognize//28.jpg'))
    print(res.json.encode())


