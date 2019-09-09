from ctypes import *
import json
import PIL
from PIL import Image
from PyQt5.Qt import QImage, QPixmap

import base64

class CardReader:
    def __init__(self):
        self.dev = WinDLL("../dll/kl/cardreaderkt5.dll")
        self.url = "{\"continueRead\":1, \"uri\":\"wss://idcard.kaercloud.top//socket\"}"
        self.p = c_int32()
        # self.p = pointer(c_size_t())
        # self.p = c_size_t()

    def openDevice(self):

        r = self.dev.KT_Dev_Open(5, reader.url, pointer(self.p))
        return r

    def readCard(self):
        wzData = create_string_buffer(1024)
        zpData = create_string_buffer(1024)

        r = self.dev.KT_Dev_ReadIDCard(self.p, wzData, zpData)

        outStr = create_string_buffer(500)
        i = c_int32(500)

        r1 = self.dev.KT_ParseIDCardInfo(wzData, outStr, pointer(i))

        if r1 == 8:
            outStr = create_string_buffer(i)
            r2 = self.dev.KT_ParseIDCardInfo(wzData, outStr, pointer(i))

        print(json.loads(outStr.value.decode('gbk')))

        img_len = c_int32(5000)
        img = create_string_buffer(img_len.value)
        print(img_len.value)

        photo_size = (358, 441)

        r2 = self.dev.KT_WltUnpack(zpData, b'JPG', -1, img, pointer(img_len))
        with open('1.jpg', 'wb') as f:
            f.write(img)


    def closeDevice(self):
        if self.dev.KT_Dev_Close() == 0:
            return True
        else:
            return False




if __name__ == "__main__":
    reader = CardReader()
    reader.openDevice()
    reader.readCard()



