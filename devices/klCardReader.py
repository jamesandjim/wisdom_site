from ctypes import *
import json
import os
import logging
from pathlib import Path, PurePath

class CardReader:

    def __init__(self):
        # 用于pyinstaller打包的文件路径
        # self.BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        # self.dllDir = os.path.join(self.BASE_DIR, 'dll\kl\cardreaderkt5.dll')
        # self.dll = WinDLL(self.dllDir)

        # 用于直接在pycharm中测试运行的文件路径
        self.dll = WinDLL('./dll/kl/cardreaderkt5.dll')

        # self.homeDir = Path.home()
        # self.dllDir = PurePath(self.homeDir, 'dll/kl', 'cardreaderkt5.dll')

        # continueRead 为1表示可连续读卡，为0则读下张卡时必须拿开再放
        self.url = "{\"continueRead\":1, \"uri\":\"wss://idcard.kaercloud.top//socket\"}"
        # C语言的INT类型，配合byref,pointer使用。表示先开设定数据类型内存区，然后，在方法执行后，传值。
        self.dev = c_int32()
        self.info = {}
        # self.p = pointer(c_size_t())
        # self.p = c_size_t()
        # logger = logging.getLogger()
        fh = logging.FileHandler('klreader.log')
        # fh = logging.StreamHandler()

        fh.setLevel(logging.DEBUG)

    def openDevice(self):
        try:
            r = self.dll.KT_Dev_Open(5, self.url, pointer(self.dev))
            return r
        except Exception as e:
            return e

    def readCard(self):
        # 身份证基本信息
        wzData = create_string_buffer(1024)
        # 身份证照片
        zpData = create_string_buffer(1024)
        try:
            r = self.dll.KT_Dev_ReadIDCard(self.dev, wzData, zpData)

            if r == 0:
                outStr = create_string_buffer(500)
                outStr_len = c_int32(500)

                r1 = self.dll.KT_ParseIDCardInfo(wzData, outStr, pointer(outStr_len))
                if r1 == 8:
                    outStr = create_string_buffer(outStr_len)
                    r2 = self.dll.KT_ParseIDCardInfo(wzData, outStr, pointer(outStr_len))

                self.info = json.loads(outStr.value.decode('gbk'))
                #print(self.info)

                img_len = c_int32(5000)
                img = create_string_buffer(img_len.value)

                r2 = self.dll.KT_WltUnpack(zpData, b'JPG', -1, img, pointer(img_len))
                cardNo = self.info['cardNo']
                with open('./photos_kl/{}.jpg'.format(cardNo), 'wb') as f:
                    f.write(img)
                return 0
            else:
                return 1
        except Exception as e:
            return e

    def closeDevice(self):
        try:
            r = self.dll.KT_Dev_Close(self.dev)
            return r
        except Exception as e:
            return e
        return






