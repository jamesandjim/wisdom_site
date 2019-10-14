from ctypes import *


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

class facePos:
    def __init__(self):
        self.SrcFacePos = FacePos()
        self.DstFacePos = FacePos()
        self.pInputImage = InputImage()

