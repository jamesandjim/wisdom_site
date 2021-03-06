import sys
import os

from PyQt5.QtWidgets import QApplication, QWidget, QDialog, QMessageBox
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtGui import QCursor, QMouseEvent

from views import mainUi
import infoCollectionController
import sysSetController
import departmentController
import faceDeviceController
import readerDeviceController
import zjptController
import personManageController
import attendanceManagementController
import loginController
import operatorController


class MyMainWindow(QWidget, mainUi.Ui_mainForm):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        # self.setWindowFlags(Qt.FramelessWindowHint)
        self.tree_menu.expandAll()
        # self.tree_menu.itemClicked['QTreeWidgetItem*', 'int'].connect(self.tree_menu_itemClicked)


    def removeC(self):
        for i in range(self.verticalLayout_3.count()):
            self.verticalLayout_3.itemAt(i).widget().deleteLater()

    @pyqtSlot('QTreeWidgetItem*', 'int')
    def on_tree_menu_itemClicked(self):
        selected = self.tree_menu.currentItem().text(0)

        if selected == '劳务人员信息采集':
            widget = infoCollectionController.InfoCollectionCls()
            self.removeC()
            self.verticalLayout_3.addWidget(widget)

        elif selected == '系统参数设置':
            widget = sysSetController.SysSetWindow()
            self.removeC()
            self.verticalLayout_3.addWidget(widget)

        elif selected == '住建平台信息设置':
            widget = zjptController.ZjptDeviceWindow()
            self.removeC()
            self.verticalLayout_3.addWidget(widget)

        elif selected == '劳务人员信息管理':
            widget = personManageController.PersonManageWindow()
            self.removeC()
            self.verticalLayout_3.addWidget(widget)

        elif selected == '人员考勤数据管理':
            widget = attendanceManagementController.AttendanceManagementWindow()
            self.removeC()
            self.verticalLayout_3.addWidget(widget)

        # elif selected == '采集设备':
        #     widget = readerDeviceController.ReaderDeviceWindow()
        #     self.removeC()
        #     self.verticalLayout_3.addWidget(widget)

        elif selected == '考勤设备':
            widget = faceDeviceController.FaceDeviceWindow()
            self.removeC()
            self.verticalLayout_3.addWidget(widget)

        elif selected == '显示屏设备':
            pass

        elif selected == '显示屏内容设置':
            pass

        elif selected == 'LCD显示':
            pass

        elif selected == '数据备份':
            pass

        elif selected == '系统人员管理':
            widget = operatorController.OperatorWindow()
            self.removeC()
            self.verticalLayout_3.addWidget(widget)

        elif selected == '班组信息管理':
            widget = departmentController.DepartmentWindow()
            self.removeC()
            self.verticalLayout_3.addWidget(widget)

        else:
            pass

    @pyqtSlot()
    def on_pb_addPerson_clicked(self):
        widget = infoCollectionController.InfoCollectionCls()
        self.removeC()
        self.verticalLayout_3.addWidget(widget)

    @pyqtSlot()
    def on_pb_zjpt_clicked(self):
        widget = personManageController.PersonManageWindow()
        self.removeC()
        self.verticalLayout_3.addWidget(widget)

    @pyqtSlot()
    def on_pb_lcdMonitor_clicked(self):
        monitor = 'lcdMonitorController.exe'
        try:
            r = os.popen(monitor)
        except Exception as e:
            QMessageBox.information(self, '提示', '打开软件出错，请确认文件是否存在！', QMessageBox.Yes)

    @pyqtSlot()
    def on_pb_tools_clicked(self):
        tools = './tools/VzFaceSDKDemo.exe'
        try:
            r = os.popen(tools)
        except Exception as e:
            QMessageBox.information(self, '提示', '打开软件出错，请确认文件是否存在！', QMessageBox.Yes)

    @pyqtSlot()
    def on_pb_exitSystem_clicked(self):
        sys.exit()

    # def mousePressEvent(self, QMouseEvent):
    #
    #     if QMouseEvent.button() == Qt.LeftButton:
    #         self.flag = True
    #
    #         self.m_Position = QMouseEvent.globalPos() - self.pos()
    #
    #         QMouseEvent.accept()
    #
    #         self.setCursor(QCursor(Qt.OpenHandCursor))
    #
    # def mouseMoveEvent(self, QMouseEvent):
    #
    #     if Qt.LeftButton and self.flag:
    #         self.move(QMouseEvent.globalPos() - self.m_Position)
    #
    #         QMouseEvent.accept()
    #
    # def mouseReleaseEvent(self, QMouseEvent):
    #
    #     self.flag = False
    #
    #     self.setCursor(QCursor(Qt.ArrowCursor))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = loginController.LoginWindow()
    if dialog.exec_() == QDialog.Accepted:
        form = MyMainWindow()
        form.showMaximized()
        sys.exit(app.exec_())

