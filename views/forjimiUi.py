# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forjimiUi.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_form_main(object):
    def setupUi(self, form_main):
        form_main.setObjectName("form_main")
        form_main.resize(600, 200)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(form_main.sizePolicy().hasHeightForWidth())
        form_main.setSizePolicy(sizePolicy)
        form_main.setMinimumSize(QtCore.QSize(600, 200))
        self.verticalLayout = QtWidgets.QVBoxLayout(form_main)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignCenter)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout.setVerticalSpacing(20)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(form_main)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineEdit_xlh = QtWidgets.QLineEdit(form_main)
        self.lineEdit_xlh.setObjectName("lineEdit_xlh")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_xlh)
        self.label_2 = QtWidgets.QLabel(form_main)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lineEdit_zcm = QtWidgets.QLineEdit(form_main)
        self.lineEdit_zcm.setObjectName("lineEdit_zcm")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_zcm)
        self.verticalLayout.addLayout(self.formLayout)
        self.pb_ok = QtWidgets.QPushButton(form_main)
        self.pb_ok.setObjectName("pb_ok")
        self.verticalLayout.addWidget(self.pb_ok)

        self.retranslateUi(form_main)
        QtCore.QMetaObject.connectSlotsByName(form_main)

    def retranslateUi(self, form_main):
        _translate = QtCore.QCoreApplication.translate
        form_main.setWindowTitle(_translate("form_main", "Form"))
        self.label.setText(_translate("form_main", "序列号："))
        self.label_2.setText(_translate("form_main", "注册码："))
        self.pb_ok.setText(_translate("form_main", "生成注册码"))
