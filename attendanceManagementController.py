import time
import datetime
import base64

from PyQt5.QtWidgets import QWidget, QMessageBox, QProgressDialog, QProgressBar, QStyledItemDelegate
from PyQt5.QtCore import pyqtSlot, QModelIndex, Qt, QTime, QDate, QDateTime
from PyQt5.Qt import QPixmap, QImage
from PyQt5.QtGui import QIcon
from PyQt5.QtSql import QSqlQueryModel

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

        # 以下参数为分页使用
        self.totalPage = 0
        self.currentPage = 0
        self.totalRecord = 0
        self.pageRecord = 20

        self.setQueryTime()

        self.queryModel = None
        self.getAllRecords()
        self.recordQuery(self.currentPage)
        self.load()

    def setQueryTime(self):
        self.dateTimeEdit_begin.setDate(QDate.currentDate())
        self.dateTimeEdit_begin.setTime(QTime(0, 0, 0))
        self.dateTimeEdit_end.setDateTime(QDateTime.currentDateTime())

    def getAllRecords(self):
        qs = '''SELECT
                        wis_person.user_id,wis_recordsx.per_id,wis_person.name,case wis_person.userType when 1 then '劳务人员' else '岗位人员' end
                        ,wis_person.department, wis_recordsx.usec, 
                        wis_faceDevice.name, wis_recordsx.sn, wis_faceDevice.location, wis_faceDevice.deviceType, 
                        case wis_recordsx.uploadYN when 1 then '已上传平台' else '未上传平台' end, wis_recordsx.face_imgdata
                        from wis_recordsx, wis_person, wis_faceDevice
                        where wis_recordsx.per_id = wis_person.idNo and wis_recordsx.sn = wis_faceDevice.deviceSn
                '''
        self.queryModel = self.db.querySQL(qs)

        # 总记录数
        self.totalRecord = self.queryModel.rowCount()

        # 总页数
        self.totalPage = int((self.totalRecord + self.pageRecord - 1) / self.pageRecord)
        self.label_totalPage.setText("/" + str(int(self.totalPage)) + "页")
        self.lineEdit_currentPage.setText(str(int(self.currentPage)+1))

    def recordQuery(self, index):
        queryPara_name = self.le_queryPara.text().strip()
        time_begin = self.dateTimeEdit_begin.dateTime().toSecsSinceEpoch()
        time_end = self.dateTimeEdit_end.dateTime().toSecsSinceEpoch()

        if queryPara_name == '':
            qs_count = "select * from wis_recordsx where timesta between %d and %d" % (time_begin, time_end)


            qs = '''SELECT
                        wis_person.user_id,wis_recordsx.per_id,wis_person.name,case wis_person.userType when 1 then '劳务人员' else '岗位人员' end
                        ,wis_person.department, wis_recordsx.usec, 
                        wis_faceDevice.name, wis_recordsx.sn, wis_faceDevice.location, wis_faceDevice.deviceType, 
                        case wis_recordsx.uploadYN when 1 then '已上传平台' else '未上传平台' end, wis_recordsx.face_imgdata
                        from wis_recordsx, wis_person, wis_faceDevice
                        where wis_recordsx.per_id = wis_person.idNo and wis_recordsx.sn = wis_faceDevice.deviceSn
                        and timesta between %d and %d 
                        limit %d, 20
                ''' % (time_begin, time_end, int(index))
        else:
            qs_count = "select * from wis_recordsx where timesta between %d and %d and name = '%s'" % (time_begin, time_end, queryPara_name)

            qs = '''SELECT
                         wis_person.user_id,wis_recordsx.per_id,wis_person.name,case wis_person.userType when 1 then '劳务人员' else '岗位人员' end
                         ,wis_person.department, wis_recordsx.usec, 
                          wis_faceDevice.name, wis_recordsx.sn, wis_faceDevice.location, wis_faceDevice.deviceType, 
                          case wis_recordsx.uploadYN when 1 then '已上传平台' else '未上传平台' end, wis_recordsx.face_imgdata
                          from wis_recordsx, wis_person, wis_faceDevice
                          where wis_recordsx.per_id = wis_person.idNo and wis_recordsx.sn = wis_faceDevice.deviceSn and wis_person.name = '%s'
                          and timesta between %d and %d 
                          limit %d, 20
                            ''' % (queryPara_name, time_begin, time_end, int(index))
        self.queryModel = self.db.querySQL(qs_count)
        # 总记录数
        self.totalRecord = self.queryModel.rowCount()
        # 总页数
        self.totalPage = int((self.totalRecord + self.pageRecord - 1) / self.pageRecord)
        self.label_totalPage.setText("/" + str(int(self.totalPage)) + "页")
        self.lineEdit_currentPage.setText(str(int(self.currentPage) + 1))
        self.queryModel = self.db.querySQL(qs)
        self.tv_attendance.setModel(self.queryModel)

    def load(self):
        self.queryModel.setHeaderData(0, Qt.Horizontal, '住建平台号')
        self.queryModel.setHeaderData(1, Qt.Horizontal, '身份证号')
        self.queryModel.setHeaderData(2, Qt.Horizontal, '人员名称')
        self.queryModel.setHeaderData(3, Qt.Horizontal, '人员类型')
        self.queryModel.setHeaderData(4, Qt.Horizontal, '人员所属班组')
        self.queryModel.setHeaderData(5, Qt.Horizontal, '出入时间')
        self.queryModel.setHeaderData(6, Qt.Horizontal, '出入设备名称')
        self.queryModel.setHeaderData(7, Qt.Horizontal, '出入设备IP')
        self.queryModel.setHeaderData(8, Qt.Horizontal, '出入设备位置')
        self.queryModel.setHeaderData(9, Qt.Horizontal, '出入设备类型')
        self.queryModel.setHeaderData(10, Qt.Horizontal, '上传平台状态')
        self.queryModel.setHeaderData(11, Qt.Horizontal, '进出图片')

        self.tv_attendance.resizeColumnsToContents()
        self.tv_attendance.horizontalHeader().setStretchLastSection(True)
        self.tv_attendance.setColumnWidth(0, 150)
        self.tv_attendance.setColumnWidth(1, 150)
        self.tv_attendance.setColumnWidth(11, 80)
        delegate = MyDelegate()
        self.tv_attendance.setItemDelegateForColumn(11, delegate)

        self.setButtonStatus()

    def setButtonStatus(self):
        if self.currentPage == int(self.totalPage-1):
            self.pb_prev.setEnabled(True)
            self.pb_next.setEnabled(False)
        if self.currentPage == 0:
            self.pb_next.setEnabled(True)
            self.pb_prev.setEnabled(False)
        if self.currentPage < self.totalPage-1 and self.currentPage > 0:
            self.pb_prev.setEnabled(True)
            self.pb_next.setEnabled(True)
        if self.totalPage <= 1:
            self.pb_prev.setEnabled(False)
            self.pb_next.setEnabled(False)
            self.lineEdit_currentPage.setText('0')

    @pyqtSlot()
    def on_pb_query_clicked(self):
        self.recordQuery(self.currentPage)
        self.load()

    @pyqtSlot()
    def on_pb_allData_clicked(self):
        self.getAllRecords()
        self.recordQuery(self.currentPage)
        self.load()

    @pyqtSlot()
    def on_lineEdit_currentPage_editingFinished(self):
        if self.lineEdit_currentPage.text().isdigit():
            self.currentPage = int(self.lineEdit_currentPage.text())-1
            if self.currentPage >= self.totalPage-1:
                self.currentPage = self.totalPage-1
            if self.currentPage <= 0:
                self.currentPage = 0

    @pyqtSlot()
    def on_pb_jumpTo_clicked(self):
        index = self.currentPage * self.pageRecord
        self.lineEdit_currentPage.setText(str(self.currentPage+1))
        self.recordQuery(index)
        self.load()


    @pyqtSlot()
    def on_pb_prev_clicked(self):
        self.currentPage -= 1
        if self.currentPage <= 0:
            self.currentPage = 0
        self.lineEdit_currentPage.setText(str(self.currentPage+1))
        index = (self.currentPage) * self.pageRecord
        self.recordQuery(index)
        self.load()

    @pyqtSlot()
    def on_pb_next_clicked(self):
        self.currentPage += 1
        if self.currentPage >= int(self.totalPage)-1:
            self.currentPage = int(self.totalPage)-1
        self.lineEdit_currentPage.setText(str(self.currentPage+1))
        index = (self.currentPage) * self.pageRecord
        self.recordQuery(index)
        self.load()


    @pyqtSlot(QModelIndex)
    def on_tv_attendance_clicked(self):
        rowID = self.tv_attendance.currentIndex().row()
        image = self.queryModel.index(rowID, 11).data()
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




