# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'infoCollectionUi.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_infoCollectionForm(object):
    def setupUi(self, infoCollectionForm):
        infoCollectionForm.setObjectName("infoCollectionForm")
        infoCollectionForm.setWindowModality(QtCore.Qt.WindowModal)
        infoCollectionForm.resize(889, 551)
        infoCollectionForm.setStyleSheet("")
        self.gridLayout = QtWidgets.QGridLayout(infoCollectionForm)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.info_main = QtWidgets.QWidget(infoCollectionForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.info_main.sizePolicy().hasHeightForWidth())
        self.info_main.setSizePolicy(sizePolicy)
        self.info_main.setStyleSheet("QWidget #info_main{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius:5px;\n"
"}")
        self.info_main.setObjectName("info_main")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.info_main)
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.info_main)
        self.tabWidget.setStyleSheet("QTabWidget #tabWidget{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius:5px;\n"
"}")
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setIconSize(QtCore.QSize(20, 20))
        self.tabWidget.setElideMode(QtCore.Qt.ElideMiddle)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setStyleSheet("QWidget #tab{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius:5px;\n"
"}")
        self.tab.setObjectName("tab")
        self.layoutWidget = QtWidgets.QWidget(self.tab)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 30, 591, 713))
        self.layoutWidget.setObjectName("layoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.layoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setVerticalSpacing(10)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.le_name = QtWidgets.QLineEdit(self.layoutWidget)
        self.le_name.setObjectName("le_name")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.le_name)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.le_sex = QtWidgets.QLineEdit(self.layoutWidget)
        self.le_sex.setObjectName("le_sex")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.le_sex)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.le_nation = QtWidgets.QLineEdit(self.layoutWidget)
        self.le_nation.setObjectName("le_nation")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.le_nation)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.le_birthdate = QtWidgets.QLineEdit(self.layoutWidget)
        self.le_birthdate.setObjectName("le_birthdate")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.le_birthdate)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.le_address = QtWidgets.QLineEdit(self.layoutWidget)
        self.le_address.setObjectName("le_address")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.le_address)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.le_idNum = QtWidgets.QLineEdit(self.layoutWidget)
        self.le_idNum.setObjectName("le_idNum")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.le_idNum)
        self.label_9 = QtWidgets.QLabel(self.layoutWidget)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.le_issue = QtWidgets.QLineEdit(self.layoutWidget)
        self.le_issue.setObjectName("le_issue")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.le_issue)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.le_effectedDate = QtWidgets.QLineEdit(self.layoutWidget)
        self.le_effectedDate.setObjectName("le_effectedDate")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.le_effectedDate)
        self.label_10 = QtWidgets.QLabel(self.layoutWidget)
        self.label_10.setObjectName("label_10")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.le_expiredDate = QtWidgets.QLineEdit(self.layoutWidget)
        self.le_expiredDate.setObjectName("le_expiredDate")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.le_expiredDate)
        self.lb_photo = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lb_photo.sizePolicy().hasHeightForWidth())
        self.lb_photo.setSizePolicy(sizePolicy)
        self.lb_photo.setMinimumSize(QtCore.QSize(200, 200))
        self.lb_photo.setMaximumSize(QtCore.QSize(200, 200))
        self.lb_photo.setScaledContents(False)
        self.lb_photo.setObjectName("lb_photo")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.lb_photo)
        self.lb_photo2 = QtWidgets.QLabel(self.layoutWidget)
        self.lb_photo2.setMinimumSize(QtCore.QSize(200, 200))
        self.lb_photo2.setMaximumSize(QtCore.QSize(200, 200))
        self.lb_photo2.setObjectName("lb_photo2")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.lb_photo2)
        self.lb_photo3 = QtWidgets.QLabel(self.tab)
        self.lb_photo3.setGeometry(QtCore.QRect(760, 270, 240, 320))
        self.lb_photo3.setMinimumSize(QtCore.QSize(240, 320))
        self.lb_photo3.setMaximumSize(QtCore.QSize(240, 320))
        self.lb_photo3.setScaledContents(True)
        self.lb_photo3.setObjectName("lb_photo3")
        self.layoutWidget1 = QtWidgets.QWidget(self.tab)
        self.layoutWidget1.setGeometry(QtCore.QRect(630, 30, 231, 231))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pb_cj = QtWidgets.QPushButton(self.layoutWidget1)
        self.pb_cj.setFlat(False)
        self.pb_cj.setObjectName("pb_cj")
        self.verticalLayout.addWidget(self.pb_cj)
        self.pb_cj1 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pb_cj1.setObjectName("pb_cj1")
        self.verticalLayout.addWidget(self.pb_cj1)
        self.pb_uploadPhoto = QtWidgets.QPushButton(self.layoutWidget1)
        self.pb_uploadPhoto.setFlat(False)
        self.pb_uploadPhoto.setObjectName("pb_uploadPhoto")
        self.verticalLayout.addWidget(self.pb_uploadPhoto)
        self.pb_save_upload = QtWidgets.QPushButton(self.layoutWidget1)
        self.pb_save_upload.setObjectName("pb_save_upload")
        self.verticalLayout.addWidget(self.pb_save_upload)
        self.pb_camera = QtWidgets.QPushButton(self.layoutWidget1)
        self.pb_camera.setObjectName("pb_camera")
        self.verticalLayout.addWidget(self.pb_camera)
        self.pb_cj_photo = QtWidgets.QPushButton(self.layoutWidget1)
        self.pb_cj_photo.setObjectName("pb_cj_photo")
        self.verticalLayout.addWidget(self.pb_cj_photo)
        self.pb_refresh_photo = QtWidgets.QPushButton(self.layoutWidget1)
        self.pb_refresh_photo.setObjectName("pb_refresh_photo")
        self.verticalLayout.addWidget(self.pb_refresh_photo)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setStyleSheet("QWidget #tab_2{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius:5px;\n"
"}")
        self.tab_2.setObjectName("tab_2")
        self.tableView = QtWidgets.QTableView(self.tab_2)
        self.tableView.setGeometry(QtCore.QRect(0, 10, 811, 381))
        self.tableView.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableView.setGridStyle(QtCore.Qt.DotLine)
        self.tableView.setObjectName("tableView")
        self.pb_readall = QtWidgets.QPushButton(self.tab_2)
        self.pb_readall.setGeometry(QtCore.QRect(880, 80, 91, 31))
        self.pb_readall.setObjectName("pb_readall")
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        self.gridLayout.addWidget(self.info_main, 0, 0, 1, 1)

        self.retranslateUi(infoCollectionForm)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(infoCollectionForm)

    def retranslateUi(self, infoCollectionForm):
        _translate = QtCore.QCoreApplication.translate
        infoCollectionForm.setWindowTitle(_translate("infoCollectionForm", "Form"))
        self.label_2.setText(_translate("infoCollectionForm", "TextLabel"))
        self.label_3.setText(_translate("infoCollectionForm", "TextLabel"))
        self.label_4.setText(_translate("infoCollectionForm", "TextLabel"))
        self.label_5.setText(_translate("infoCollectionForm", "TextLabel"))
        self.label_8.setText(_translate("infoCollectionForm", "TextLabel"))
        self.label_6.setText(_translate("infoCollectionForm", "TextLabel"))
        self.label_9.setText(_translate("infoCollectionForm", "TextLabel"))
        self.label_7.setText(_translate("infoCollectionForm", "TextLabel"))
        self.label_10.setText(_translate("infoCollectionForm", "TextLabel"))
        self.lb_photo.setText(_translate("infoCollectionForm", "TextLabel"))
        self.lb_photo2.setText(_translate("infoCollectionForm", "TextLabel"))
        self.lb_photo3.setText(_translate("infoCollectionForm", "TextLabel"))
        self.pb_cj.setText(_translate("infoCollectionForm", "采   集"))
        self.pb_cj1.setText(_translate("infoCollectionForm", "读身份证信息"))
        self.pb_uploadPhoto.setText(_translate("infoCollectionForm", "上传人员照片"))
        self.pb_save_upload.setText(_translate("infoCollectionForm", "保存数据到本地"))
        self.pb_camera.setText(_translate("infoCollectionForm", "从摄像头拍照"))
        self.pb_cj_photo.setText(_translate("infoCollectionForm", "从考勤设备拍摄照片"))
        self.pb_refresh_photo.setText(_translate("infoCollectionForm", "刷新考勤设备照片"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("infoCollectionForm", "人员信息采集"))
        self.pb_readall.setText(_translate("infoCollectionForm", "获取人员列表"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("infoCollectionForm", "人员信息列表"))
