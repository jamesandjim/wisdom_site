from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5.QtCore import pyqtSlot, QModelIndex, Qt

from models.dbtools import Dboperator

from views import faceDeviceUi


class FaceDeviceWindow(QWidget, faceDeviceUi.Ui_Form):
    def __init__(self, parent=None):
        super(FaceDeviceWindow, self).__init__(parent)
        self.setupUi(self)
        self.db = Dboperator()
        self.data = None
        self.load()
        self.disableTxt()
        self.operator = ''

    def load(self):
        '''初始化界面中的表格数据'''
        qs = '''
             select id, name, deviceType, location, case status when 1 then '正常使用' else '停止使用' end,
             ip, netmask, gateway, sn, key, memo
             from wis_faceDevice
             '''
        self.data = self.db.querySQL(qs)
        self.tv_device.setModel(self.data)

        self.data.setHeaderData(0, Qt.Horizontal, '设备编号')
        self.data.setHeaderData(1, Qt.Horizontal, '设备名称')
        self.data.setHeaderData(2, Qt.Horizontal, '设备类型')
        self.data.setHeaderData(3, Qt.Horizontal, '安装位置')
        self.data.setHeaderData(4, Qt.Horizontal, '是否启用')
        self.data.setHeaderData(5, Qt.Horizontal, '设备IP')
        self.data.setHeaderData(6, Qt.Horizontal, '子网掩码')
        self.data.setHeaderData(7, Qt.Horizontal, '设备网关')
        self.data.setHeaderData(8, Qt.Horizontal, '设备SN')
        self.data.setHeaderData(9, Qt.Horizontal, '设备KEY')
        self.data.setHeaderData(10, Qt.Horizontal, '说明')
        self.tv_device.resizeColumnsToContents()


    def enableTxt(self):
        '''使界面文本框可编辑'''
        self.le_deviceId.setEnabled(True)
        self.le_deviceName.setEnabled(True)
        self.cb_deviceType.setEnabled(True)
        self.cb_location.setEnabled(True)
        self.radioButton_nomal.setEnabled(True)
        self.radioButton_stop.setEnabled(True)
        self.le_deviceIP.setEnabled(True)
        self.le_deivceMask.setEnabled(True)
        self.le_deviceGateWay.setEnabled(True)
        self.le_deviceSN.setEnabled(True)
        self.le_key.setEnabled(True)
        self.le_Memo.setEnabled(True)

        self.pb_update.setEnabled(False)
        self.pb_del.setEnabled(False)
        self.pb_save.setEnabled(True)
        self.pb_esc.setEnabled(True)

    def disableTxt(self):
        '''使界面文本框不可编辑'''
        self.le_deviceId.setEnabled(False)
        self.le_deviceName.setEnabled(False)
        self.cb_deviceType.setEnabled(False)
        self.cb_location.setEnabled(False)
        self.radioButton_nomal.setEnabled(False)
        self.radioButton_stop.setEnabled(False)
        self.le_deviceIP.setEnabled(False)
        self.le_deivceMask.setEnabled(False)
        self.le_deviceGateWay.setEnabled(False)
        self.le_deviceSN.setEnabled(False)
        self.le_key.setEnabled(False)
        self.le_Memo.setEnabled(False)

        self.pb_del.setEnabled(False)
        self.pb_update.setEnabled(False)
        self.pb_save.setEnabled(False)
        self.pb_esc.setEnabled(False)

    def clearTxt(self):
        '''清除界面文本框中的内容'''
        self.le_deviceId.clear()
        self.le_deviceName.clear()
        # self.cb_deviceType.clear()
        # self.cb_location.clear()
        self.radioButton_nomal.setChecked(True)
        self.radioButton_stop.setChecked(False)
        self.le_deviceIP.clear()
        self.le_deivceMask.clear()
        self.le_deviceGateWay.clear()
        self.le_deviceSN.clear()
        self.le_key.clear()
        self.le_Memo.clear()

    @pyqtSlot()
    def on_pb_add_clicked(self):
        '''增加按钮的处理方法'''
        self.enableTxt()
        self.clearTxt()
        self.pb_add.setEnabled(False)
        self.operator = 'add'

    @pyqtSlot()
    def on_pb_update_clicked(self):
        '''修改按钮的处理方法'''
        self.enableTxt()
        self.pb_add.setEnabled(False)
        self.operator = 'update'

    @pyqtSlot()
    def on_pb_del_clicked(self):
        '''删除按钮的处理方法'''
        qs = "delete  from wis_faceDevice where id = '%s'" % self.le_deviceId
        if QMessageBox.information(self, '提示', '你确认要删除选中设备？', QMessageBox.Yes | QMessageBox.No,
                                   QMessageBox.Yes) == QMessageBox.Yes:
            self.db.excuteSQl(qs)
            self.txtClear()
            self.load()

    @pyqtSlot()
    def on_pb_save_clicked(self):
        '''保存按钮的处理方法'''
        deviceId = self.le_deviceId.text()
        name = self.le_deviceName.text()
        deviceType = self.cb_deviceType.currentText()
        location = self.cb_location.currentText()
        status = 1 if self.radioButton_nomal.isChecked() else 0
        ip = self.le_deviceIP.text()
        netmask = self.le_deivceMask.text()
        gateway = self.le_deviceGateWay.text()
        sn = self.le_deviceSN.text()
        key = self.le_key.text()
        memo = self.le_Memo.text()

        if self.operator == 'add':
            qs = '''
            insert into wis_faceDevice values ('%s', '%s', '%s', '%s', %d, '%s','%s','%s','%s','%s','%s')
            ''' % (deviceId, name, deviceType, location, status, ip, netmask, gateway, sn, key, memo)
        else:
            qs = '''
            update wis_faceDevice set name = '%s', deviceType = '%s', location = '%s', status = %d, ip = '%s',
            netmask = '%s', gateway = '%s', sn = '%s', key = '%s', memo = '%s'
            where id = '%s'
            ''' % (name, deviceType, location, status, ip, netmask, gateway, sn, key, memo, deviceId)

        self.db.excuteSQl(qs)
        self.load()

        self.disableTxt()
        self.clearTxt()
        self.pb_add.setEnabled(True)

    @pyqtSlot()
    def on_pb_esc_clicked(self):
        '''取消按钮的处理方法'''
        self.disableTxt()
        self.clearTxt()
        self.pb_add.setEnabled(True)

    @pyqtSlot()
    def on_pb_query_clicked(self):
        '''查询按钮的处理方法'''
        queryPara = self.le_queryPara.text()
        if queryPara == '':
            QMessageBox.information(self, '提示', '请输入查询条件！', QMessageBox.Yes)
        else:
            qs = '''select id, name, deviceType, location, case status when 1 then '正常使用' else '停止使用' end,
             ip, netmask, gateway, sn, key, memo
             from wis_faceDevice where name = '%s' or ip = '%s'
            ''' % (queryPara, queryPara)

            self.data = self.db.querySQL(qs)

            self.tv_device.setModel(self.data)
            self.data.setHeaderData(0, Qt.Horizontal, '设备编号')
            self.data.setHeaderData(1, Qt.Horizontal, '设备名称')
            self.data.setHeaderData(2, Qt.Horizontal, '设备类型')
            self.data.setHeaderData(3, Qt.Horizontal, '安装位置')
            self.data.setHeaderData(4, Qt.Horizontal, '是否启用')
            self.data.setHeaderData(5, Qt.Horizontal, '设备IP')
            self.data.setHeaderData(6, Qt.Horizontal, '子网掩码')
            self.data.setHeaderData(7, Qt.Horizontal, '设备网关')
            self.data.setHeaderData(8, Qt.Horizontal, '设备SN')
            self.data.setHeaderData(9, Qt.Horizontal, '设备KEY')
            self.data.setHeaderData(10, Qt.Horizontal, '说明')
            self.tv_device.resizeColumnsToContents()

    @pyqtSlot()
    def on_pb_allData_clicked(self):
        '''全部数据按钮的处理方法'''
        self.le_queryPara.clear()
        self.load()

    @pyqtSlot(QModelIndex)
    def on_tv_device_clicked(self):
        '''选择表中行数据的处理方法'''
        rowID = self.tv_device.currentIndex().row()

        deviceId = self.data.index(rowID, 0).data()
        deviceName = self.data.index(rowID, 1).data()
        deviceType = self.data.index(rowID, 2).data()
        location = self.data.index(rowID, 3).data()
        status = self.data.index(rowID, 4).data()
        deviceIP = self.data.index(rowID, 5).data()
        netmask = self.data.index(rowID, 6).data()
        gateway = self.data.index(rowID, 7).data()
        deviceSN = self.data.index(rowID, 8).data()
        deviceKey = self.data.index(rowID, 9).data()
        memo = self.data.index(rowID, 10).data()

        self.le_deviceId.setText(deviceId)
        self.le_deviceName.setText(deviceName)
        self.cb_deviceType.setCurrentText(deviceType)
        self.cb_location.setCurrentText(location)
        self.le_deviceIP.setText(deviceIP)
        self.le_deivceMask.setText(netmask)
        self.le_deviceGateWay.setText(gateway)
        self.le_deviceSN.setText(deviceSN)
        self.le_key.setText(deviceKey)
        self.le_Memo.setText(memo)
        if status == '正常使用':
            self.radioButton_nomal.setChecked(True)
        else:
            self.radioButton_stop.setChecked(True)


        self.pb_update.setEnabled(True)
        self.pb_del.setEnabled(True)