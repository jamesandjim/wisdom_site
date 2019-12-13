# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'registerUi.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(561, 189)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(10, 10, 541, 161))
        self.widget.setObjectName("widget")
        self.formLayout = QtWidgets.QFormLayout(self.widget)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setSpacing(10)
        self.formLayout.setObjectName("formLayout")
        self.label_company = QtWidgets.QLabel(self.widget)
        self.label_company.setObjectName("label_company")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_company)
        self.lineEdit_company = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_company.setObjectName("lineEdit_company")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_company)
        self.label_xlh = QtWidgets.QLabel(self.widget)
        self.label_xlh.setObjectName("label_xlh")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_xlh)
        self.lineEdit_xlh = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_xlh.setObjectName("lineEdit_xlh")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_xlh)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineEdit_zcm = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_zcm.setObjectName("lineEdit_zcm")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_zcm)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pb_esc = QtWidgets.QPushButton(self.widget)
        self.pb_esc.setObjectName("pb_esc")
        self.horizontalLayout.addWidget(self.pb_esc)
        self.pb_ok = QtWidgets.QPushButton(self.widget)
        self.pb_ok.setObjectName("pb_ok")
        self.horizontalLayout.addWidget(self.pb_ok)
        self.formLayout.setLayout(3, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "软件注册"))
        self.label_company.setText(_translate("Dialog", "公司名称："))
        self.label_xlh.setText(_translate("Dialog", "序列号："))
        self.label.setText(_translate("Dialog", "注册码："))
        self.pb_esc.setText(_translate("Dialog", "取    消"))
        self.pb_ok.setText(_translate("Dialog", "注    册"))
