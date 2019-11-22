import requests
from commTools.st_des import des_descrypt, des_encrypt
from commTools.toBASE64 import jpgtostr
import json
import xml.etree.ElementTree as ET


class Cdzj:
    def __init__(self):
        self.uploadPersonURL = ""
        self.downloadPersonURL = ""
        self.uploadAttendanceURL = ""
        self.downloadDelPersonURL = ""
        self.feedbackURL = ""
        self.person = {}
        self.attdata = {}
        self.delPersonID = ''
        self.msg = ''
        
    def uploadPerson(self):
        """ 用于上传人员信息到住建平台 """
        r = requests.post(self.uploadPersonURL, data=self.person)
        result = r.json()

        if result['errcode'] == 0:
            self.msg = 'success'
        else:
            self.msg = result['errmsg']      
        
    def downloadPerson(self, deviceSN, key):
        """ 用于从住建平台下载正式人员，需要提供考勤设备的sn,与对就的key """
        headers = {'Content-Type': 'application/json;charset=gb2312'}
        payload = {'sn': deviceSN}
        r = requests.get(self.downloadPersonURL, params=payload)
        xml = r.text
        el = ET.fromstring(xml)
        st = el.text
        js = json.loads(st)
        result = js['Result']
        zresult = js['Msg']
        if result == 0:
            content = js['Content']
            if content != '':
                bcon = des_descrypt(content, key)
                ccon = bcon.decode('utf-8')
                dcon = json.loads(ccon)
                for item in dcon:
                    self.person['user_id'] = item['user_id']
                    self.person['work_sn'] = item['work_sn']
                    self.person['idNo'] = item['id_card']
                    self.msg = 'success'
            else:
                self.msg = '未收到数据'
        else:
            self.msg = zresult

    def uploadAttendance(self, deviceSN, key):
        """ 用于上传人员考勤信息到住建平台 """
        content = des_encrypt(self.attdata, key)
        payload = {'sn': deviceSN, 'content': content}
        r = requests.post(self.uploadAttendanceURL, data=payload)
        xml = r.text
        el = ET.fromstring(xml)
        r1 = el.text
        # r1 = txt.replace(r'/', '')
        # r1 = r1.replace(r'<string>', '')
        j = json.loads(r1)
        if j['Result'] == 0:
            self.msg = 'success'
        else:
            self.msg = j['Msg']

    def downloadDelPerson(self, deviceSN, key):
        """ 用于从住建平台下载需要删除的人员 """
        headers = {'content-type': 'application/json;charset=utf-8'}
        params = {'sn': deviceSN}
        r = requests.get(self.downloadDelPersonURL, params=params)
        xml = r.text
        el = ET.fromstring(xml)
        str1 = el.text
        js = json.loads(str1)
        re = js['Result']
        if re == 0:
            content = js['Content']
            bcontent = des_descrypt(content, key)
            ccontent = bcontent.decode('utf-8')
            dcontent = json.loads(ccontent)
            for item in dcontent:
                self.delPersonID = item['user_id']
            self.msg = 'success'
        else:
            self.msg = js['Msg']

    def feedback(self, deviceSN, otype, msg):
        """ 用于下载人员和下载需删除的人员成功后，给住建平台的反馈 """
        p = {'type': otype, 'sn': deviceSN, 'msg': msg}
        r = requests.get(self.feedbackURL, params=p)
        rtxt = r.text
        el = ET.fromstring(rtxt)
        str1 = el.text
        js = json.loads(str1)
        if js['Result'] == 0:
            self.msg = 'success'
        else:
            self.msg = r.json['Msg']
