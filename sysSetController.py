from PyQt5.QtWidgets import QWidget, QFileDialog
from PyQt5.QtCore import pyqtSlot

from views import sysSetUi

from models.dbtools import Dboperator


class SysSetWindow(QWidget, sysSetUi.Ui_Form):
    def __init__(self, parent=None):
        super(SysSetWindow, self).__init__(parent)
        self.setupUi(self)
        self.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        self.db = Dboperator()
        self.load()

    def enableAll(self):
        self.checkBox_photoBdYN.setEnabled(True)
        self.checkBox_aqmYN.setEnabled(True)
        self.checkBox_htzdclYN.setEnabled(True)
        self.comboBox_zjptName.setEnabled(True)
        self.checkBox_zjptYN.setEnabled(True)
        self.spinBox_htzkclTime.setEnabled(True)
        self.le_localServer.setEnabled(True)
        self.le_backupUrl.setEnabled(True)
        self.pb_selectPath.setEnabled(True)
        self.le_cjSN.setEnabled(True)
        self.le_cjKEY.setEnabled(True)
        self.pb_save.setEnabled(True)

    def disableAll(self):
        self.checkBox_photoBdYN.setEnabled(False)
        self.checkBox_aqmYN.setEnabled(False)
        self.checkBox_htzdclYN.setEnabled(False)
        self.comboBox_zjptName.setEnabled(False)
        self.checkBox_zjptYN.setEnabled(False)
        self.spinBox_htzkclTime.setEnabled(False)
        self.le_localServer.setEnabled(False)
        self.le_backupUrl.setEnabled(False)
        self.pb_selectPath.setEnabled(False)
        self.le_cjSN.setEnabled(False)
        self.le_cjKEY.setEnabled(False)
        self.pb_save.setEnabled(False)

    def load(self):
        """装载系统参数"""
        qs = "select * from wis_sysSet where id = '99'"
        alldata = self.db.querySQL(qs)
        current = alldata.record(0)

        zjptYN = current.field('zjptYN').value()
        htzdclYN = current.field('htzdclYN').value()
        htzdclTime = current.field('htzdclTime').value()
        localServer = current.field('localServer').value()
        backupUrl = current.field('backupUrl').value()
        photoBdYN = current.field('photoBdYN').value()
        aqmYN = current.field('aqmYN').value()
        cjSN = current.field('cjSN').value()
        cjKEY = current.field('cjKEY').value()
        if zjptYN == 1:
            self.checkBox_zjptYN.setChecked(True)
            item = current.field('zjptName').value()
            items = []
            items.append(item)
            self.comboBox_zjptName.addItems(items)
            self.comboBox_zjptName.setCurrentIndex(0)
        else:
            self.checkBox_zjptYN.setChecked(False)
            self.comboBox_zjptName.clear()
            self.comboBox_zjptName.setEnabled(False)

        if htzdclYN == 1:
            self.checkBox_htzdclYN.setChecked(True)
            self.spinBox_htzkclTime.setValue(htzdclTime)
        else:
            self.checkBox_htzdclYN.setChecked(False)
            self.spinBox_htzkclTime.setEnabled(False)

        if aqmYN == 1:
            self.checkBox_aqmYN.setChecked(True)
        else:
            self.checkBox_aqmYN.setChecked(False)

        if photoBdYN == 1:
            self.checkBox_photoBdYN.setChecked(True)
        else:
            self.checkBox_photoBdYN.setChecked(False)

        self.le_backupUrl.setText(backupUrl)
        self.le_localServer.setText(localServer)
        self.le_cjSN.setText(cjSN)
        self.le_cjKEY.setText(cjKEY)

    @pyqtSlot()
    def on_pb_update_clicked(self):
        self.enableAll()

    @pyqtSlot()
    def on_pb_save_clicked(self):
        zjptYN = 1 if self.checkBox_zjptYN.isChecked() else 0
        zjptName = self.comboBox_zjptName.currentText()
        htzdclYN = 1 if self.checkBox_htzdclYN.isChecked() else 0
        htzdclTime = int(self.spinBox_htzkclTime.value())
        localServer = self.le_localServer.text()
        backupUrl = self.le_backupUrl.text()
        photoBdYN = 1 if self.checkBox_photoBdYN.isChecked() else 0
        aqmYN = 1 if self.checkBox_aqmYN.isChecked() else 0
        cjSN = self.le_cjSN.text()
        cjKEY = self.le_cjKEY.text()

        qs = "update wis_sysSet set zjptYN = %d, zjptName = '%s', htzdclYN = %d, htzdclTime = %d, localServer = '%s', backupUrl = '%s', photoBdYN = %d, aqmYN = %d, cjSN = '%s', cjKEY = '%s' " %(zjptYN, zjptName, htzdclYN, htzdclTime, localServer, backupUrl, photoBdYN, aqmYN, cjSN, cjKEY)
        self.db.excuteSQl(qs)
        self.disableAll()

    @pyqtSlot()
    def on_pb_selectPath_clicked(self):
        path = QFileDialog.getExistingDirectory(self, '选择用于备份数据的目录', '/')

        self.le_backupUrl.setText(path)







