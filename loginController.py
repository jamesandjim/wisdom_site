from PyQt5.QtWidgets import QWidget, QDialog
from PyQt5.QtCore import pyqtSlot, QModelIndex, Qt

from views import loginUi


class LoginWindow(QDialog, loginUi.Ui_login):
    def __init__(self, parent=None, mode=0):
        super(LoginWindow, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.mode = mode

    @pyqtSlot()
    def on_pb_login_clicked(self):
        self.accept()

    @pyqtSlot()
    def on_pb_esc_clicked(self):
        self.close()