import base64
import requests
import shutil

from PyQt5.QtWidgets import QWidget, QMessageBox, QFileDialog
from PyQt5 import QtSql
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.Qt import QImage, QPixmap

from views import infoCollectionUi
from devices import zkCardReader
from devices import klCardReader
from models.dbtools import Dboperator
from devices.face03 import Face_device
from devices.camera import CameraDev
from devices.face01 import FaceDevice

from commTools import st_des, toBASE64


class InfoCollectionCls(QWidget, infoCollectionUi.Ui_infoCollectionForm):
    def __init__(self, parent=None):
        super(InfoCollectionCls, self).__init__(parent)
        self.setupUi(self)
        self.face = FaceDevice()
        self.pb_cj.setVisible(False)
        self.pb_refresh_photo.setVisible(False)
        # self.cr = zkCardReader.CardReader()
        self.db = Dboperator()

        self.load()

    def load(self):
        qs = "select name from wis_department"
        data = self.db.querySQL(qs)
        self.cb_department.setModel(data)


    @pyqtSlot()
    def on_pb_refresh_photo_clicked(self):
        """刷新考勤设备照片 处理函数"""
        img = QPixmap('./photos_face/{}.jpg'.format(self.le_idNum.text()))
        self.lb_photo3.setPixmap(img)

    @pyqtSlot()
    def on_pb_camera_clicked(self):
        """从摄像头拍照 处理函数"""
        try:
            cam_Dev = CameraDev()
            cam_Dev.filename = self.le_idNum.text()
            cam_Dev.take_photo()
            srcImg = './photos_face/{}.jpg'.format(cam_Dev.filename)
            dstImg = './photos_face/{}_face.jpg'.format(cam_Dev.filename)
            r = self.face.getFacePos(srcImg, dstImg)
            if r:
                img = QPixmap(dstImg)

                self.lb_photo3.setPixmap(img)
            else:
                QMessageBox.information(self, '提示', '图片中未检测到头像，请重试！', QMessageBox.Yes)
        except Exception as e:
            QMessageBox.information(self, '提示', '未检测到摄像头！', QMessageBox.Yes)

    @pyqtSlot()
    def on_pb_cj_photo_clicked(self):
        """从考勤设备拍摄照片 处理函数"""
        face = Face_device('192.168.0.105')
        person = {"id": str(self.le_idNum.text()), "name": str(self.le_name.text())}

        if face.createPerson(person):

            if face.takeImg(person["id"]):
                map = QPixmap("./photos_face/{}".format(self.le_idNum.text()))
                self.lb_photo3.setPixmap(map)
            else:
                QMessageBox.information(self, '提示', '不能拍照', QMessageBox.Yes)
        else:
            QMessageBox.information(self, '提示', '不能创建人员', QMessageBox.Yes)

    @pyqtSlot()
    def on_pb_readall_clicked(self):
        """人员信息列表 处理函数"""
        queryModel = self.db.querySQL('select * from wis_person')
        self.tableView.setModel(queryModel)
        queryModel.setHeaderData(0, Qt.Horizontal, '身份证号')
        queryModel.setHeaderData(1, Qt.Horizontal, '姓名')
        queryModel.setHeaderData(2, Qt.Horizontal, '性别')
        queryModel.setHeaderData(3, Qt.Horizontal, '民族')
        queryModel.setHeaderData(4, Qt.Horizontal, '出生日期')
        queryModel.setHeaderData(5, Qt.Horizontal, '住址')
        queryModel.setHeaderData(6, Qt.Horizontal, '发证机关')
        queryModel.setHeaderData(7, Qt.Horizontal, '证件有效期')
        queryModel.setHeaderData(8, Qt.Horizontal, '身份证照片')
        queryModel.setHeaderData(9, Qt.Horizontal, '人员可见光照片')
        queryModel.setHeaderData(10, Qt.Horizontal, '人员红外照片')
        queryModel.setHeaderData(11, Qt.Horizontal, '人员类型')
        queryModel.setHeaderData(12, Qt.Horizontal, '设备序列号')
        queryModel.setHeaderData(13, Qt.Horizontal, '注册类别')
        queryModel.setHeaderData(14, Qt.Horizontal, '住建平台ID')
        queryModel.setHeaderData(15, Qt.Horizontal, '用户工号')
        queryModel.setHeaderData(16, Qt.Horizontal, '所属班组或部门')
        queryModel.setHeaderData(17, Qt.Horizontal, '数据状态')

    @pyqtSlot()
    def on_pb_save_upload_clicked(self):
        """保存数据到本地 处理函数"""
        idperiod = str('{}-{}'.format(self.le_effectedDate.text(), self.le_expiredDate.text()))
        idNo = str(self.le_idNum.text())
        name = str(self.le_name.text())
        gender = 1 if self.le_sex.text() == '男' else 2
        nation = str(self.le_nation.text())
        birthday = str(self.le_birthdate.text())
        address = str(self.le_address.text())
        idissue = str(self.le_issue.text())
        idphoto = "./photos_kl/{}.jpg".format(self.le_idNum.text())
        photo = './photos_face/{}.jpg'.format(self.le_idNum.text())
        inf_photo = ""
        userType = 1

        RegType = 3 if self.cb_RegType.currentText() == '人脸采集' else 1
        user_id = ""
        work_sn = ""
        department = str(self.cb_department.currentText())
        deviceStatus = 0
        zjptStatus = 0
        if self.checkbox_uploadYN.isChecked():
            uploadYN = 1
        else:
            uploadYN = 0
        if self.rb_personStatus1.isChecked():
            personStatus = 1
        else:
            personStatus = 2

        if idNo != '':

            q_sql = "select * from wis_person where idNo = '%s'" % idNo
            query = self.db.querySQL(q_sql)
            if query.rowCount() > 0:
                QMessageBox.information(self, '提示', '人员信息重复！', QMessageBox.Yes)
            else:

                sql = "INSERT INTO wis_person VALUES('%s','%s',%d,'%s','%s','%s','%s','%s','%s','%s','%s',%d,%d,'%s','%s','%s',%d,%d,%d,%d)" % (idNo, name, gender, nation, birthday, address, idissue, idperiod, idphoto, photo, inf_photo, userType, RegType, user_id, work_sn, department, deviceStatus, zjptStatus, uploadYN, personStatus)

                self.db.excuteSQl(sql)
                QMessageBox.information(self, '提示', '人员信息采集成功！', QMessageBox.Yes)
        else:
            QMessageBox.information(self, '提示', '人员信息为空！', QMessageBox.Yes)

    @pyqtSlot()
    def on_pb_uploadPhoto_clicked(self):
        """使用电脑中的照片 处理函数"""
        path, imptype = QFileDialog.getOpenFileName(self, '选择用于识别的人像', '/', 'jpg(*.jpg);;bmp(*.bmp)')
        img = QPixmap(path)
        self.lb_photo2.setPixmap(img)
        self.lb_photo2.setScaledContents(True)
        newpath = './photos_face/{}.jpg'.format(self.le_idNum.text())
        shutil.copyfile(path, newpath)
        srcImg = './photos_face/{}.jpg'.format(self.le_idNum.text())
        dstImg = './photos_face/{}_face.jpg'.format(self.le_idNum.text())
        r = self.face.getFacePos(srcImg, dstImg)
        if r:
            img = QPixmap(dstImg)

            self.lb_photo3.setPixmap(img)
        else:
            QMessageBox.information(self, '提示', '图片中未检测到头像，请重选图片！', QMessageBox.Yes)

    @pyqtSlot()
    def on_pb_cj1_clicked(self):
        """读身份证信息 处理函数"""
        self.pb_cj1.setText('信息读取中....')
        self.lb_photo.clear()
        self.lb_photo2.clear()
        self.lb_photo3.clear()
        try:
            cr = klCardReader.CardReader()
        except Exception as e:
            return e
        r = cr.openDevice()

        if r == 0:
            try:
                r = cr.readCard()
                if r == 0:
                    self.le_name.setText(cr.info['name'])
                    self.le_address.setText(cr.info['address'])
                    self.le_sex.setText(cr.info['sexDesc'])
                    self.le_nation.setText(cr.info['nationDesc'])
                    self.le_birthdate.setText(cr.info['born'])
                    self.le_idNum.setText(cr.info['cardNo'])
                    self.le_issue.setText(cr.info['issuedAt'])
                    self.le_effectedDate.setText(cr.info['effectedDate'])
                    self.le_expiredDate.setText(cr.info['expiredDate'])

                    image = QPixmap("./photos_kl/{}.jpg".format(cr.info['cardNo']))
                    self.lb_photo.setPixmap(image)
                else:
                    QMessageBox.information(self, '提示', '请确认身份证是否放到阅读器上！', QMessageBox.Yes)
            except Exception as e:
                QMessageBox.information(self, '提示', '读卡失败，{}'.format(e), QMessageBox.Yes)
            finally:
                cr.closeDevice()
                self.pb_cj1.setText('读身份证信息')
        else:
            QMessageBox.information(self, '提示', '身份证阅读器打开失败！', QMessageBox.Yes)

    @pyqtSlot()
    def on_pb_cj_clicked(self):
        """读身份证信息（中控） 处理函数"""
        try:
            cr = zkCardReader.CardReader()
        except Exception as e:
            return e

        if cr.openDevice() > 0:

            re = cr.readCard()
            if re == 1:
                self.le_name.setText(cr.info['name'])
                self.le_address.setText(cr.info['address'])
                self.le_sex.setText(cr.info['sex'])
                self.le_nation.setText(cr.info['nation'])
                self.le_birthdate.setText(cr.info['birthdate'])
                self.le_idNum.setText(cr.info['idNum'])
                self.le_issue.setText(cr.info['issue'])
                self.le_effectedDate.setText(str(cr.info['effectedDate']))
                self.le_expiredDate.setText(str(cr.info['expiredDate']))

                photo = base64.b64decode(cr.info['b_Photo'])

                q_photo = QImage.fromData(photo)
                image = QPixmap.fromImage(q_photo)
                self.lb_photo.setPixmap(image)
                cr.closeDevice()

            else:
                QMessageBox.information(self, '提示', '请重新放置身份证！', QMessageBox.Yes)

        else:
            QMessageBox.information(self, '提示', '身份证阅读器打开失败！', QMessageBox.Yes)

    @pyqtSlot()
    def on_pb_uploadPerson_clicked(self):
        pass






