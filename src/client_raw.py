# encoding=utf-8

from requests import post
from protocol import APIURL, Configuration, ResultSet
from baiduocr.src import *
import rospy, json

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

client = None # TODO Config it

def baiduocr_raw(req):
    rs = client.recognize(req.url)
    return BaiduOCRRaw(json.dumps(rs))

def baiduocr_simple(req):
    rs = ResultSet(client.recognize(req.url))
    return BaiduOCRSimpl(rs.errNum, rs.contents, rs.errMsg)

def raw_server():
    rospy.init_node('BaiduOCRRaw')
    s = rospy.Service('BaiduOCRRaw', BaiduOCRRaw, handle_add_two_ints)
    rospy.spin()

def simple_server():
    rospy.init_node('BaiduOCRSimple')
    s = rospy.Service('BaiduOCRSimple', BaiduOCRSimple, handle_add_two_ints)
    rospy.spin()

if __name__ == '__main__':
    raw_server()
    simple_server()
