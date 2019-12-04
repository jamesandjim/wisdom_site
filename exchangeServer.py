import os
import sys
import time
import random
from PyQt5.QtCore import QTimer

from commTools.netUtil import ping
from models.dbtools import Dboperator
from cdzjpt import Cdzj


class ExchangeInfo:
    '''用于处理与住建交换数据的逻辑'''
    def __init__(self):
        '''各种属性及需要交换的数据'''
        self.cdzj = Cdzj()
        self.faceDevs = None
        self.persons = None

    def forCdzj(self):
        print('处理住建数据')

    def forDevice(self):
        print('处理设备数据')


if __name__ == '__main__':
    # 测试平台是否通，测试设备是否联网
    ex = ExchangeInfo()

    while True:
        db = Dboperator()
        # 测试住建平台是否可用（暂时只能确保外网通畅）

        if ping('61.139.2.69') == 'on':
            # 如是住建网络通畅，则找到需要处理的人员信息，未上传到住建的，未从住建下载到本地的
            qs = "select * from wis_person where uploadYN = 1 and personStatus = 1 and zjptStatus = 0"
            pers = db.querySQL(qs)
            pers_conut = pers.rowCount()
            if pers_conut > 0:
                i = 0
                while i < pers_conut:
                    per = pers.record(i)

            r = [True, False]
            running = random.choice(r)
            if not running:
                # 处理交换事项
                ex.forCdzj()

                print('数据处理中。。。。。。')
                time.sleep(5)
            else:
                print('没有需处理数据，等30秒再试')
                time.sleep(2)
        else:
            print('网络不通，等30秒再试')
            time.sleep(30)

        if ping(ip) == 'on':
            # 找到需要处理的人员信息，未下传到设备的
            ex.forFaceDev()
        else:
            print('设备不在线，等30秒再试')
            time.sleep(30)

