# 处理HTTP服务器返回的数据
import json
import time
from models.dbtools import Dboperator

from infoAgent import Info


class ResultHandle:
    def __init__(self, dic):
        self.dic = dic
        self.prepare()

    def prepare(self):
        last_result = self.dic['last_result']
        if last_result != '':
            lr = json.loads(last_result)
            cmd = lr['cmd']
            code = lr['code']
            reply = lr['reply']

            if cmd == 'create_face':
                if code == 0:
                    print('%s 人员增加成功！' % self.dic['ipaddr'])
                    '''todo  修改数据库中对应人员记录，将已上传改为1'''

                else:
                    print(reply)
            elif cmd == 'query_face':
                print('query_face')
                return lr['per_id']
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
        dtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(jn['usec']))
        qs = '''
                insert into wis_recordsx values ('%s', '%s', %d, '%s','%s', %d, %d, %d, %d,'%s','%s', %d)
                ''' % (jn['sn'], dtime, int(jn['matched']), jn['per_id'], jn['name'], int(jn['role']), int(jn['hat']), int(jn['face_imgsize']), int(jn['model_imgsize']), jn['face_imgdata'], jn['model_imgdata'], 0)
        self.db.excuteSQl(qs)
