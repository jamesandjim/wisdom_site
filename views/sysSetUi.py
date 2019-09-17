# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sysSetUi.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_sysSetForm(object):
    def setupUi(self, sysSetForm):
        sysSetForm.setObjectName("sysSetForm")
        sysSetForm.resize(835, 559)
        sysSetForm.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        self.verticalLayout = QtWidgets.QVBoxLayout(sysSetForm)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(sysSetForm)
        self.widget.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(5, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)
        self.verticalLayout.addWidget(self.widget)

        self.retranslateUi(sysSetForm)
        QtCore.QMetaObject.connectSlotsByName(sysSetForm)

    def retranslateUi(self, sysSetForm):
        _translate = QtCore.QCoreApplication.translate
        sysSetForm.setWindowTitle(_translate("sysSetForm", "系统参数设置"))
        self.pushButton.setText(_translate("sysSetForm", "PushButton"))
