from ctypes import *
from pathlib import Path, PurePath, PureWindowsPath


dll = WinDLL('jbnvsdk.dll')

hwnd = c_int32()

dll.JBNV_SearchServer(hwnd, 1)

print(hwnd)

