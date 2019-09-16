from ctypes import *

from pathlib import Path, PurePath, PureWindowsPath


dll = WinDLL('jbnvsdk.dll')

hwnd = pointer(c_uint())

class ServerInfo(Structure):
    _fields_ = [
        ('dwSize', c_ulong),
        ('dwServerFlag', c_ulong),
        ('dwServerIp', c_ulong),
        ('szServerIp', c_char*16),
        ('wServerPort', c_ushort),
        ('wChannelNum', c_short),
        ('dwVersionNum', c_ushort),
        ('szServerName', c_char*32),
        ('dwServerCPUType', c_ulong),
        ('bServerSerial', c_ubyte*48),
        ('byMACAddr', c_ubyte*6),
        ('dwAlarmInCount', c_ulong),
        ('dwAlarmOutCount', c_ulong),
        ('dwSysFlags', c_ulong),
        ('dwUserRight', c_ulong),
        ('csServerDes', c_char*64)

    ]


class Status(Structure):
    _fields_ = [
        ('st1', c_ubyte*64),
        ('st2', c_ubyte*256)

    ]

# dll.JBNV_SearchServer(byref(hwnd), 1)
x = dll.JBNV_OpenServer('192.168.0.201', 8200, 'admin', 'admin', byref(hwnd))
serverInfo = ServerInfo()
stat = Status()
stauts = dll.JBNV_GetServerNetStatus(hwnd, byref(stat))
print(stauts)
print(stat.st1[:])
y = dll.JBNV_GetServerInfo(hwnd, byref(serverInfo))

print(serverInfo.dwSize)
print(x)
print(y)

print(type(hwnd))

