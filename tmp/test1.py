from devices.lib_zbx_facedevice import FaceImage, FaceFlags, QueryFaceInfo, Cam, IpScan_t
from ctypes import *
import sys

face = windll.LoadLibrary('libFaceRecognitionSDK_x86.dll')

face.ZBX_InitEx(100)

face.ZBX_SetNotifyConnected(1)

# @WINFUNCTYPE(None, POINTER(IpScan_t), c_int)
# def callback(ipscan, usr):
#     print('ok')
#     print(ipscan.contents.mac)

@WINFUNCTYPE(None, POINTER(Cam), POINTER(QueryFaceInfo), POINTER(c_int))
def callback1(cam, info, usr):
    print('info.contents')

# face.ZBX_RegDiscoverIpscanCb(callback, 0)

# face.ZBX_DiscoverIpscan()

errNo = create_string_buffer(50)

cam = POINTER(c_int)

cam = face.ZBX_ConnectEx(b'192.168.0.105', 8099, '', '', byref(errNo), 1, 1, True)

face.ZBX_RegFaceQueryCb(cam, callback1, 0)

flags = FaceFlags(b'12357', b'jamesye', 0, 1, 0xFFFFFFFF, 0, 0, b'')

with open('ymg.jpg', 'rb') as f:
    file = f.read()

size = sys.getsizeof(file)

img = FaceImage(1, 0, file, size)

face.ZBX_AddJpgFaces(cam, byref(flags), byref(img), 1, 0)

while True:
    pass
