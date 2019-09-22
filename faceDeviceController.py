from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5.QtCore import pyqtSlot, QModelIndex

from models.dbtools import Dboperator

from views import faceDeviceUi


class FaceDeviceWindow(QWidget, faceDeviceUi.Ui_Form):
    def __init__(self, parent=None):
        super(FaceDeviceWindow, self).__init__(parent)
        self.setupUi(self)
        self.db = Dboperator()