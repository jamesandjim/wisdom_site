import base64
from PyQt5.QtWidgets import QWidget, QMessageBox, QFileDialog
from PyQt5 import QtSql, QtGui
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.Qt import QImage, QPixmap

import info_collection
from devices import zkCardReader
from models.dbtools import Dboperator
from devices.face01 import Face_device


class Info_Ui(QWidget, info_collection.Ui_info_collect_Form):
    def __init__(self, parent=None):
        super(Info_Ui, self).__init__(parent)
        self.setupUi(self)
        self.cr = zkCardReader.CardReader()
        self.db = Dboperator()

    @pyqtSlot()
    def on_pb_cj_photo_clicked(self):
        face = Face_device('192.168.0.105')
        if face.setPassWord():
            face.getDeviceKey()
        else:
            print('无法联接设备')

    @pyqtSlot()
    def on_pb_readall_clicked(self):
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

        idperiod = str('{}-{}'.format(str(self.cr.info['effectedDate']), str(self.cr.info['expiredDate'])))
        idNo = str(self.le_idNum.text())
        name = str(self.le_name.text())
        gender = 1 if self.le_sex.text() == '男' else 0
        nation = str(self.le_nation.text())
        birthday = str(self.le_birthdate.text())
        address = str(self.le_address.text())
        idissue = str(self.le_issue.text())
        idphoto = "akdkdk"
        photo = "iejeii"
        inf_photo = "erqer"
        userType = 1
        dev_mac = "cj_kdk"
        RegType = 3
        user_id = ""
        work_sn = ""
        department = 1
        status = 0

        q_sql = "select * from wis_person where idNo = '%s'" % idNo
        self.db.excuteSQl(q_sql)
        if self.db.query.next():
            QMessageBox.information(self, '提示', '人员信息重复！', QMessageBox.Yes)
        else:

            sql = "INSERT INTO wis_person VALUES('%s','%s',%d,'%s','%s','%s','%s','%s','%s','%s','%s',%d,'%s',%d,'%s','%s',%d,%d)" % (idNo, name, gender, nation, birthday, address, idissue, idperiod, idphoto, photo, inf_photo, userType, dev_mac, RegType, user_id, work_sn, department, status)
            print(sql)

            self.db.excuteSQl(sql)


    @pyqtSlot()
    def on_pb_uploadPhoto_clicked(self):
        path, imptype = QFileDialog.getOpenFileName(self, '选择用于识别的人像', '/', 'jpg(*.jpg);;bmp(*.bmp)')
        img = QPixmap(path)
        self.lb_photo2.setPixmap(img)
        self.lb_photo2.setScaledContents(True)
        print(path)

    @pyqtSlot()
    def on_pushButton_clicked(self):
        self.querydb()
        print('xxx')

    @pyqtSlot()
    def on_pb_cj_clicked(self):


        if self.cr.openDevice() > 0:

            re = self.cr.readCard()
            if re == 1:
                self.le_name.setText(self.cr.info['name'])
                self.le_address.setText(self.cr.info['address'])
                self.le_sex.setText(self.cr.info['sex'])
                self.le_nation.setText(self.cr.info['nation'])
                self.le_birthdate.setText(self.cr.info['birthdate'])
                self.le_idNum.setText(self.cr.info['idNum'])
                self.le_issue.setText(self.cr.info['issue'])
                self.le_effectedDate.setText(str(self.cr.info['effectedDate']))
                self.le_expiredDate.setText(str(self.cr.info['expiredDate']))

                photo = base64.b64decode(self.cr.info['b_Photo'])

                q_photo = QImage.fromData(photo)
                image = QPixmap.fromImage(q_photo)
                self.lb_photo.setPixmap(image)



            else:
                QMessageBox.information(self, '提示', '请重新放置身份证！', QMessageBox.Yes)

        else:
            QMessageBox.information(self, '提示', '身份证阅读器打开失败！', QMessageBox.Yes)


    def opendb(self):
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')

        db.setDatabaseName('./db/wisdom.db')
        db.open()

    def querydb(self):
        self.opendb()
        # query = QtSql.QSqlQuery()
        query = QtSql.QSqlQueryModel()
        query.setQuery('select bookname as 书名, bookid as 书号, auth as 作者, category as 书类, publisher as 出版社 from book')
        # query.setQuery('select * from book')
        self.tableView.setModel(query)





