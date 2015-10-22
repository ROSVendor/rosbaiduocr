#!/usr/bin/env python

import roslib
roslib.load_manifest('rosbaiduocr')

from protocol import BaiduOCRClient
from rosvendor.core.generator.server import gen_server
from rosbaiduocr.srv import *
import json

client = BaiduOCRClient.load('default.json')

@gen_server('BaiduOCRRaw', BaiduOCRRaw)
def baiduocr_raw(req):
    rs = client.recognize(req.url)
    return BaiduOCRRawResponse(json.dumps(rs))

if __name__ == '__main__':
    baiduocr_raw()

