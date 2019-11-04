from ctypes import *


#定义搜索像机的参数-结构体
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


dll = windll.LoadLibrary('libFaceRecognitionSDK_x86.dll')
dll.ZBX_InitEx(100)
dll.ZBX_SetNotifyConnected(1)

# 定义回调函数
@WINFUNCTYPE(None, POINTER(IpScan_t), c_int)
def callback(ipscan, usr):
    print(ipscan.contents.mac)


# 注册搜索回调函数
dll.ZBX_RegDiscoverIpscanCb(callback, 0)

# 搜索像机
dll.ZBX_DiscoverIpscan()
while True:
    pass