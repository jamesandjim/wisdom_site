# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindows.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1102, 662)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setAutoFillBackground(False)
        Form.setStyleSheet("background-color: rgb(229, 225, 222);")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setSpacing(1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.header = QtWidgets.QWidget(Form)
        self.header.setEnabled(True)
        self.header.setMinimumSize(QtCore.QSize(0, 80))
        self.header.setMaximumSize(QtCore.QSize(16777215, 80))
        self.header.setAutoFillBackground(False)
        self.header.setStyleSheet("background-color: rgb(57, 112, 254);\n"
"\n"
"")
        self.header.setObjectName("header")
        self.layoutWidget = QtWidgets.QWidget(self.header)
        self.layoutWidget.setGeometry(QtCore.QRect(180, 0, 552, 82))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setMinimumSize(QtCore.QSize(200, 0))
        self.label.setMaximumSize(QtCore.QSize(200, 16777215))
        self.label.setStyleSheet("background-color: rgb(57, 112, 254);")
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton.setMaximumSize(QtCore.QSize(80, 80))
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ico/resource/ico/1.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(70, 70))
        self.pushButton.setCheckable(True)
        self.pushButton.setFlat(True)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_4.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_2.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_2.setMaximumSize(QtCore.QSize(80, 80))
        self.pushButton_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/ico/resource/ico/2.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QtCore.QSize(70, 70))
        self.pushButton_2.setCheckable(True)
        self.pushButton_2.setFlat(True)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_4.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_3.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_3.setMaximumSize(QtCore.QSize(80, 80))
        self.pushButton_3.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/ico/resource/ico/3.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QtCore.QSize(70, 70))
        self.pushButton_3.setCheckable(True)
        self.pushButton_3.setFlat(True)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_4.addWidget(self.pushButton_3)
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.pushButton_8 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_8.setMinimumSize(QtCore.QSize(80, 80))
        self.pushButton_8.setMaximumSize(QtCore.QSize(80, 80))
        self.pushButton_8.setStyleSheet("")
        self.pushButton_8.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/ico/resource/ico/exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_8.setIcon(icon3)
        self.pushButton_8.setIconSize(QtCore.QSize(70, 70))
        self.pushButton_8.setCheckable(True)
        self.pushButton_8.setFlat(True)
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout_4.addWidget(self.pushButton_8)
        self.horizontalLayout.addWidget(self.header)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.widget_2 = QtWidgets.QWidget(Form)
        self.widget_2.setMinimumSize(QtCore.QSize(300, 0))
        self.widget_2.setMaximumSize(QtCore.QSize(300, 16777215))
        self.widget_2.setSizeIncrement(QtCore.QSize(300, 0))
        self.widget_2.setStyleSheet("background-color: rgb(249, 249, 249);\n"
"border-left-color: rgb(121, 121, 121);\n"
"border-radius:5px;")
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tree_menu = QtWidgets.QTreeWidget(self.widget_2)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI Light")
        font.setPointSize(10)
        self.tree_menu.setFont(font)
        self.tree_menu.setAnimated(True)
        self.tree_menu.setObjectName("tree_menu")
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.tree_menu.headerItem().setFont(0, font)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/ico/resource/ico/main.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tree_menu.headerItem().setIcon(0, icon4)
        item_0 = QtWidgets.QTreeWidgetItem(self.tree_menu)
        item_0 = QtWidgets.QTreeWidgetItem(self.tree_menu)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(10)
        item_0.setFont(0, font)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/ico/resource/ico/2.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon5.addPixmap(QtGui.QPixmap(":/ico/resource/ico/1.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        item_0.setIcon(0, icon5)
        item_0.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsDropEnabled|QtCore.Qt.ItemIsUserCheckable|QtCore.Qt.ItemIsEnabled)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.tree_menu)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.tree_menu)
        self.verticalLayout_2.addWidget(self.tree_menu)
        self.horizontalLayout_2.addWidget(self.widget_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(5, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.main_content = QtWidgets.QWidget(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_content.sizePolicy().hasHeightForWidth())
        self.main_content.setSizePolicy(sizePolicy)
        self.main_content.setMinimumSize(QtCore.QSize(500, 0))
        self.main_content.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:5px;")
        self.main_content.setObjectName("main_content")
        self.verticalLayout_3.addWidget(self.main_content)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setMinimumSize(QtCore.QSize(0, 25))
        self.label_2.setMaximumSize(QtCore.QSize(16777215, 25))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "SDTI智慧工地系统"))
        self.tree_menu.headerItem().setText(0, _translate("Form", "智慧工地系统"))
        __sortingEnabled = self.tree_menu.isSortingEnabled()
        self.tree_menu.setSortingEnabled(False)
        self.tree_menu.topLevelItem(0).setText(0, _translate("Form", "系统设置"))
        self.tree_menu.topLevelItem(1).setText(0, _translate("Form", "日常操作"))
        self.tree_menu.topLevelItem(1).child(0).setText(0, _translate("Form", "人员信息采集"))
        self.tree_menu.topLevelItem(1).child(1).setText(0, _translate("Form", "人员信息查询"))
        self.tree_menu.topLevelItem(1).child(2).setText(0, _translate("Form", "人员考勤数据管理"))
        self.tree_menu.topLevelItem(2).setText(0, _translate("Form", "设备管理"))
        self.tree_menu.topLevelItem(2).child(0).setText(0, _translate("Form", "采集设备"))
        self.tree_menu.topLevelItem(2).child(1).setText(0, _translate("Form", "考勤设备"))
        self.tree_menu.topLevelItem(2).child(2).setText(0, _translate("Form", "显示屏设备"))
        self.tree_menu.topLevelItem(3).setText(0, _translate("Form", "操作员管理"))
        self.tree_menu.setSortingEnabled(__sortingEnabled)
        self.label_2.setText(_translate("Form", "成都丰盛时代科技有限公司 版权所有"))
import resource_rc
