#!/usr/bin/env python

import roslib
roslib.load_manifest('rosbaiduocr')

from protocol import BaiduOCRClient
from rosvendor.core.generator.server import gen_server
from rosbaiduocr.srv import *
import json, os, sys

if len(sys.argv) == 2:
    config_path = os.path.realpath(sys.argv[1])
else:
    config_path = 'default.json'

client = BaiduOCRClient.load(config_path)

@gen_server('BaiduOCRSimple', BaiduOCRRaw)
def baiduocr_raw(req):
    rs = client.recognize(req.url)
    return BaiduOCRRawResponse(json.dumps(rs))

if __name__ == '__main__':
    baiduocr_raw()

