from ctypes import *
from ctypes import wintypes
import cv2
import base64
import os
import sys
import mmap


class IpScan_t(Structure):
    _fields_ = [
        ('mac', c_char*20),
        ('ip', c_char*20),
        ('netmask', c_char*20),
        ('manufacturer', c_char*16),
        ('platform', c_char*32),
        ('system', c_char * 32),
        ('version', c_char * 64),
        ('usr_type', c_int)
    ]

class ZBXSdkVersion(Structure):
    _fields_ = [
        ('sdk_version', c_char*64),
        ('protocl_version', c_char*64),
        ('sdk_code_version', c_char*64),
        ('min_firmware_ver', c_char*64),
        ('algorithm_version', c_char*64)
    ]


class FaceFlags(Structure):
    _fields_ = [
        ('faceID', c_char*20),
        ('faceName', c_char*16),
        ('role', c_int),
        ('wgCardNO', c_uint),
        ('effectTime', c_uint),
        ('effectStartTime', c_uint),
        ('version', c_short),
        ('resv', c_char*8182)
    ]


class FaceImage(Structure):
    _fields_ = [
        ('img_seq', c_int),
        ('img_fmt', c_int),
        ('img', c_char_p),
        ('img_len', c_int),
        ('width', c_int),
        ('height', c_int)
    ]


class Cam(Structure):
    _fields_ = []


class FaceDevice:
    def __init__(self):
        self.dll = windll.LoadLibrary('libFaceRecognitionSDK_x86.dll')
        self.msg = ''
        self.x = IpScan_t()
        self.y = 0
        self.cam = Cam()
        self.prpareUse()

        self.ipscan_cb_t = WINFUNCTYPE(None, POINTER(IpScan_t), c_int)

        # self.registGlobal()

        self.getdevice = self.dll.ZBX_DiscoverIpscan
        self.getdevice.argtype = ()
        self.getdevice.restype = c_void_p


    def prpareUse(self):
        self.dll.ZBX_InitEx(100)
        self.dll.ZBX_SetNotifyConnected(1)

    @staticmethod
    def registGlobal(self):

        cb = self.ipscan_cb_t(discover_ipscan_cb_t)

        self.dll.ZBX_RegDiscoverIpscanCb(self.ipscan_cb_t(discover_ipscan_cb_t), 0)

    @staticmethod
    def connect(self, errNo):
        self.cam = self.dll.ZBX_ConnectEx(b'192.168.0.105', 8099, '', '', byref(errNo), 1, 1, True)

    def getLedMode(self):
        mode = c_char()
        self.dll.ZBX_GetLedMode(self.cam, byref(mode))
        return mode.value.decode('utf-8')

    def setLedMode(self, mode):
        self.dll.ZBX_SetLedMode(self.cam, mode)

    def addFace(self, flags, img):

        r = self.dll.ZBX_AddJpgFaces(self.cam, byref(flags), byref(img), 1, 0)
        return r


    def trigger(self):
        r = self.dll.ZBX_Trigger(self.cam, 0)
        return r

    def __del__(self):
        self.dll.ZBX_DeInit()


def discover_ipscan_cb_t(x, y):
    print('ok, %s' % x.contents.mac)
    return None


if __name__ == '__main__':
    face = FaceDevice()



    err = c_int()
    err = POINTER(c_int)
    face.connect(err)
    mode = face.getLedMode()

    print(mode)
    face.setLedMode(2)
    mode = face.getLedMode()
    print(mode)

    flags = FaceFlags(b'123456', b'jamesye', 0, 1, 0xFFFFFFFF, 0, 0, b'')
    with open('123.jpg', 'rb') as f:
        file = f.read()

    print(type(file))

    size = sys.getsizeof(file)

    print(size)

    img = FaceImage(1, 0, file, size)
    r = face.addFace(flags, img)

    print(r)

    r = face.trigger()
    print(r)

    face.getdevice()










