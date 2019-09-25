# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'attendanceManagementUi.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.WindowModal)
        Form.resize(1034, 738)
        Form.setStyleSheet("QWidget #Form{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius:5px;\n"
"}")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setStyleSheet("QWidget #widget{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius:5px;\n"
"}")
        self.widget.setObjectName("widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_3.addItem(spacerItem)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(10, 10, 10, 0)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.le_queryPara = QtWidgets.QLineEdit(self.widget)
        self.le_queryPara.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.le_queryPara.setObjectName("le_queryPara")
        self.horizontalLayout_2.addWidget(self.le_queryPara)
        self.pb_cj_att = QtWidgets.QPushButton(self.widget)
        self.pb_cj_att.setObjectName("pb_cj_att")
        self.horizontalLayout_2.addWidget(self.pb_cj_att)
        self.pb_uploadAtt = QtWidgets.QPushButton(self.widget)
        self.pb_uploadAtt.setObjectName("pb_uploadAtt")
        self.horizontalLayout_2.addWidget(self.pb_uploadAtt)
        self.pb_query = QtWidgets.QPushButton(self.widget)
        self.pb_query.setObjectName("pb_query")
        self.horizontalLayout_2.addWidget(self.pb_query)
        self.pb_allData = QtWidgets.QPushButton(self.widget)
        self.pb_allData.setObjectName("pb_allData")
        self.horizontalLayout_2.addWidget(self.pb_allData)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_3.addItem(spacerItem2)
        self.tv_attendance = QtWidgets.QTableView(self.widget)
        self.tv_attendance.setAlternatingRowColors(True)
        self.tv_attendance.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tv_attendance.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tv_attendance.setWordWrap(False)
        self.tv_attendance.setObjectName("tv_attendance")
        self.tv_attendance.horizontalHeader().setDefaultSectionSize(200)
        self.verticalLayout_3.addWidget(self.tv_attendance)
        self.verticalLayout_2.addWidget(self.widget)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_4.setText(_translate("Form", "请输入查询条件："))
        self.pb_cj_att.setText(_translate("Form", "手动采集设备考勤数据"))
        self.pb_uploadAtt.setText(_translate("Form", "手动上传考勤数据到住建平台"))
        self.pb_query.setText(_translate("Form", "本地查询"))
        self.pb_allData.setText(_translate("Form", "全部数据"))
