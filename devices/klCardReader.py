from ctypes import *
import base64


class CardReader:
    def __init__(self):
        self.dev = WinDLL("../dll/jbnv/JBNVSDK.dll")



if __name__ == "__main__":
    reader = CardReader()

