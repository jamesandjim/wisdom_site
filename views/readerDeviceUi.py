# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'readerDeviceUi.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.WindowModal)
        Form.resize(809, 628)
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
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout.setContentsMargins(-1, 10, -1, -1)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.le_deviceId = QtWidgets.QLineEdit(self.widget)
        self.le_deviceId.setObjectName("le_deviceId")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.le_deviceId)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.le_deviceName = QtWidgets.QLineEdit(self.widget)
        self.le_deviceName.setObjectName("le_deviceName")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.le_deviceName)
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.cb_deviceType = QtWidgets.QComboBox(self.widget)
        self.cb_deviceType.setObjectName("cb_deviceType")
        self.cb_deviceType.addItem("")
        self.cb_deviceType.addItem("")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.cb_deviceType)
        self.label_11 = QtWidgets.QLabel(self.widget)
        self.label_11.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_11.setObjectName("label_11")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.le_deviceSN = QtWidgets.QLineEdit(self.widget)
        self.le_deviceSN.setObjectName("le_deviceSN")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.le_deviceSN)
        self.label_12 = QtWidgets.QLabel(self.widget)
        self.label_12.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_12.setObjectName("label_12")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.le_key = QtWidgets.QLineEdit(self.widget)
        self.le_key.setObjectName("le_key")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.le_key)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.le_Memo = QtWidgets.QLineEdit(self.widget)
        self.le_Memo.setObjectName("le_Memo")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.le_Memo)
        self.radioButton_stop = QtWidgets.QRadioButton(self.widget)
        self.radioButton_stop.setObjectName("radioButton_stop")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.radioButton_stop)
        self.radioButton_nomal = QtWidgets.QRadioButton(self.widget)
        self.radioButton_nomal.setChecked(True)
        self.radioButton_nomal.setObjectName("radioButton_nomal")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.radioButton_nomal)
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.horizontalLayout.addLayout(self.formLayout)
        spacerItem = QtWidgets.QSpacerItem(15, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pb_add = QtWidgets.QPushButton(self.widget)
        self.pb_add.setObjectName("pb_add")
        self.verticalLayout.addWidget(self.pb_add)
        self.pb_update = QtWidgets.QPushButton(self.widget)
        self.pb_update.setObjectName("pb_update")
        self.verticalLayout.addWidget(self.pb_update)
        self.pb_del = QtWidgets.QPushButton(self.widget)
        self.pb_del.setObjectName("pb_del")
        self.verticalLayout.addWidget(self.pb_del)
        self.pb_save = QtWidgets.QPushButton(self.widget)
        self.pb_save.setObjectName("pb_save")
        self.verticalLayout.addWidget(self.pb_save)
        self.pb_esc = QtWidgets.QPushButton(self.widget)
        self.pb_esc.setObjectName("pb_esc")
        self.verticalLayout.addWidget(self.pb_esc)
        self.horizontalLayout.addLayout(self.verticalLayout)
        spacerItem2 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        spacerItem3 = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_3.addItem(spacerItem3)
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
        self.pb_query = QtWidgets.QPushButton(self.widget)
        self.pb_query.setObjectName("pb_query")
        self.horizontalLayout_2.addWidget(self.pb_query)
        self.pb_allData = QtWidgets.QPushButton(self.widget)
        self.pb_allData.setObjectName("pb_allData")
        self.horizontalLayout_2.addWidget(self.pb_allData)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.tv_device = QtWidgets.QTableView(self.widget)
        self.tv_device.setAlternatingRowColors(True)
        self.tv_device.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tv_device.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tv_device.setWordWrap(False)
        self.tv_device.setObjectName("tv_device")
        self.tv_device.horizontalHeader().setDefaultSectionSize(200)
        self.verticalLayout_3.addWidget(self.tv_device)
        self.verticalLayout_2.addWidget(self.widget)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "设备编号"))
        self.label_2.setText(_translate("Form", "设备名称"))
        self.label_5.setText(_translate("Form", "设备类型"))
        self.cb_deviceType.setItemText(0, _translate("Form", "KL803"))
        self.cb_deviceType.setItemText(1, _translate("Form", "ZK100"))
        self.label_11.setText(_translate("Form", "设备SN"))
        self.label_12.setText(_translate("Form", "设备key"))
        self.label_3.setText(_translate("Form", "说明"))
        self.radioButton_stop.setText(_translate("Form", "停止使用"))
        self.radioButton_nomal.setText(_translate("Form", "正常使用"))
        self.label_7.setText(_translate("Form", "是否启用"))
        self.pb_add.setText(_translate("Form", "增加"))
        self.pb_update.setText(_translate("Form", "修改"))
        self.pb_del.setText(_translate("Form", "删除"))
        self.pb_save.setText(_translate("Form", "保存"))
        self.pb_esc.setText(_translate("Form", "取消"))
        self.label_4.setText(_translate("Form", "请输入查询条件："))
        self.pb_query.setText(_translate("Form", "查  询"))
        self.pb_allData.setText(_translate("Form", "全部数据"))
