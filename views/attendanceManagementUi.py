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
        Form.resize(1065, 738)
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
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
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
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.dateTimeEdit_begin = QtWidgets.QDateTimeEdit(self.widget)
        self.dateTimeEdit_begin.setCurrentSection(QtWidgets.QDateTimeEdit.DaySection)
        self.dateTimeEdit_begin.setCalendarPopup(True)
        self.dateTimeEdit_begin.setObjectName("dateTimeEdit_begin")
        self.horizontalLayout_2.addWidget(self.dateTimeEdit_begin)
        self.dateTimeEdit_end = QtWidgets.QDateTimeEdit(self.widget)
        self.dateTimeEdit_end.setCurrentSection(QtWidgets.QDateTimeEdit.DaySection)
        self.dateTimeEdit_end.setCalendarPopup(True)
        self.dateTimeEdit_end.setObjectName("dateTimeEdit_end")
        self.horizontalLayout_2.addWidget(self.dateTimeEdit_end)
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
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tv_attendance = QtWidgets.QTableView(self.widget)
        self.tv_attendance.setAlternatingRowColors(True)
        self.tv_attendance.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tv_attendance.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tv_attendance.setWordWrap(False)
        self.tv_attendance.setObjectName("tv_attendance")
        self.tv_attendance.horizontalHeader().setDefaultSectionSize(200)
        self.tv_attendance.horizontalHeader().setMinimumSectionSize(40)
        self.horizontalLayout.addWidget(self.tv_attendance)
        self.label_image = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_image.sizePolicy().hasHeightForWidth())
        self.label_image.setSizePolicy(sizePolicy)
        self.label_image.setMinimumSize(QtCore.QSize(300, 500))
        self.label_image.setMaximumSize(QtCore.QSize(300, 400))
        self.label_image.setText("")
        self.label_image.setAlignment(QtCore.Qt.AlignCenter)
        self.label_image.setObjectName("label_image")
        self.horizontalLayout.addWidget(self.label_image)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addWidget(self.widget)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_4.setText(_translate("Form", "请输入查询条件："))
        self.le_queryPara.setPlaceholderText(_translate("Form", "请输入人员名称"))
        self.label.setText(_translate("Form", "起止日期："))
        self.dateTimeEdit_begin.setDisplayFormat(_translate("Form", "yyyy/MM/dd HH:mm:ss"))
        self.dateTimeEdit_end.setDisplayFormat(_translate("Form", "yyyy/MM/dd HH:mm:ss"))
        self.pb_cj_att.setText(_translate("Form", "手动采集设备考勤数据"))
        self.pb_uploadAtt.setText(_translate("Form", "手动上传考勤数据到住建平台"))
        self.pb_query.setText(_translate("Form", "本地查询"))
        self.pb_allData.setText(_translate("Form", "全部数据"))
