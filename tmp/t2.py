from ctypes import *

dll = windll.LoadLibrary('jbnvsdk.dll')


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


SrcFacePos = FacePos()
DstFacePos = FacePos()

pInputImage = InputImage()

hwnd = pointer(c_uint())
#hwnd = create_string_buffer(20)
msg = create_string_buffer(256)
c = c_uint(1)

r = dll.JBNV_GetFaceImage(b"timg.jpg", b"out.jpg", byref(pInputImage), byref(SrcFacePos), byref(DstFacePos))

c = dll.JBNV_GetErrorMessage(r, byref(msg), 256, 0x00000804)
print(msg.value.decode('gbk'))

print(pInputImage.x)
print(pInputImage.y)
print(SrcFacePos.left)
print(SrcFacePos.top)
print(SrcFacePos.right)
print(SrcFacePos.bottom)
print(DstFacePos.left)
print(DstFacePos.top)
print(DstFacePos.right)
print(DstFacePos.bottom)


# hwnd = pointer(c_uint())

# class ServerInfo(Structure):
#     _fields_ = [
#         ('dwSize', c_ulong),
#         ('dwServerFlag', c_ulong),
#         ('dwServerIp', c_ulong),
#         ('szServerIp', c_char*16),
#         ('wServerPort', c_ushort),
#         ('wChannelNum', c_short),
#         ('dwVersionNum', c_ushort),
#         ('szServerName', c_char*32),
#         ('dwServerCPUType', c_ulong),
#         ('bServerSerial', c_ubyte*48),
#         ('byMACAddr', c_ubyte*6),
#         ('dwAlarmInCount', c_ulong),
#         ('dwAlarmOutCount', c_ulong),
#         ('dwSysFlags', c_ulong),
#         ('dwUserRight', c_ulong),
#         ('csServerDes', c_char*64)

#     ]


# class Status(Structure):
#     _fields_ = [
#         ('st1', c_ubyte*64),
#         ('st2', c_ubyte*256)

#     ]

# # dll.JBNV_SearchServer(byref(hwnd), 1)
# x = dll.JBNV_OpenServer('192.168.0.201', 8200, 'admin', 'admin', byref(hwnd))
# serverInfo = ServerInfo()
# stat = Status()
# stauts = dll.JBNV_GetServerNetStatus(hwnd, byref(stat))
# print(stauts)
# print(stat.st1[:])
# y = dll.JBNV_GetServerInfo(hwnd, byref(serverInfo))

# print(serverInfo.dwSize)
# print(x)
# print(y)

# print(type(hwnd))

