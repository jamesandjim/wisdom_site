# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'info_collection.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_info_collect_Form(object):
    def setupUi(self, info_collect_Form):
        info_collect_Form.setObjectName("info_collect_Form")
        info_collect_Form.resize(825, 679)
        info_collect_Form.setStyleSheet("border-color: rgb(255, 255, 255);\n"
"")
        self.verticalLayout = QtWidgets.QVBoxLayout(info_collect_Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.info_main = QtWidgets.QWidget(info_collect_Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.info_main.sizePolicy().hasHeightForWidth())
        self.info_main.setSizePolicy(sizePolicy)
        self.info_main.setStyleSheet("border-color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        self.info_main.setObjectName("info_main")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.info_main)
        self.verticalLayout_2.setContentsMargins(5, 20, 5, 5)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(self.info_main)
        self.groupBox.setMinimumSize(QtCore.QSize(0, 200))
        self.groupBox.setStyleSheet("QGroupBox#groupBox {\n"
"    \n"
"    background-color: rgb(255, 255, 255);\n"
"    gridline-color: rgb(13, 144, 11);\n"
"    \n"
"}")
        self.groupBox.setFlat(False)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setContentsMargins(-1, 20, -1, -1)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.info_main)
        self.groupBox_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setContentsMargins(-1, 20, -1, -1)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tableView = QtWidgets.QTableView(self.groupBox_2)
        self.tableView.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableView.setGridStyle(QtCore.Qt.DotLine)
        self.tableView.setObjectName("tableView")
        self.verticalLayout_3.addWidget(self.tableView)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        self.verticalLayout.addWidget(self.info_main)

        self.retranslateUi(info_collect_Form)
        QtCore.QMetaObject.connectSlotsByName(info_collect_Form)

    def retranslateUi(self, info_collect_Form):
        _translate = QtCore.QCoreApplication.translate
        info_collect_Form.setWindowTitle(_translate("info_collect_Form", "Form"))
        self.groupBox.setTitle(_translate("info_collect_Form", "查询与操作"))
        self.label.setText(_translate("info_collect_Form", "文本内容请输入："))
        self.pushButton.setText(_translate("info_collect_Form", "PushButton"))
        self.groupBox_2.setTitle(_translate("info_collect_Form", "人员信息列表"))
