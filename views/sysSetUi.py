# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sysSetUi.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(907, 658)
        Form.setStyleSheet("QWidget #Form{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius:5px;\n"
"}")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.toolBox = QtWidgets.QToolBox(Form)
        self.toolBox.setStyleSheet("QToolBox #toolBox{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius:5px;\n"
"}")
        self.toolBox.setObjectName("toolBox")
        self.page_jbcs = QtWidgets.QWidget()
        self.page_jbcs.setGeometry(QtCore.QRect(0, 0, 907, 580))
        self.page_jbcs.setStyleSheet("QWidget #page_jbcs{\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.page_jbcs.setObjectName("page_jbcs")
        self.label_2 = QtWidgets.QLabel(self.page_jbcs)
        self.label_2.setGeometry(QtCore.QRect(28, 15, 96, 16))
        self.label_2.setObjectName("label_2")
        self.checkBox = QtWidgets.QCheckBox(self.page_jbcs)
        self.checkBox.setGeometry(QtCore.QRect(130, 15, 95, 16))
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName("checkBox")
        self.label = QtWidgets.QLabel(self.page_jbcs)
        self.label.setGeometry(QtCore.QRect(28, 43, 72, 16))
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(self.page_jbcs)
        self.comboBox.setGeometry(QtCore.QRect(128, 45, 241, 20))
        self.comboBox.setObjectName("comboBox")
        self.label_3 = QtWidgets.QLabel(self.page_jbcs)
        self.label_3.setGeometry(QtCore.QRect(28, 195, 72, 16))
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(self.page_jbcs)
        self.lineEdit.setGeometry(QtCore.QRect(130, 195, 641, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.checkBox_4 = QtWidgets.QCheckBox(self.page_jbcs)
        self.checkBox_4.setGeometry(QtCore.QRect(128, 95, 227, 16))
        self.checkBox_4.setObjectName("checkBox_4")
        self.label_4 = QtWidgets.QLabel(self.page_jbcs)
        self.label_4.setGeometry(QtCore.QRect(28, 163, 84, 16))
        self.label_4.setObjectName("label_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.page_jbcs)
        self.lineEdit_2.setGeometry(QtCore.QRect(130, 163, 641, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_5 = QtWidgets.QLabel(self.page_jbcs)
        self.label_5.setGeometry(QtCore.QRect(28, 133, 96, 16))
        self.label_5.setObjectName("label_5")
        self.spinBox = QtWidgets.QSpinBox(self.page_jbcs)
        self.spinBox.setGeometry(QtCore.QRect(130, 133, 38, 18))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBox.sizePolicy().hasHeightForWidth())
        self.spinBox.setSizePolicy(sizePolicy)
        self.spinBox.setObjectName("spinBox")
        self.widget = QtWidgets.QWidget(self.page_jbcs)
        self.widget.setGeometry(QtCore.QRect(130, 250, 176, 43))
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_2.addWidget(self.pushButton_3)
        self.pushButton = QtWidgets.QPushButton(self.page_jbcs)
        self.pushButton.setGeometry(QtCore.QRect(130, 221, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.toolBox.addItem(self.page_jbcs, "")
        self.page_sbcs = QtWidgets.QWidget()
        self.page_sbcs.setGeometry(QtCore.QRect(0, 0, 907, 580))
        self.page_sbcs.setStyleSheet("QWidget #page_myzj{\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.page_sbcs.setObjectName("page_sbcs")
        self.checkBox_2 = QtWidgets.QCheckBox(self.page_sbcs)
        self.checkBox_2.setGeometry(QtCore.QRect(50, 50, 231, 16))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.page_sbcs)
        self.checkBox_3.setGeometry(QtCore.QRect(50, 100, 191, 16))
        self.checkBox_3.setObjectName("checkBox_3")
        self.toolBox.addItem(self.page_sbcs, "")
        self.page_qtcs = QtWidgets.QWidget()
        self.page_qtcs.setObjectName("page_qtcs")
        self.toolBox.addItem(self.page_qtcs, "")
        self.verticalLayout.addWidget(self.toolBox)

        self.retranslateUi(Form)
        self.toolBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "是否联接住建平台"))
        self.checkBox.setText(_translate("Form", "接入住建平台"))
        self.label.setText(_translate("Form", "住建平台选择"))
        self.label_3.setText(_translate("Form", "数据备份目录"))
        self.checkBox_4.setText(_translate("Form", "后台自动处理人员及考勤信息上传下载"))
        self.label_4.setText(_translate("Form", "本地服务器地址"))
        self.label_5.setText(_translate("Form", "后台处理时间间隔"))
        self.pushButton_2.setText(_translate("Form", "修改"))
        self.pushButton_3.setText(_translate("Form", "保存"))
        self.pushButton.setText(_translate("Form", "选择目录"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_jbcs), _translate("Form", "系统运行基本参数"))
        self.checkBox_2.setText(_translate("Form", "人脸照片上传后立即与身份证对比"))
        self.checkBox_3.setText(_translate("Form", "未带安全帽不允许进场"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_sbcs), _translate("Form", "设备功能参数"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_qtcs), _translate("Form", "其他参数"))
