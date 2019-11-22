from PyQt5.QtWidgets import QWidget, QDialog, QMessageBox
from PyQt5.QtCore import pyqtSlot, QModelIndex, Qt
from PyQt5.QtGui import QCursor, QMouseEvent

from views import loginUi
from models.dbtools import Dboperator


class LoginWindow(QDialog, loginUi.Ui_login):
    def __init__(self, parent=None, mode=0):
        super(LoginWindow, self).__init__(parent)
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        # self.setAttribute(Qt.WA_TranslucentBackground)
        self.db = Dboperator()
        self.mode = mode

    @pyqtSlot()
    def on_pb_login_clicked(self):
        name = self.le_userName.text()
        passWord = self.le_passWord.text()
        qs = "select * from wis_operator where name = '%s' and password = '%s'" % (name.strip(), passWord.strip())
        queryModel = self.db.querySQL(qs)
        count = queryModel.rowCount()
        if count == 1:
            self.accept()
        else:

            QMessageBox.information(self, '提示', '用户名或密码错误！', QMessageBox.Yes)
            self.le_userName.clear()
            self.le_passWord.clear()

    @pyqtSlot()
    def on_pb_esc_clicked(self):
        self.close()

    def mousePressEvent(self, QMouseEvent):

        if QMouseEvent.button() == Qt.LeftButton:
            self.flag = True

            self.m_Position = QMouseEvent.globalPos() - self.pos()

            QMouseEvent.accept()

            self.setCursor(QCursor(Qt.OpenHandCursor))

    def mouseMoveEvent(self, QMouseEvent):

        if Qt.LeftButton and self.flag:
            self.move(QMouseEvent.globalPos() - self.m_Position)

            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):

        self.flag = False

        self.setCursor(QCursor(Qt.ArrowCursor))