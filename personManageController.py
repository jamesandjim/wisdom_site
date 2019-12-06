import datetime
import base64
import requests
import time

from PyQt5.QtWidgets import QWidget, QMessageBox, QProgressDialog, QProgressBar
from PyQt5.QtCore import pyqtSlot, QModelIndex, Qt
from PyQt5.Qt import QPixmap

from commTools.toBASE64 import jpgtostr
from models.dbtools import Dboperator
from views import personManagementUi
import cdzjpt
from devices.face01 import FaceDevice


class PersonManageWindow(QWidget, personManagementUi.Ui_Form):
    def __init__(self, parent=None):
        super(PersonManageWindow, self).__init__(parent)
        self.setupUi(self)
        self.pb_refresh.setVisible(False)
        self.data = None
        self.disableEdit()
        self.face = FaceDevice()
        self.db = Dboperator()
        self.cdzj = cdzjpt.Cdzj()
        self.cjSN = ''
        self.cjKEY = ''
        self.faceDevices = None
        self.load()

    def load(self):
        '''方法作用为初始化窗口数据'''
        qs = '''
        select idNo, name, case gender when 1 then '男' when 2 then '女' end, nation, birthday, address, idissue, idperiod,
        idphoto, photo, case userType when 1 then '劳务人员' when 2 then '岗位人员' end,
        case RegType when 3 then '人脸采集' else '其他' end, user_id, work_sn, department,
        case deviceStatus when 0 then '未同步到设备' when 1 then '已同步到设备' end, 
        case zjptStatus when 0 then '未同步到住建平台' when 1 then '已同步到住建平台' end, 
        case uploadYN when 0 then '不上传平台' when 1 then '应上传平台' end,
        case personStatus when 2 then '已停用' when 1 then '正常' end
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

        zjqs = "select * from wis_cdzjpt where id = '99'"
        current = self.db.querySQL(zjqs).record(0)
        self.cdzj.uploadPersonURL = current.field('uploadPersonURL').value()
        # print(self.cdzj.uploadPersonURL)
        self.cdzj.downloadPersonURL = current.field('downloadPersonURL').value()
        self.cdzj.downloadDelPersonURL = current.field('deletePersonURL').value()
        self.cdzj.uploadAttendanceURL = current.field('uploadAttURL').value()
        self.cdzj.feedbackURL = current.field('feedbackURL').value()

        sysSetQs = "select * from wis_sysSet where id = 99"
        currentSysSet = self.db.querySQL(sysSetQs).record(0)
        self.cjSN = currentSysSet.field('cjSN').value()
        self.cjKEY = currentSysSet.field('cjKEY').value()

        device_qs = "select sn, key from wis_faceDevice where status = 1"
        self.faceDevices = self.db.querySQL(device_qs)

    def enableEdit(self):
        '''方法作用为使界面文本框可以输入'''
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
        '''方法作用为使界面文本框无法输入'''
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
        '''方法作用为清除文本框中的内容'''
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
        self.label_photo.clear()
        self.label_idphoto.clear()

    @pyqtSlot()
    def on_pb_replaceIMG_clicked(self):
        '''方法作用为更换人员的人脸图片'''
        pass

    @pyqtSlot()
    def on_pb_del_clicked(self):
        '''方法作用删除人员'''
        qs = "delete  from wis_person where idNo = '%s'" % self.le_idNo.text()
        if QMessageBox.information(self, '提示', '你确认要删除选中人员？', QMessageBox.Yes|QMessageBox.No, QMessageBox.Yes) == QMessageBox.Yes:
            self.db.excuteSQl(qs)
            self.txtClear()
            self.load()

    @pyqtSlot()
    def on_pb_update_clicked(self):
        '''方法作用为对人员信息进行修改'''
        self.enableEdit()

    @pyqtSlot()
    def on_pb_save_clicked(self):
        '''方法作用为修改人员信息后，进行保存'''
        department = self.comboBox_department.currentText()
        idNo = self.le_idNo.text()
        userType = 1 if self.comboBox_userType.currentText() == '劳务人员' else 2
        RegType = 3 if self.comboBox_RegType.currentText() == '人脸采集' else 0
        uploadYN = 1 if self.checkBox_uploadYN.isChecked() else 0
        personStatus = 1 if self.radioButton_personStatus_nomal.isChecked() else 2
        qs = '''
             update wis_person set department = '%s', userType = %d, RegType = %d, uploadYN = %d, personStatus = %d
             where idNo = '%s'
             ''' % (department, userType, RegType, uploadYN, personStatus, idNo)
        self.db.excuteSQl(qs)
        self.disableEdit()
        self.load()

    @pyqtSlot()
    def on_pb_esc_clicked(self):
        '''方法作用为中止修改操作'''
        self.disableEdit()

    @pyqtSlot()
    def on_comboBox_department_activated(self):
        '''方法作用为点部门单选框时，载入相应部门信息'''
        qs1 = 'select name from wis_department'
        allDepartment = self.db.querySQL(qs1)
        self.comboBox_department.clear()
        self.comboBox_department.setModel(allDepartment)

    @pyqtSlot(QModelIndex)
    def on_tv_person_clicked(self, QModelIndex):
        '''方法作用为选中表中人员信息后，将人员信息在详情中进行填充'''
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
            self.radioButton_personStatus_stop.setChecked(True)

        idphoto_pixmap = QPixmap(idphoto)
        self.label_idphoto.setPixmap(idphoto_pixmap)
        self.label_idphoto.setScaledContents(True)
        photo_pixmap = QPixmap(photo)
        self.label_photo.setPixmap(photo_pixmap)
        self.label_photo.setScaledContents(True)

        self.pb_update.setEnabled(True)
        self.pb_replaceIMG.setEnabled(True)
        self.pb_del.setEnabled(True)

    @pyqtSlot()
    def on_pb_query_clicked(self):
        '''方法作用为根据输入条件，查询本地人员信息'''
        queryPara = self.le_queryPara.text()
        if queryPara == '':
            QMessageBox.information(self, '提示', '请输入查询条件！', QMessageBox.Yes)
        else:
            qs = '''
                    select idNo, name, case gender when 1 then '男' when 2 then '女' end, nation, birthday, address, idissue, idperiod,
                    idphoto, photo, case userType when 1 then '劳务人员' when 2 then '岗位人员' end,
                    case RegType when 3 then '人脸采集' else '其他' end, user_id, work_sn, department,
                    case deviceStatus when 0 then '未同步到设备' when 1 then '已同步到设备' end, 
                    case zjptStatus when 0 then '未同步到住建平台' when 1 then '已同步到住建平台' when 2 then '住建平台已删除' end, 
                    case uploadYN when 0 then '不上传平台' when 1 then '应上传平台' end,
                    case personStatus when 2 then '已停用' when 1 then '正常' end
                    from wis_person
                    where idNo = '%s' or name = '%s'
                    ''' % (queryPara, queryPara)
            somePerson = self.db.querySQL(qs)
            self.data = somePerson
            self.tv_person.setModel(self.data)

            somePerson.setHeaderData(0, Qt.Horizontal, '身份证号码')
            somePerson.setHeaderData(1, Qt.Horizontal, '姓名')
            somePerson.setHeaderData(2, Qt.Horizontal, '性别')
            somePerson.setHeaderData(3, Qt.Horizontal, '民族')
            somePerson.setHeaderData(4, Qt.Horizontal, '出生日期')
            somePerson.setHeaderData(5, Qt.Horizontal, '住址')
            somePerson.setHeaderData(6, Qt.Horizontal, '发证机关')
            somePerson.setHeaderData(7, Qt.Horizontal, '有效期')
            somePerson.setHeaderData(8, Qt.Horizontal, '身份证照片地址')
            somePerson.setHeaderData(9, Qt.Horizontal, '人脸照片地址')
            somePerson.setHeaderData(10, Qt.Horizontal, '用户类型')
            somePerson.setHeaderData(11, Qt.Horizontal, '注册类型')
            somePerson.setHeaderData(12, Qt.Horizontal, '住建平台统一号')
            somePerson.setHeaderData(13, Qt.Horizontal, '住建平台工作号')
            somePerson.setHeaderData(14, Qt.Horizontal, '部门班组')
            somePerson.setHeaderData(15, Qt.Horizontal, '设备同步状态')
            somePerson.setHeaderData(16, Qt.Horizontal, '平台同步状态')
            somePerson.setHeaderData(17, Qt.Horizontal, '是否上传平台')
            somePerson.setHeaderData(18, Qt.Horizontal, '人员状态')

            self.tv_person.resizeColumnsToContents()

    @pyqtSlot()
    def on_pb_allData_clicked(self):
        '''方法作用为查询全部人员信息'''
        self.load()

    @pyqtSlot()
    def on_pb_uploadToDevice_clicked(self):
        '''方法作用为上传人员信息到人脸识别设备-授权'''

        qs = "select * from wis_person"
        persons = self.db.querySQL(qs)
        countP = persons.rowCount()
        if countP > 0:
            i = 0
            while i < countP:
                dic = {}
                person = persons.record(i)
                dic['version'] = '0.2'
                dic['cmd'] = 'create_face'
                dic['per_id'] = person.field('idNo').value()
                dic['face_id'] = person.field('idNo').value()
                dic['per_name'] = person.field('name').value()
                # dic['idcardNum'] = person.field('idNo').value()
                dic['idcardper'] = person.field('idNo').value()
                dic['s_time'] = 0
                dic['e_time'] = 10000
                personStatus = person.field('personStatus').value()
                if personStatus == 1:
                    dic['per_type'] = 0
                else:
                    dic['per_type'] = 2

                dic['usr_type'] = 0

                desImg = './photos_face/{}_face.jpg'.format(dic['per_id'])

                with open(desImg, 'rb') as f:
                    bimg = base64.b64encode(f.read())
                dic['img_data'] = bimg

                requests.post('http://127.0.0.1:8080/addFace', data=dic)
                time.sleep(1)
                i += 1

        self.queryResult()
        QMessageBox.information(self, '提示', '增加人脸到设备完成,在数据中查看上传结果！', QMessageBox.Yes)

    @pyqtSlot()
    def on_pb_refresh_clicked(self):
        '''刷新本地数据'''
        qs = "select * from wis_person where personStatus = 1 and deviceStatus = 0"
        persons = self.db.querySQL(qs)
        countP = persons.rowCount()
        if countP > 0:
            i = 0
            while i < countP:
                dic = {}
                person = persons.record(i)
                dic['version'] = '0.2'
                dic['cmd'] = 'query_face'
                dic['per_id'] = person.field('idNo').value()

                dic['id'] = 20
                dic['name'] = ''

                requests.post('http://127.0.0.1:8080/queryFace', data=dic)
                time.sleep(1)
                i += 1
        self.load()


    @pyqtSlot()
    def on_pb_uploadPerson_clicked(self):
        '''方法作用为上传本地人员信息到成都住建平台'''

        qs = "select * from wis_person where zjptStatus = 0 and uploadYN = 1 and personStatus = 1"
        uploadPersons = self.db.querySQL(qs)
        countP = uploadPersons.rowCount()
        if countP > 0:
            i = 0
            while i < countP:
                person = uploadPersons.record(i)
                idNo = person.field('idNo').value()
                name = person.field('name').value()
                gender = person.field('gender').value()
                nation = person.field('nation').value()
                tbirthday = person.field('birthday').value()
                year = tbirthday[0:4]
                month = tbirthday[4:6]
                day = tbirthday[6:]
                birthday = year+'-'+month+'-'+day
                address = person.field('address').value()
                idissue = person.field('idissue').value()
                idperiod = person.field('idperiod').value()
                idphotoPath = person.field('idphoto').value()
                idphoto = jpgtostr(idphotoPath)

                photoPath = person.field('photo').value()
                photo = jpgtostr(photoPath)
                inf_photo = ''
                userType = person.field('userType').value()
                dev_mac = self.cjSN
                RegType = person.field('RegType').value()

                self.cdzj.person['idNo'] = idNo
                self.cdzj.person['name'] = name
                self.cdzj.person['gender'] = gender
                self.cdzj.person['nation'] = nation
                self.cdzj.person['birthday'] = birthday
                self.cdzj.person['address'] = address
                self.cdzj.person['idissue'] = idissue
                self.cdzj.person['idperiod'] = idperiod
                self.cdzj.person['idphoto'] = idphoto
                self.cdzj.person['photo'] = photo
                self.cdzj.person['inf_photo'] = inf_photo
                self.cdzj.person['userType'] = userType
                self.cdzj.person['dev_mac'] = dev_mac
                self.cdzj.person['RegType'] = RegType

                self.cdzj.uploadPerson()
                if self.cdzj.msg_uploadPerson == 'success':
                    qs = "update wis_person set zjptStatus = 1 where idNo = '%s'" % idNo
                    self.db.excuteSQl(qs)
                    okMsg = "人员:%s,身份证号:%s,%s成功上传到平台\n" % (name, idNo, datetime.datetime.now())
                    with open('uploadLog.txt', 'a') as f:
                        f.write(okMsg)

                        f.close()

                else:
                    failMsg = "人员:%s,身份证号:%s,%s上传到平台失败，原因:%s\n" % (name, idNo, datetime.datetime.now(), self.cdzj.msg_uploadPerson)
                    with open('uploadLog.txt', 'a') as f:
                        f.write(failMsg)
                        f.close()
                i = i + 1
            QMessageBox.information(self, '提示', '上传结束！', QMessageBox.Yes)
        else:
            QMessageBox.information(self, '提示', '当前没有需要上传的人员！', QMessageBox.Yes)

    @pyqtSlot()
    def on_pb_downloadPerson_clicked(self):
        '''方法作用从住建平台上下载已生成了住建平台号的人员信息'''
        runStatus = True
        progress = QProgressDialog(self)
        progress.setWindowTitle('请稍等')
        progress.setLabelText('数据下载中...')
        progress.setCancelButtonText('中止操作')
        progress.setWindowModality(Qt.WindowModal)
        progress.resize(800, 50)
        while runStatus:
            countD = self.faceDevices.rowCount()

            progress.setRange(0, countD)

            if countD > 0:
                i = 0

                while i < countD:

                    faces = self.faceDevices.record(i)

                    sn = str.strip(faces.field('sn').value())
                    key = str.strip(faces.field('key').value())

                    self.cdzj.downloadPerson(sn, key)
                    if self.cdzj.msg_downloadPerson == 'success':
                        qs = "update wis_person set user_id = '%s', work_sn = '%s' where idNo = '%s'" % (self.cdzj.person['user_id'], self.cdzj.person['work_sn'], self.cdzj.person['idNo'])
                        self.db.excuteSQl(qs)
                        selectQs = "select * from wis_person where idNo = '%s'" % self.cdzj.person['idNo']
                        data = self.db.querySQL(selectQs)
                        countP = data.rowCount()
                        self.cdzj.feedback(sn, 2, '下发成功')
                        progress.setValue(i)
                        if progress.wasCanceled():
                            QMessageBox.warning(self, "提示", "操作失败")
                            break
                        # QMessageBox.information(self, '提示', '本次同步人员数：%d  ' % countP, QMessageBox.Yes)
                    else:
                        runStatus = False
                        progress.close()
                        QMessageBox.information(self, '提示', '同步失败，原因：%s  ' % self.cdzj.msg, QMessageBox.Yes)
                        # self.cdzj.feedback('smz-a03', 3, '下发失败')
                        break
                    i += 1
                else:
                    progress.setValue(countD)
                    QMessageBox.information(self, "提示", "操作成功")

            else:
                progress.deleteLater()
                QMessageBox.information(self, '提示', '未找到考勤设备！', QMessageBox.Yes)
                break


    @pyqtSlot()
    def on_pb_downloadDeletePerson_clicked(self):
        '''方法作用从住建平台上下载已删除的人员信息'''
        runStatus = True
        while runStatus:
            countd = self.faceDevices.rowCount()
            if countd > 0:
                i = 0
                while i < countd:
                    faces = self.faceDevices.record(i)
                    sn = str.strip(faces.field('sn').value())
                    key = str.strip(faces.field('key').value())
                    self.cdzj.downloadDelPerson(sn, key)
                    if self.cdzj.msg_downloadDelPerson == 'success':
                        qs = "update wis_person set personStatus = 0 where idNo = '%s'" % self.cdzj.delPersonID
                        self.db.excuteSQl(qs)
                        self.cdzj.feedback(sn, 0, '人员删除成功')
                        QMessageBox.information(self, '提示', '已同步需删除人员，请手工同步到设备！', QMessageBox.Yes)
                    else:
                        QMessageBox.information(self, '提示', '同步失败，原因：%s  ' % self.cdzj.msg, QMessageBox.Yes)
                        runStatus = False
                        # self.cdzj.feedback('smz-a03', 1, '人员删除失败')
                    i += 1
            else:
                QMessageBox.information(self, '提示', '未找到考勤设备！', QMessageBox.Yes)
                break


    def queryResult(self):
        '''用来处理增加人员后，更新增加人员的情况，同刷新本地数据'''
        qs = "select * from wis_person where personStatus = 1 and deviceStatus = 0"
        persons = self.db.querySQL(qs)
        countP = persons.rowCount()
        if countP > 0:
            i = 0
            while i < countP:
                dic = {}
                person = persons.record(i)
                dic['version'] = '0.2'
                dic['cmd'] = 'query_face'
                dic['per_id'] = person.field('idNo').value()

                dic['id'] = 20
                dic['name'] = ''

                requests.post('http://127.0.0.1:8080/queryFace', data=dic)
                time.sleep(1)
                i += 1
        self.load()



