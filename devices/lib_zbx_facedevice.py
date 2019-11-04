from ctypes import *

# 定义相机结构
class Cam(Structure):
    _fields_ = []


# 定义FaceFlags结构
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


# 定义FaceImage结构
class FaceImage(Structure):
    _fields_ = [
        ('img_seq', c_int),
        ('img_fmt', c_int),
        ('img', c_char_p),
        ('img_len', c_int),
        ('width', c_int),
        ('height', c_int)
    ]


# 定义搜索像机的参数-结构体
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


# 定义增加人脸后返回的人脸信息结构
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

# class ZBSFaceLib:
#     dll = windll.LoadLibrary('libFaceRecognitionSDK_x86.dll')
#
#     zbx_InitEx = dll.ZBX_InitEx
#     zbx_InitEx.argtype = (c_int,)
#     zbx_InitEx.restype = c_void_p
#
#     zbx_SetNotifyConnected = dll.ZBX_SetNotifyConnected
#     zbx_SetNotifyConnected.argtype = (c_int,)
#     zbx_SetNotifyConnected.restype = c_void_p
#
#     zbx_ConnectEventCb_t = CFUNCTYPE(None, POINTER(IpScan_t), c_int)
#
#     zbx_ZBX_RegDiscoverIpscanCb = dll.ZBX_RegDiscoverIpscanCb
#     zbx_ZBX_RegDiscoverIpscanCb.argtype = (zbx_ZBX_RegDiscoverIpscanCb, c_int)
#     zbx_ZBX_RegDiscoverIpscanCb.restype = c_void_p
#
#     zbx_DiscoverIpscan = dll.ZBX_DiscoverIpscan
#
#     zbx_ConnectEx = dll.ZBX_ConnectEx
#     zbx_ConnectEx.argtype = (POINTER(c_char), c_ushort, POINTER(c_char), POINTER(c_char), POINTER(c_int), c_uint, c_int, c_bool)
#     zbx_ConnectEx.restype = c_void_p
#
#     zbx_FaceQueryCb_t =CFUNCTYPE(None, POINTER(Cam), POINTER(QueryFaceInfo), POINTER(c_int))
#     zbx_RegFaceQueryCb = dll.ZBX_RegFaceQueryCbEx
#     zbx_RegFaceQueryCb.argtype = (POINTER(Cam), zbx_FaceQueryCb_t, POINTER(c_int))
#
#     zbx_AddJpgFaces = dll.ZBX_AddJpgFaces
#     zbx_AddJpgFaces.argtype = (POINTER(Cam), POINTER(FaceFlags), POINTER(FaceImage), c_int, c_int)
#     zbx_AddJpgFaces.restype = c_uint





