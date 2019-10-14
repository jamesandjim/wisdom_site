from ctypes import *


class FaceDevice:
    '''定义人脸考勤设备的操作'''
    def __init__(self):
        self.dll = windll.LoadLibrary('jbnvsdk.dll')
        self.SrcFacePos = FacePos()
        self.DstFacePos = FacePos()
        self.facePos_end = {}
        self.pInputImage = InputImage()
        self.hwnd = pointer(c_uint())
        self.msg = create_string_buffer(256) #调用函数后返回的信息

    def searchServer(self):
        pass

    def openServer(self, ip):
        result = self.dll.JBNV_OpenServer(ip.encode(), 8200, b'admin', b'admin', byref(self.hwnd))
        if result:
            self.dll.JBNV_GetErrorMessage(result, byref(self.msg), 256, 0x00000804)
            return False
        else:
            return True

    def closeServer(self):
        result = self.dll.JBNV_CloseServer(self.hwnd)
        if result:
            self.dll.JBNV_GetErrorMessage(result, byref(self.msg), 256, 0x00000804)
            return False
        else:
            return True

    def getFacePos(self, srcImg, dstImg):
        result = self.dll.JBNV_GetFaceImage(srcImg.encode(), dstImg.encode(), byref(self.pInputImage), byref(self.SrcFacePos), byref(self.DstFacePos))
        if result:
            self.dll.JBNV_GetErrorMessage(result, byref(self.msg), 256, 0x00000804)
            return False
        else:
            self.facePos_end['x'] = self.DstFacePos.left
            self.facePos_end['y'] = self.DstFacePos.top
            self.facePos_end['w'] = self.DstFacePos.right - self.facePos_end.left
            self.facePos_end['h'] = self.DstFacePos.bottom - self.facePos_end.top

            return True

    def addPerson(self):
        pass

    def delPerson(self):
        pass

    def updatePerson(self):
        pass

    def queryPerson(self):
        pass

    def queryPersonPart(self):
        pass

    def delAllPerson(self):
        pass

    def queryRecordPart(self):
        pass

    def queryRecordTime(self):
        pass

    def ipconfig(self):
        pass

    def openDoor(self):
        pass

    def setTime(self):
        pass

    def getTime(self):
        pass

    def faceConfig(self):
        pass

    def serverUrlConfig(self):
        pass

    

    # c = c_uint(1)
    #
    # result = dll.JBNV_OpenServer(b'192.168.0.201', 8200, b'admin', b'admin', byref(hwnd))
    # if result:
    #     c = dll.JBNV_GetErrorMessage(result, byref(msg), 256, 0x00000804)
    #
    # else:
    #     r = dll.JBNV_GetFaceImage(b"timg.jpg", b"out.jpg", byref(pInputImage), byref(SrcFacePos), byref(DstFacePos))
    #
    #     c = dll.JBNV_GetErrorMessage(r, byref(msg), 256, 0x00000804)
    #     print(pInputImage.x)
    #     print(pInputImage.y)
    #     print(SrcFacePos.left)
    #     print(SrcFacePos.top)
    #     print(SrcFacePos.right)
    #     print(SrcFacePos.bottom)
    #     print(DstFacePos.left)
    #     print(DstFacePos.top)
    #     print(DstFacePos.right)
    #     print(DstFacePos.bottom)
    # print(msg.value.decode('gbk'))


class InputImage(Structure):
    _fields_ = [
        ('x', c_uint),
        ('y', c_uint)
    ]


class FacePos(Structure):
    _fields_ = [
        ('left', c_uint),
        ('top', c_uint),
        ('right', c_uint),
        ('bottom', c_uint),
    ]



