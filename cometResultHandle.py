# 处理HTTP服务器返回的数据
import json
import time
from models.dbtools import Dboperator

from infoAgent import Info


class ResultHandle:
    def __init__(self, dic):
        self.dic = dic
        self.db = Dboperator()
        self.prepare()

    def prepare(self):
        last_result = self.dic['last_result']
        if last_result != '1':
            lr = json.loads(last_result)
            print(lr)
            cmd = lr['cmd']
            code = lr['code']
            reply = lr['reply']

            if cmd == 'create_face':
                if code == 0:

                    print('人员增加成功！')

                else:
                    print(reply)
            elif cmd == 'query_face':
                if code == 0:
                    qs = "update wis_person set deviceStatus = 1 where idNo = '%s'" % lr['per_id']
                    self.db.excuteSQl(qs)
                    print('查询成功！')
            elif cmd == 'delete_face':
                if lr['code'] == 0:

                    print('人员删除成功！')
                else:
                    print(lr['reply'])
            elif cmd == 'update_face':
                print('update_face')
            elif cmd == 'reboot_cam':
                print('reboot_cam')
            elif cmd == 'ss_set_timing':
                print('ss_set_timing')
            elif cmd == 'set_spoofing':
                print('set_spoofing')
            elif cmd == 'set_attr':
                print('set_attr')
            elif cmd == 'set_voice_cfg':
                print('set_voice_cfg')
            elif cmd == 'set_sleep_time':
                print('set_sleep_time')
            elif cmd == 'set_reco_mode':
                print('set_reco_mode')
            elif cmd == 'set_hat_pass':
                print('set_hat_pass')
            elif cmd == 'set_face_mode':
                print('set_face_mode')
            elif cmd == 'error':
                print('命令错误')
            else:
                pass

    def addFaceHandle(self):
        print('处理人员增加成功后事宜')


class RecordHandle:
    def __init__(self, dic):
        self.dic = dic
        self.db = Dboperator()

    def insertdb(self):
        jn = self.dic['body']
        dtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(jn['usec'])-8*60*60))
        per_id = jn['per_id']
        sn = jn['sn']
        qs = '''
                insert into wis_recordsx values ('%s', '%s', %d,'%s', %d, '%s','%s', %d, %d, %d, %d,'%s','%s', %d)
                ''' % (jn['sequence'], jn['sn'], jn['usec']-8*60*60, dtime, int(jn['matched']), jn['per_id'], jn['name'], int(jn['role']), int(jn['hat']), int(jn['face_imgsize']), int(jn['model_imgsize']), jn['face_imgdata'], '', 0)
        self.db.excuteSQl(qs)
        qs = "select wis_faceDevice.location from wis_faceDevice where wis_faceDevice.deviceSn ='%s'" % sn
        inOrout = self.db.querySQL(qs).record(0).field('location').value()

        qs = "select wis_person.department from wis_person where wis_person.idNo = '%s'" % per_id
        departs = self.db.querySQL(qs)
        deName = departs.record(0).field('department').value()
        if inOrout == '入口设备':
            qs1 = "update wis_department set currentNum = currentNum + 1 where name = '%s'" % deName
        if inOrout == '出口设备':
            qs1 = "update wis_department set currentNum = currentNum - 1 where name = '%s'" % deName
        self.db.excuteSQl(qs1)
