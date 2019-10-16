import datetime

from PyQt5.QtWidgets import QWidget, QMessageBox, QProgressDialog, QProgressBar
from PyQt5.QtCore import pyqtSlot, QModelIndex, Qt
from PyQt5.Qt import QPixmap

from commTools.toBASE64 import jpgtostr
from models.dbtools import Dboperator

from views import attendanceManagementUi


class AttendanceManagementWindow(QWidget, attendanceManagementUi.Ui_Form):
    def __init__(self, parent=None):
        super(AttendanceManagementWindow, self).__init__(parent)
        self.setupUi(self)
        self.db = Dboperator()

    @pyqtSlot()
    def on_pb_allData_clicked(self):
        qs = '''
             select faceID, datetime, gender from wis_records
             '''
        allRecords = self.db.querySQL(qs)
        self.tv_attendance.setModel(allRecords)