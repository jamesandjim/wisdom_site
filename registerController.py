import time
from PyQt5.QtWidgets import QWidget, QDialog, QMessageBox
from PyQt5.QtCore import pyqtSlot

from views import registerUi
from devices.computerInfo import printDisk, forzc
from models.dbtools import Dboperator


class RegisterWindow(QDialog, registerUi.Ui_Dialog):
    def __init__(self, parent=None):
        super(RegisterWindow, self).__init__(parent)
        self.setupUi(self)
        self.xlh = ''
        self.registerTime = time.time()
        self.getXlh()
        self.db = Dboperator()

    def getXlh(self):
        disk = printDisk()
        self.xlh = disk[0]['UUID']
        self.lineEdit_xlh.setText(self.xlh)

    @pyqtSlot()
    def on_pb_esc_clicked(self):
        self.close()

    @pyqtSlot()
    def on_pb_ok_clicked(self):
        company = self.lineEdit_company.text()
        zcm = forzc(str.strip(self.lineEdit_xlh.text()))
        if company != '' and zcm != '':
            if str.strip(self.lineEdit_zcm.text()) == zcm:
                self.accept()
                qs = "update wis_sysSet set zcm = '%s', company = '%s', registerTime = %d" % (zcm, company, self.registerTime)
                self.db.excuteSQl(qs)
            else:
                self.reject()
        else:
            QMessageBox.information(self, '提示', '公司名和注册码不能为空！', QMessageBox.Yes)



