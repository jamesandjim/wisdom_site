from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5.QtCore import pyqtSlot, QModelIndex, Qt
from PyQt5.Qt import QPixmap

from models.dbtools import Dboperator
from views import personManagementUi


class PersonManageWindow(QWidget, personManagementUi.Ui_Form):
    def __init__(self, parent=None):
        super(PersonManageWindow, self).__init__(parent)
        self.setupUi(self)
        self.data = None
        self.disableEdit()
        self.db = Dboperator()
        self.load()

    def load(self):
        qs = '''
        select idNo, name, case gender when 1 then '男' when 0 then '女' end, nation, birthday, address, idissue, idperiod,
        idphoto, photo, case userType when 1 then '劳务人员' when 2 then '岗位人员' end,
        case RegType when 3 then '人脸采集' else '其他' end, user_id, work_sn, department,
        case deviceStatus when 0 then '未同步到设备' when 1 then '已同步到设备' end, 
        case zjptStatus when 0 then '未同步到住建平台' when 1 then '已同步到住建平台' end, 
        case uploadYN when 0 then '不上传平台' when 1 then '应上传平台' end,
        case personStatus when 0 then '已停用' when 1 then '正常' end
        from wis_person
        '''
        allPerson = self.db.querySQL(qs)
        self.data = allPerson
        self.tv_person.setModel(self.data)
        allPerson.setHeaderData(0, Qt.Horizontal, '身份证号码')
        allPerson.setHeaderData(1, Qt.Horizontal, '姓名')
        allPerson.setHeaderData(2, Qt.Horizontal, '性别')
        allPerson.setHeaderData(3, Qt.Horizontal, '民族')
        allPerson.setHeaderData(4, Qt.Horizontal, '出生日期')
        allPerson.setHeaderData(5, Qt.Horizontal, '住址')
        allPerson.setHeaderData(6, Qt.Horizontal, '发证机关')
        allPerson.setHeaderData(7, Qt.Horizontal, '有效期')
        allPerson.setHeaderData(8, Qt.Horizontal, '身份证照片地址')
        allPerson.setHeaderData(9, Qt.Horizontal, '人脸照片地址')
        allPerson.setHeaderData(10, Qt.Horizontal, '用户类型')
        allPerson.setHeaderData(11, Qt.Horizontal, '注册类型')
        allPerson.setHeaderData(12, Qt.Horizontal, '住建平台统一号')
        allPerson.setHeaderData(13, Qt.Horizontal, '住建平台工作号')
        allPerson.setHeaderData(14, Qt.Horizontal, '部门班组')
        allPerson.setHeaderData(15, Qt.Horizontal, '设备同步状态')
        allPerson.setHeaderData(16, Qt.Horizontal, '平台同步状态')
        allPerson.setHeaderData(17, Qt.Horizontal, '是否上传平台')
        allPerson.setHeaderData(18, Qt.Horizontal, '人员状态')

        self.tv_person.resizeColumnsToContents()

    def enableEdit(self):
        self.comboBox_department.setEnabled(True)
        self.comboBox_userType.setEnabled(True)
        self.comboBox_RegType.setEnabled(True)
        self.checkBox_uploadYN.setEnabled(True)
        self.radioButton_personStatus_stop.setEnabled(True)
        self.radioButton_personStatus_nomal.setEnabled(True)

        self.pb_save.setEnabled(True)
        self.pb_esc.setEnabled(True)
        self.pb_del.setEnabled(False)

    def disableEdit(self):
        self.comboBox_department.setEnabled(False)
        self.comboBox_userType.setEnabled(False)
        self.comboBox_RegType.setEnabled(False)
        self.checkBox_uploadYN.setEnabled(False)
        self.radioButton_personStatus_stop.setEnabled(False)
        self.radioButton_personStatus_nomal.setEnabled(False)
        self.pb_save.setEnabled(False)
        self.pb_esc.setEnabled(False)
        self.pb_del.setEnabled(False)
        self.pb_update.setEnabled(False)
        self.pb_replaceIMG.setEnabled(False)

    def txtClear(self):
        self.le_idNo.clear()
        self.le_name.clear()
        self.le_gender.clear()
        self.le_nation.clear()
        self.le_address.clear()
        self.le_birthday.clear()
        self.le_idperiod.clear()
        self.le_idissue.clear()
        self.comboBox_department.clear()
        self.comboBox_RegType.clear()
        self.comboBox_userType.clear()
        self.le_user_id.clear()
        self.checkBox_uploadYN.setChecked(False)
        self.le_work_sn.clear()
        self.le_deviceStatus.clear()
        self.le_zjptStatus.clear()


    @pyqtSlot()
    def on_pb_replaceIMG_clicked(self):
        pass

    @pyqtSlot()
    def on_pb_del_clicked(self):
        qs = "delete  from wis_person where idNo = '%s'" % self.le_idNo.text()
        if QMessageBox.information(self, '提示', '你确认要删除选中人员？', QMessageBox.Yes|QMessageBox.No, QMessageBox.Yes) == QMessageBox.Yes:
            self.db.excuteSQl(qs)
            self.txtClear()
            self.load()

    @pyqtSlot()
    def on_pb_update_clicked(self):
        self.enableEdit()

    @pyqtSlot()
    def on_pb_save_clicked(self):
        department = self.comboBox_department.currentText()
        idNo = self.le_idNo.text()
        userType = 1 if self.comboBox_userType.currentText() == '劳务人员' else 2
        RegType = 3 if self.comboBox_RegType.currentText() == '人脸采集' else 0
        uploadYN = 1 if self.checkBox_uploadYN.isChecked() else 0
        personStatus = 1 if self.radioButton_personStatus_nomal.isChecked() else 0
        qs = '''
             update wis_person set department = '%s', userType = %d, RegType = %d, uploadYN = %d, personStatus = %d
             where idNo = '%s'
             ''' % (department, userType, RegType, uploadYN, personStatus, idNo)
        self.db.excuteSQl(qs)
        self.disableEdit()
        self.load()

    @pyqtSlot()
    def on_pb_esc_clicked(self):
        self.disableEdit()

    @pyqtSlot()
    def on_comboBox_department_activated(self):
        qs1 = 'select name from wis_department'
        allDepartment = self.db.querySQL(qs1)
        self.comboBox_department.clear()
        self.comboBox_department.setModel(allDepartment)


    @pyqtSlot(QModelIndex)
    def on_tv_person_clicked(self, QModelIndex):
        rowID = self.tv_person.currentIndex().row()

        idNo = self.data.index(rowID, 0).data()
        name = self.data.index(rowID, 1).data()
        gender = self.data.index(rowID, 2).data()
        nation = self.data.index(rowID, 3).data()
        birthday = self.data.index(rowID, 4).data()
        address = self.data.index(rowID, 5).data()
        idissue = self.data.index(rowID, 6).data()
        idperiod = self.data.index(rowID, 7).data()
        idphoto = self.data.index(rowID, 8).data()
        photo = self.data.index(rowID, 9).data()
        userType = self.data.index(rowID, 10).data()
        RegType = self.data.index(rowID, 11).data()
        user_id = self.data.index(rowID, 12).data()
        work_sn = self.data.index(rowID, 13).data()
        department = self.data.index(rowID, 14).data()
        deviceStatus = self.data.index(rowID, 15).data()
        zjptStatus = self.data.index(rowID, 16).data()
        uploadYN = self.data.index(rowID, 17).data()
        personStatus = self.data.index(rowID, 18).data()

        self.le_idNo.setText(idNo)
        self.le_name.setText(name)
        self.le_gender.setText(gender)
        self.le_nation.setText(nation)
        self.le_address.setText(address)
        self.le_birthday.setText(birthday)
        self.le_idperiod.setText(idperiod)
        self.le_idissue.setText(idissue)
        self.le_user_id.setText(user_id)
        self.le_work_sn.setText(work_sn)
        self.le_deviceStatus.setText(deviceStatus)
        self.le_zjptStatus.setText(zjptStatus)

        qs1 = 'select name from wis_department'
        allDepartment = self.db.querySQL(qs1)
        self.comboBox_department.clear()
        self.comboBox_department.setModel(allDepartment)
        self.comboBox_department.setCurrentText(department)

        list_userType = ['劳务人员', '岗位人员', '其他人员']
        self.comboBox_userType.clear()
        self.comboBox_userType.addItems(list_userType)
        self.comboBox_userType.setCurrentText(userType)

        list_RegType = ['人脸采集', '刷卡采集', '指纹采集', '其他采集']
        self.comboBox_RegType.clear()
        self.comboBox_RegType.addItems(list_RegType)
        self.comboBox_RegType.setCurrentText(RegType)


        if uploadYN == '应上传平台':
            self.checkBox_uploadYN.setChecked(True)
        else:
            self.checkBox_uploadYN.setChecked(False)

        if personStatus == '正常':
            self.radioButton_personStatus_nomal.setChecked(True)
        else:
            self.radioButton_personStatus_stop.setChecked(False)
        idphoto_pixmap = QPixmap(idphoto)
        self.label_idphoto.setPixmap(idphoto_pixmap)
        self.label_idphoto.setScaledContents(True)
        photo_pixmap = QPixmap(photo)
        self.label_photo.setPixmap(photo_pixmap)
        self.label_photo.setScaledContents(True)

        self.pb_update.setEnabled(True)
        self.pb_replaceIMG.setEnabled(True)
        self.pb_del.setEnabled(True)


