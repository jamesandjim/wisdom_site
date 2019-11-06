from PyQt5 import QtCore
import time

from PyQt5.QtMultimediaWidgets import QCameraViewfinder
from PyQt5.QtMultimedia import QCamera

x = QCamera()
a = x.captureMode()
print(a)




