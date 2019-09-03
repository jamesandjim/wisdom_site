import requests
import json


class Face_device:
    def __init__(self, ip):
        self.key = '123456'
        self.ip = ip
        self.operator = {"op": "setPassWord"}
        self.url = "http://{}:8090/{}".format(self.ip, self.operator['op'])
        self.setPassWord_url = "http://{}:8090/setPassWord".format(self.ip)

    def setPassWord(self):
        """
        成功返回True，否则false
        :return:
        """
        payload = {'oldPass': '123456', 'newPass': '123456'}
        r = requests.post(self.setPassWord_url, data=payload)
        j = r.json()
        if j['success']:
            return True
        else:
            return False


    def getDeviceKey(self):
        url = "http://{}:8090/getDeviceKey".format(self.ip)
        r = requests.get(url)
        j = r.json()
        if j['success']:
            return j['data']
        else:
            return None


