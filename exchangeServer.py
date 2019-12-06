import time
import datetime
import base64
import requests

from commTools.netUtil import ping
from commTools.toBASE64 import jpgtostr
from models.dbtools import Dboperator
from cdzjpt import Cdzj


db = Dboperator()


class DeviceExchangeInfo:
    '''用于处理与人脸设备交换数据的逻辑'''
    def __init__(self):
        '''各种属性及需要交换的数据'''
        # self.db = Dboperator()
        global db
        self.devsIPlist = []
        self.prepare()

    def prepare(self):
        dev_qs = "select ip from wis_faceDevice where status = 1"
        devices = db.querySQL(dev_qs)
        dev_count = devices.rowCount()
        if dev_count > 0:
            i = 0

            while i < dev_count:
                device = devices.record(i)
                self.devsIPlist.append(device.field('ip').value())
                i += 1

    def queryResult(self):
        '''用来处理增加人员后，更新增加人员的情况，同刷新本地数据'''
        qs = "select * from wis_person where personStatus = 1 and deviceStatus = 0"
        persons = db.querySQL(qs)
        countP = persons.rowCount()
        if countP > 0:
            i = 0
            while i < countP:
                dic = {}
                person = persons.record(i)
                dic['version'] = '0.2'
                dic['cmd'] = 'query_face'
                dic['per_id'] = person.field('idNo').value()

                dic['id'] = 20
                dic['name'] = ''

                requests.post('http://127.0.0.1:8080/queryFace', data=dic)
                time.sleep(1)
                i += 1

    def addFace(self):
        qs = "select * from wis_person where personStatus = 1 and deviceStatus = 0"
        persons = db.querySQL(qs)
        countP = persons.rowCount()
        if countP > 0:
            i = 0
            while i < countP:
                dic = {}
                person = persons.record(i)
                dic['version'] = '0.2'
                dic['cmd'] = 'create_face'
                dic['per_id'] = person.field('idNo').value()
                dic['face_id'] = person.field('idNo').value()
                dic['per_name'] = person.field('name').value()
                dic['idcardNum'] = person.field('idNo').value()
                dic['idcardper'] = person.field('idNo').value()
                dic['s_time'] = 0
                dic['e_time'] = 10000
                personStatus = person.field('personStatus').value()
                if personStatus == 1:
                    dic['per_type'] = 0
                else:
                    dic['per_type'] = 2

                dic['usr_type'] = 0

                desImg = './photos_face/{}_face.jpg'.format(dic['per_id'])

                with open(desImg, 'rb') as f:
                    bimg = base64.b64encode(f.read())
                dic['img_data'] = bimg

                requests.post('http://127.0.0.1:8080/addFace', data=dic)
                time.sleep(1)
                i += 1
            self.queryResult()

    def deleteFace(self):
        qs = "select * from wis_person where zjptStatus = 2"
        persons = db.querySQL(qs)
        countP = persons.rowCount()
        if countP > 0:
            i = 0
            while i < countP:
                dic = {}
                person = persons.record(i)
                dic['version'] = '0.2'
                dic['cmd'] = 'delete_face'
                dic['per_id'] = person.field('idNo').value()
                dic['type'] = 0

                requests.post('http://127.0.0.1:8080/delFace', data=dic)
                time.sleep(1)
                i += 1

    def personExchange(self):
        self.addFace()
        time.sleep(5)
        self.deleteFace()


class CdzjExchangeInfo:
    '''用于处理与住建交换数据的逻辑'''
    def __init__(self):
        '''各种属性及需要交换的数据'''
        # self.db = Dboperator()
        global db
        self.cdzj = Cdzj()

        self.cjSN = ''
        self.cjKEY = ''
        self.prepare()

    def prepare(self):
        """初始化一些常用的参数，包括成都住建的访问地址，采集设备的SN和KEY"""
        zjqs = "select * from wis_cdzjpt where id = '99'"
        current = db.querySQL(zjqs).record(0)
        self.cdzj.uploadPersonURL = current.field('uploadPersonURL').value()
        self.cdzj.downloadPersonURL = current.field('downloadPersonURL').value()
        self.cdzj.downloadDelPersonURL = current.field('deletePersonURL').value()
        self.cdzj.uploadAttendanceURL = current.field('uploadAttURL').value()
        self.cdzj.feedbackURL = current.field('feedbackURL').value()

        sysSetQs = "select * from wis_sysSet where id = 99"
        currentSysSet = db.querySQL(sysSetQs).record(0)
        self.cjSN = currentSysSet.field('cjSN').value()
        self.cjKEY = currentSysSet.field('cjKEY').value()

    def uploadPersons(self):
        qs = "select * from wis_person where zjptStatus = 0 and uploadYN = 1 and personStatus = 1"
        uploadPersons = db.querySQL(qs)
        countP = uploadPersons.rowCount()
        if countP > 0:
            i = 0
            while i < countP:
                person = uploadPersons.record(i)

                idNo = person.field('idNo').value()
                name = person.field('name').value()

                tbirthday = person.field('birthday').value()
                birthday = tbirthday[0:4] + '-' + tbirthday[4:6] + '-' + tbirthday[6:]

                self.cdzj.person['idNo'] = person.field('idNo').value()
                self.cdzj.person['name'] = person.field('name').value()
                self.cdzj.person['gender'] = person.field('gender').value()
                self.cdzj.person['nation'] = person.field('nation').value()
                self.cdzj.person['birthday'] = birthday
                self.cdzj.person['address'] = person.field('address').value()
                self.cdzj.person['idissue'] = person.field('idissue').value()
                self.cdzj.person['idperiod'] = person.field('idperiod').value()
                self.cdzj.person['idphoto'] = jpgtostr(person.field('idphoto').value())
                self.cdzj.person['photo'] = jpgtostr(person.field('photo').value())
                self.cdzj.person['inf_photo'] = ''
                self.cdzj.person['userType'] = person.field('userType').value()
                self.cdzj.person['dev_mac'] = self.cjSN
                self.cdzj.person['RegType'] = person.field('RegType').value()

                self.cdzj.uploadPerson()
                if self.cdzj.msg_uploadPerson == 'success':
                    qs = "update wis_person set zjptStatus = 1 where idNo = '%s'" % idNo
                    db.excuteSQl(qs)
                    okMsg = "人员:%s,身份证号:%s,%s成功上传到平台\n" % (name, idNo, datetime.datetime.now())
                    with open('uploadPersonsLog.txt', 'a') as f:
                        f.write(okMsg)
                        # f.close()
                else:
                    failMsg = "人员:%s,身份证号:%s,%s上传到平台失败，原因:%s\n" % (name, idNo, datetime.datetime.now(), self.cdzj.msg_uploadPerson)
                    with open('uploadPersonsLog.txt', 'a') as f:
                        f.write(failMsg)
                        # f.close()
                i += 1

    def downloadPersons(self):
        dev_qs = "select * from wis_faceDevice where status = 1"
        devices = db.querySQL(dev_qs)
        countD = devices.rowCount()

        if countD > 0:
            i = 0

            while i < countD:
                faces = devices.record(i)

                sn = str.strip(faces.field('sn').value())
                key = str.strip(faces.field('key').value())

                self.cdzj.downloadPerson(sn, key)
                if self.cdzj.msg_downloadPerson == 'success':
                    for p in self.cdzj.persons:
                        selectQs = "select * from wis_person where idNo = '%s'" % p['idNo']
                        data = db.querySQL(selectQs)
                        countP = data.rowCount()
                        if countP == 1:

                            qs = "update wis_person set user_id = '%s', work_sn = '%s' where idNo = '%s'" % (
                            p['user_id'], p['work_sn'], p['idNo'])
                            db.excuteSQl(qs)

                            self.cdzj.feedback(sn, 2, '下发成功')
                            okMsg = "人员:%s,身份证号:%s,%s成功产生住建号：%s\n" % (data.record(0).field('name').value(), self.cdzj.person['idNo'], datetime.datetime.now(), self.cdzj.person['user_id'])
                            with open('downloadPersonsLog.txt', 'a') as f:
                                f.write(okMsg)
                        else:
                            with open('downloadPersonsLog.txt', 'a') as f:
                                f.write('平台数据与本地数据不一致，姓名：%s，住建号：%s, 身份证号：%s\n' % (p['name'], p['user_id'], p['idNo']))
                else:
                    with open('downloadPersonsLog.txt', 'a') as f:
                        f.write(self.cdzj.msg_downloadPerson)

                i += 1

    def downloadDeletePersons(self):
        dev_qs = "select * from wis_faceDevice where status = 1"
        devices = db.querySQL(dev_qs)
        countD = devices.rowCount()

        if countD > 0:
            i = 0

            while i < countD:
                faces = devices.record(i)

                sn = str.strip(faces.field('sn').value())
                key = str.strip(faces.field('key').value())
                if self.cdzj.msg_downloadDelPerson == 'success':
                    selectQs = "select * from wis_person where user_id = '%s'" % self.cdzj.delPersonID
                    data = db.querySQL(selectQs)
                    countP = data.rowCount()
                    if countP == 1:
                        qs = "update wis_person set zjptStatus = 2 where user_id = '%s'" % self.cdzj.delPersonID
                        db.excuteSQl(qs)

                        okMsg = "人员:%s,身份证号:%s,%s成功删除\n" % (data.record(0).field('name').value(), data.record(0).field('idNo').value(), datetime.datetime.now())
                        with open('downloadDeletePersonsLog.txt', 'a') as f:
                            f.write(okMsg)
                        self.cdzj.feedback(sn, 0, '人员删除成功')
                else:
                    with open('downloadDeletePersonsLog.txt', 'a') as f:
                        f.write(self.cdzj.msg_downloadDelPerson+'\n')
                i += 1
        else:
            with open('downloadDeletePersonsLog.txt', 'a') as f:
                f.write('未找到考勤设备！\n')

    def uploadAttendeces(self):
        rec_qs = '''
                 select wis_recordsx.per_id, wis_recordsx.usec as recog_time, wis_faceDevice.sn as sn, wis_faceDevice.key as devkey, wis_person.user_id as user_id
                 from wis_recordsx, wis_faceDevice, wis_person
                 where wis_recordsx.sn = wis_faceDevice.deviceSn and wis_recordsx.per_id = wis_person.idNo 
                 and wis_recordsx.uploadYN = 0 and wis_person.user_id != ''
                 '''
        atts = db.querySQL(rec_qs)
        att_count = atts.rowCount()
        if att_count > 0:
            i = 0
            while i < att_count:
                att = atts.record(i)
                per_id = att.field('per_id').value()
                sn = att.field('sn').value()
                devkey = att.field('devkey').value()
                user_id = att.field('user_id').value()
                recog_time = att.field('recog_time').value()
                logs = {'sn': sn, 'user_id': user_id, 'recog_time': recog_time, 'recog_type': 'face'}
                logs_list = [logs]

                self.cdzj.attdata = {'Count': 1, 'logs': logs_list}
                self.cdzj.uploadAttendance(sn, devkey)

                if self.cdzj.msg_uploadAttendance == 'success':
                    qs = "update wis_recordsx set uploadYN = 1 where sn = '%s' and usec = '%s', and per_id = '%s'" % (sn, recog_time, per_id)
                    db.excuteSQl(qs)
                    okMsg = "记录：%s, %s, %s 已上传成功\n" % (sn, recog_time, per_id)
                    with open('uploadAttendancesLog.txt', 'a') as f:
                        f.write(okMsg)
                else:
                    with open('uploadAttendancesLog.txt', 'a') as f:
                        f.write(self.cdzj.msg_uploadAttendance + '\n')
                i += 1

    def personExchange(self):
        self.uploadPersons()
        time.sleep(5)
        self.downloadPersons()
        time.sleep(5)
        self.downloadDeletePersons()

    def attendenceExchange(self):
        self.uploadAttendeces()


if __name__ == '__main__':
    # 测试平台是否通，测试设备是否联网
    cdzj_exchange = CdzjExchangeInfo()
    device_exchange = DeviceExchangeInfo()

    while True:
        # 以下为处理设备数据的操作
        if len(device_exchange.devsIPlist) > 0:
            for ip in device_exchange.devsIPlist:
                if ping(ip) == 'on':
                    print('处理人脸设备。。。。')
                    # 找到需要处理的人员信息，未下传到设备的
                    device_exchange.personExchange()
                else:
                    print('设备不在线，等30秒再试')
                    pass
        else:
            print('没有需要处理下发的人脸设备')
            pass

        # 测试住建平台是否可用（暂时只能确保外网通畅）
        if ping('61.139.2.69') == 'on':
            # 如是住建网络通畅，则找到需要处理的人员信息，未上传到住建的，未从住建下载到本地的
            print('处理住建。。。。')
            cdzj_exchange.personExchange()
            cdzj_exchange.uploadAttendeces()
        else:
            print('网络不通，等30秒再试')
            time.sleep(30)



