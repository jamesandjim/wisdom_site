# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'collectImg.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(518, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 2, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.pb_takePhoto = QtWidgets.QPushButton(Dialog)
        self.pb_takePhoto.setObjectName("pb_takePhoto")
        self.verticalLayout.addWidget(self.pb_takePhoto)
        self.pb_accept = QtWidgets.QPushButton(Dialog)
        self.pb_accept.setEnabled(False)
        self.pb_accept.setObjectName("pb_accept")
        self.verticalLayout.addWidget(self.pb_accept)
        self.pb_esc = QtWidgets.QPushButton(Dialog)
        self.pb_esc.setObjectName("pb_esc")
        self.verticalLayout.addWidget(self.pb_esc)
        spacerItem1 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.lb_photo = QtWidgets.QLabel(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lb_photo.sizePolicy().hasHeightForWidth())
        self.lb_photo.setSizePolicy(sizePolicy)
        self.lb_photo.setMinimumSize(QtCore.QSize(500, 500))
        self.lb_photo.setMaximumSize(QtCore.QSize(500, 500))
        self.lb_photo.setText("")
        self.lb_photo.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lb_photo.setObjectName("lb_photo")
        self.verticalLayout.addWidget(self.lb_photo)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "拍照"))
        self.pb_takePhoto.setText(_translate("Dialog", "拍        照"))
        self.pb_accept.setText(_translate("Dialog", "保存照片退出"))
        self.pb_esc.setText(_translate("Dialog", "不拍照退出"))
