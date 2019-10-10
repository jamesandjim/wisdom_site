# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginUi.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_login(object):
    def setupUi(self, login):
        login.setObjectName("login")
        login.resize(800, 400)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(login.sizePolicy().hasHeightForWidth())
        login.setSizePolicy(sizePolicy)
        login.setMinimumSize(QtCore.QSize(800, 400))
        login.setMaximumSize(QtCore.QSize(800, 400))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ico/resource/ico/main.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        login.setWindowIcon(icon)
        login.setStyleSheet("")
        self.label_3 = QtWidgets.QLabel(login)
        self.label_3.setGeometry(QtCore.QRect(430, 60, 100, 26))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(0, 0, 255);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(login)
        self.label_4.setGeometry(QtCore.QRect(70, 80, 200, 200))
        self.label_4.setMinimumSize(QtCore.QSize(200, 200))
        self.label_4.setMaximumSize(QtCore.QSize(200, 200))
        self.label_4.setStyleSheet("image: url(:/img/resource/img/login.png);")
        self.label_4.setText("")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.line = QtWidgets.QFrame(login)
        self.line.setGeometry(QtCore.QRect(330, 60, 20, 301))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.widget = QtWidgets.QWidget(login)
        self.widget.setGeometry(QtCore.QRect(430, 270, 291, 41))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pb_login = QtWidgets.QPushButton(self.widget)
        self.pb_login.setMinimumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.pb_login.setFont(font)
        self.pb_login.setStyleSheet("background-color: rgb(0, 170, 255);\n"
"border-radius:4px")
        self.pb_login.setObjectName("pb_login")
        self.horizontalLayout.addWidget(self.pb_login)
        self.pb_esc = QtWidgets.QPushButton(self.widget)
        self.pb_esc.setMinimumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.pb_esc.setFont(font)
        self.pb_esc.setStyleSheet("background-color: rgb(0, 170, 255);\n"
"border-radius:4px")
        self.pb_esc.setObjectName("pb_esc")
        self.horizontalLayout.addWidget(self.pb_esc)
        self.widget1 = QtWidgets.QWidget(login)
        self.widget1.setGeometry(QtCore.QRect(430, 120, 291, 32))
        self.widget1.setObjectName("widget1")
        self.formLayout = QtWidgets.QFormLayout(self.widget1)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.le_userName = QtWidgets.QLineEdit(self.widget1)
        self.le_userName.setMinimumSize(QtCore.QSize(210, 30))
        self.le_userName.setStyleSheet("QLineEdit {\n"
"    border:1px solid rgb(180, 180, 180);\n"
"    background:rgb(230,230,230);\n"
"    border-radius:4px\n"
"}")
        self.le_userName.setObjectName("le_userName")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.le_userName)
        self.widget2 = QtWidgets.QWidget(login)
        self.widget2.setGeometry(QtCore.QRect(430, 190, 291, 32))
        self.widget2.setObjectName("widget2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.widget2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.le_passWord = QtWidgets.QLineEdit(self.widget2)
        self.le_passWord.setMinimumSize(QtCore.QSize(210, 30))
        self.le_passWord.setStyleSheet("QLineEdit {\n"
"    border:1px solid rgb(180, 180, 180);\n"
"    background:rgb(230,230,230);\n"
"    border-radius:4px\n"
"}")
        self.le_passWord.setEchoMode(QtWidgets.QLineEdit.Password)
        self.le_passWord.setObjectName("le_passWord")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.le_passWord)

        self.retranslateUi(login)
        QtCore.QMetaObject.connectSlotsByName(login)

    def retranslateUi(self, login):
        _translate = QtCore.QCoreApplication.translate
        login.setWindowTitle(_translate("login", "登录"))
        self.label_3.setText(_translate("login", "登录/Login"))
        self.pb_login.setText(_translate("login", "登  录"))
        self.pb_esc.setText(_translate("login", "退  出"))
        self.le_userName.setPlaceholderText(_translate("login", "用户登录名称"))
        self.le_passWord.setPlaceholderText(_translate("login", "用户登录密码"))
import resource_rc
