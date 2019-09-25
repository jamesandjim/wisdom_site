# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'zjptUi.ui'
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
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.toolBox = QtWidgets.QToolBox(Form)
        self.toolBox.setStyleSheet("QToolBox #toolBox{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius:5px;\n"
"}")
        self.toolBox.setObjectName("toolBox")
        self.page_cdzj = QtWidgets.QWidget()
        self.page_cdzj.setGeometry(QtCore.QRect(0, 0, 907, 606))
        self.page_cdzj.setStyleSheet("QWidget #page_cdzj{\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.page_cdzj.setObjectName("page_cdzj")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.page_cdzj)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout_2.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.formLayout.setVerticalSpacing(10)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.page_cdzj)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.le_uploadPersonURL = QtWidgets.QLineEdit(self.page_cdzj)
        self.le_uploadPersonURL.setObjectName("le_uploadPersonURL")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.le_uploadPersonURL)
        self.label_2 = QtWidgets.QLabel(self.page_cdzj)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.le_deleteURL = QtWidgets.QLineEdit(self.page_cdzj)
        self.le_deleteURL.setObjectName("le_deleteURL")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.le_deleteURL)
        self.label_3 = QtWidgets.QLabel(self.page_cdzj)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.le_uploadAttURL = QtWidgets.QLineEdit(self.page_cdzj)
        self.le_uploadAttURL.setObjectName("le_uploadAttURL")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.le_uploadAttURL)
        self.label_4 = QtWidgets.QLabel(self.page_cdzj)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.le_feedbackURL = QtWidgets.QLineEdit(self.page_cdzj)
        self.le_feedbackURL.setObjectName("le_feedbackURL")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.le_feedbackURL)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pb_update = QtWidgets.QPushButton(self.page_cdzj)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_update.sizePolicy().hasHeightForWidth())
        self.pb_update.setSizePolicy(sizePolicy)
        self.pb_update.setObjectName("pb_update")
        self.horizontalLayout.addWidget(self.pb_update)
        self.pb_save = QtWidgets.QPushButton(self.page_cdzj)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_save.sizePolicy().hasHeightForWidth())
        self.pb_save.setSizePolicy(sizePolicy)
        self.pb_save.setObjectName("pb_save")
        self.horizontalLayout.addWidget(self.pb_save)
        self.formLayout.setLayout(5, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.formLayout)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        self.toolBox.addItem(self.page_cdzj, "")
        self.page_myzj = QtWidgets.QWidget()
        self.page_myzj.setGeometry(QtCore.QRect(0, 0, 907, 606))
        self.page_myzj.setStyleSheet("QWidget #page_myzj{\n"
"background-color: rgb(255, 255, 255);\n"
"}")
        self.page_myzj.setObjectName("page_myzj")
        self.toolBox.addItem(self.page_myzj, "")
        self.gridLayout.addWidget(self.toolBox, 0, 0, 1, 1)

        self.retranslateUi(Form)
        self.toolBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "人员信息上传地址"))
        self.label_2.setText(_translate("Form", "人员信息删除地址"))
        self.label_3.setText(_translate("Form", "考勤信息上传地址"))
        self.label_4.setText(_translate("Form", "操作结果反馈地址"))
        self.pb_update.setText(_translate("Form", "修改"))
        self.pb_save.setText(_translate("Form", "保存"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_cdzj), _translate("Form", "成都住建平台信息"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_myzj), _translate("Form", "绵阳住建平台信息"))
