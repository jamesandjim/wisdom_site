import datetime
import base64

from PyQt5.QtWidgets import QWidget, QMessageBox, QProgressDialog, QProgressBar, QStyledItemDelegate
from PyQt5.QtCore import pyqtSlot, QModelIndex, Qt, QTime, QDate, QDateTime
from PyQt5.Qt import QPixmap, QImage
from PyQt5.QtGui import QIcon

from commTools.toBASE64 import jpgtostr, strtojpg
from models.dbtools import Dboperator
import cdzjpt

from views import attendanceManagementUi


class AttendanceManagementWindow(QWidget, attendanceManagementUi.Ui_Form):
    def __init__(self, parent=None):
        super(AttendanceManagementWindow, self).__init__(parent)
        self.setupUi(self)
        self.db = Dboperator()
        self.cdzj = cdzjpt.Cdzj()
        self.records = None
        self.load()

    def load(self):

        self.dateTimeEdit_begin.setDate(QDate.currentDate())
        self.dateTimeEdit_begin.setTime(QTime(0,0,0))
        self.dateTimeEdit_end.setDateTime(QDateTime.currentDateTime())

    @pyqtSlot()
    def on_pb_allData_clicked(self):
        qs = '''SELECT
                wis_person.user_id,wis_records.faceId,wis_person.name,case wis_person.userType when 1 then '劳务人员' else '岗位人员' end
                ,wis_person.department, wis_records.datetime, 
                wis_faceDevice.name, wis_records.ip, wis_faceDevice.location, wis_faceDevice.deviceType, 
                case wis_records.uploadYN when 1 then '已上传平台' else '未上传平台' end, wis_records.image
                from wis_records, wis_person, wis_faceDevice
                where wis_records.faceId = wis_person.idNo and wis_records.ip = wis_faceDevice.ip
        '''
        allRecords = self.db.querySQL(qs)
        self.records = allRecords
        count = allRecords.rowCount()
        print(count)
        self.tv_attendance.setModel(allRecords)

        allRecords.setHeaderData(0, Qt.Horizontal, '住建平台号')
        allRecords.setHeaderData(1, Qt.Horizontal, '身份证号')
        allRecords.setHeaderData(2, Qt.Horizontal, '人员名称')
        allRecords.setHeaderData(3, Qt.Horizontal, '人员类型')
        allRecords.setHeaderData(4, Qt.Horizontal, '人员所属班组')
        allRecords.setHeaderData(5, Qt.Horizontal, '出入时间')
        allRecords.setHeaderData(6, Qt.Horizontal, '出入设备名称')
        allRecords.setHeaderData(7, Qt.Horizontal, '出入设备IP')
        allRecords.setHeaderData(8, Qt.Horizontal, '出入设备位置')
        allRecords.setHeaderData(9, Qt.Horizontal, '出入设备类型')
        allRecords.setHeaderData(10, Qt.Horizontal, '上传平台状态')
        allRecords.setHeaderData(11, Qt.Horizontal, '进出图片')

        self.tv_attendance.resizeColumnsToContents()
        self.tv_attendance.horizontalHeader().setStretchLastSection(True)
        self.tv_attendance.setColumnWidth(0, 200)
        self.tv_attendance.setColumnWidth(1, 200)
        self.tv_attendance.setColumnWidth(11, 80)
        delegate = MyDelegate()
        self.tv_attendance.setItemDelegateForColumn(11, delegate)

    @pyqtSlot()
    def on_pb_uploadAtt_clicked(self):
        qs = '''
             select wis_faceDevice.
             '''

    @pyqtSlot(QModelIndex)
    def on_tv_attendance_clicked(self):
        rowID = self.tv_attendance.currentIndex().row()
        image = self.records.index(rowID, 11).data()
        bimage = base64.b64decode(image)
        fileimage = QImage.fromData(bimage)
        piximage = QPixmap.fromImage(fileimage)
        self.label_image.setPixmap(piximage)
        self.label_image.setScaledContents(True)


class MyDelegate(QStyledItemDelegate):
    def __init__(self, parent=None):
        super(MyDelegate, self).__init__(parent)
        self._icons = QIcon(':/ico/resource/ico/ex.jpg')

    def get_icon(self):
        # get the icon according to the condition:
        # In this case, for example,
        # the icon will be repeated periodically
        icon = QIcon(':/ico/resource/ico/ex.jpg')
        return icon

    def paint(self, painter, option, index):
        icon = self.get_icon()
        icon.paint(painter, option.rect, Qt.AlignCenter)




