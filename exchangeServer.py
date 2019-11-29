import os
import sys
import time
import random
from PyQt5.QtCore import QTimer

from commTools.netUtil import ping


class ExchangeInfo:
    def __init__(self):
        '''各种属性及需要交换的数据'''

        self.faceDevs = None
        self.persons = None

    def forCdzj(self):
        print('处理住建数据')

    def forFaceDev(self):
        print('处理设备数据')


if __name__ == '__main__':
    # 测试平台是否通，测试设备是否联网
    ex = ExchangeInfo()

    while True:
        iplist = ['61.139.2.69', '8.8.8.8', '5.5.5.5', '192.168.0.201', '192.168.0.222']
        ip = random.choice(iplist)
        print(ip)

        if ping(ip) == 'on':
            # todo 查询数据库中的值，确认现在有没有进行数据交换操作,将值赋给running
            r = [True, False]
            running = random.choice(r)
            if not running:
                # 处理交换事项
                ex.forCdzj()
                ex.forFaceDev()
                print('数据处理中。。。。。。')
                time.sleep(5)
            else:
                print('没有需处理数据，等30秒再试')
                time.sleep(2)
        else:
            print('网络不通，等30秒再试')
            time.sleep(1)
