from ctypes import *
import sys


#定义搜索像机的参数-结构体
class IpScan_t(Structure):
    _fields_ = [
        ('mac', c_char*20),
        ('ip', c_char*20),
        ('netmask', c_char*20),
        ('manufacturer', c_char*16),
        ('platform', c_char*32),
        ('system', c_char*32),
        ('version', c_char*64),
        ('usr_type', c_int)
    ]


# 人脸信息结构体
class QueryFaceInfo(Structure):
    _field_ = [
        ('record_count', c_int),
        ('record_no', c_int),
        ('personID', c_char*20),
        ('personName', c_byte*16),
        ('role', c_int),
        ('feature_count', c_short),
        ('feature_size', c_short),
        ('feature', POINTER(c_int*5)),
        ('imgNum', c_int),
        ('imgSize', c_int*5),
        ('imgFmt', c_char*20),
        ('imgBuff', POINTER(c_int*5)),
        ('wgCardNo', c_uint),
        ('effectTime', c_uint),
        ('effectStartTime', c_uint)
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



dll = windll.LoadLibrary('libFaceRecognitionSDK_x86.dll')
dll.ZBX_InitEx(100)
dll.ZBX_SetNotifyConnected(1)

# 定义回调函数
# @WINFUNCTYPE(None, POINTER(IpScan_t), c_int)
# def callback(ipScan, usr):
#     print(ipScan.contents.mac)
#     print(ipScan.contents.ip)
#     print(ipScan.contents.netmask)


# 注册搜索回调函数
# dll.ZBX_RegDiscoverIpscanCb(callback, 0)

# 搜索像机
# dll.ZBX_DiscoverIpscan()

errNo = c_int()

cam = pointer(c_int())
cam = dll.ZBX_ConnectEx(b'192.168.0.105', 8099, '', '', byref(errNo), 1, 1, True)

# r = dll.ZBX_Connected(cam)
# print(r)

# 注册人脸回调

@WINFUNCTYPE(None, POINTER(c_int), POINTER(QueryFaceInfo), c_int)
def regFaceQueryCB(x, y, z):
    print(y.contents.personName)


dll.ZBX_RegFaceQueryCb(cam, regFaceQueryCB, 0)
flags = FaceFlags(b'12356', b'jamesye', 0, 1, 0xFFFFFFFF, 0, 0, b'')
with open('ymg.jpg', 'rb') as f:
    file = f.read()

print(type(file))

size = sys.getsizeof(file)

print(size)

img = FaceImage(1, 0, file, size)
dll.ZBX_AddJpgFaces(cam, flags, img, 1, 0)

while True:
    pass






