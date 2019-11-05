# 处理HTTP服务器返回的数据
import json
import time
from models.dbtools import Dboperator


class ResultHandle:
    def __init__(self, dic):
        self.dic = dic
        self.prepare()

    def prepare(self):
        last_result = self.dic['last_result']
        if last_result != '':
            lr = json.loads(last_result)
            cmd = lr['cmd']

            if cmd == 'create_face':
                print('create_face')
            elif cmd == 'query_face':
                print('query_face')
                self.queryFaceHandle()
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

    def queryFaceHandle(self):
        print('查询到数据')


class RecordHandle:
    def __init__(self, dic):
        self.dic = dic
        self.db = Dboperator()

    def insertdb(self):
        jn = self.dic['body']
        dtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(jn['usec']))
        qs = '''
                insert into wis_records values ('%s', %d, %d, '%s', '%s', '%s', %d, %d, %d, %d, %d, %d, %d, %d, %d, '%s', '%s', 0)
                ''' % (jn['per_id'], 1, jn['matched'], dtime, jn['face_imgdata'], jn['sn'], 0, 1, 0, jn['hat'], 0, 0, 2, 0, jn['role'], jn['sn'], '')
        self.db.excuteSQl(qs)
