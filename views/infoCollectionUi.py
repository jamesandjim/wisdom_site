# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'infoCollectionUi.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_infoCollectionForm(object):
    def setupUi(self, infoCollectionForm):
        infoCollectionForm.setObjectName("infoCollectionForm")
        infoCollectionForm.setWindowModality(QtCore.Qt.WindowModal)
        infoCollectionForm.resize(1087, 831)
        infoCollectionForm.setStyleSheet("")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(infoCollectionForm)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.info_main = QtWidgets.QWidget(infoCollectionForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.info_main.sizePolicy().hasHeightForWidth())
        self.info_main.setSizePolicy(sizePolicy)
        self.info_main.setStyleSheet("QWidget #info_main{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius:5px;\n"
"}")
        self.info_main.setObjectName("info_main")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.info_main)
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.info_main)
        self.tabWidget.setStyleSheet("QTabWidget #tabWidget{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius:5px;\n"
"}")
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setIconSize(QtCore.QSize(20, 20))
        self.tabWidget.setElideMode(QtCore.Qt.ElideMiddle)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setStyleSheet("QWidget #tab{\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius:5px;\n"
"}")
        self.tab.setObjectName("tab")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_4.setContentsMargins(10, 20, 10, 20)
        self.verticalLayout_4.setSpacing(20)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.gb_base = QtWidgets.QGroupBox(self.tab)
        self.gb_base.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.gb_base.setObjectName("gb_base")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.gb_base)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.formLayout.setVerticalSpacing(15)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.gb_base)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.le_name = QtWidgets.QLineEdit(self.gb_base)
        self.le_name.setMinimumSize(QtCore.QSize(0, 0))
        self.le_name.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.le_name.setReadOnly(True)
        self.le_name.setObjectName("le_name")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.le_name)
        self.label_5 = QtWidgets.QLabel(self.gb_base)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.le_birthdate = QtWidgets.QLineEdit(self.gb_base)
        self.le_birthdate.setMinimumSize(QtCore.QSize(0, 0))
        self.le_birthdate.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.le_birthdate.setReadOnly(True)
        self.le_birthdate.setObjectName("le_birthdate")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.le_birthdate)
        self.label_6 = QtWidgets.QLabel(self.gb_base)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.le_idNum = QtWidgets.QLineEdit(self.gb_base)
        self.le_idNum.setMinimumSize(QtCore.QSize(0, 0))
        self.le_idNum.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.le_idNum.setReadOnly(True)
        self.le_idNum.setObjectName("le_idNum")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.le_idNum)
        self.label_7 = QtWidgets.QLabel(self.gb_base)
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.le_effectedDate = QtWidgets.QLineEdit(self.gb_base)
        self.le_effectedDate.setMinimumSize(QtCore.QSize(0, 0))
        self.le_effectedDate.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.le_effectedDate.setReadOnly(True)
        self.le_effectedDate.setObjectName("le_effectedDate")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.le_effectedDate)
        self.horizontalLayout_2.addLayout(self.formLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.formLayout_4 = QtWidgets.QFormLayout()
        self.formLayout_4.setVerticalSpacing(15)
        self.formLayout_4.setObjectName("formLayout_4")
        self.label_3 = QtWidgets.QLabel(self.gb_base)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.le_sex = QtWidgets.QLineEdit(self.gb_base)
        self.le_sex.setMinimumSize(QtCore.QSize(0, 0))
        self.le_sex.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.le_sex.setReadOnly(True)
        self.le_sex.setObjectName("le_sex")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.le_sex)
        self.label_4 = QtWidgets.QLabel(self.gb_base)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.le_nation = QtWidgets.QLineEdit(self.gb_base)
        self.le_nation.setMinimumSize(QtCore.QSize(0, 0))
        self.le_nation.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.le_nation.setReadOnly(True)
        self.le_nation.setObjectName("le_nation")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.le_nation)
        self.label_9 = QtWidgets.QLabel(self.gb_base)
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.le_issue = QtWidgets.QLineEdit(self.gb_base)
        self.le_issue.setMinimumSize(QtCore.QSize(0, 0))
        self.le_issue.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.le_issue.setReadOnly(True)
        self.le_issue.setObjectName("le_issue")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.le_issue)
        self.label_10 = QtWidgets.QLabel(self.gb_base)
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.formLayout_4.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.le_expiredDate = QtWidgets.QLineEdit(self.gb_base)
        self.le_expiredDate.setMinimumSize(QtCore.QSize(0, 0))
        self.le_expiredDate.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.le_expiredDate.setReadOnly(True)
        self.le_expiredDate.setObjectName("le_expiredDate")
        self.formLayout_4.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.le_expiredDate)
        self.horizontalLayout_2.addLayout(self.formLayout_4)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.formLayout_5 = QtWidgets.QFormLayout()
        self.formLayout_5.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.formLayout_5.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.formLayout_5.setContentsMargins(-1, 5, -1, -1)
        self.formLayout_5.setHorizontalSpacing(18)
        self.formLayout_5.setVerticalSpacing(6)
        self.formLayout_5.setObjectName("formLayout_5")
        self.label_8 = QtWidgets.QLabel(self.gb_base)
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.le_address = QtWidgets.QLineEdit(self.gb_base)
        self.le_address.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.le_address.setReadOnly(True)
        self.le_address.setObjectName("le_address")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.le_address)
        self.verticalLayout_5.addLayout(self.formLayout_5)
        self.horizontalLayout_4.addLayout(self.verticalLayout_5)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pb_cj = QtWidgets.QPushButton(self.gb_base)
        self.pb_cj.setEnabled(True)
        self.pb_cj.setFlat(False)
        self.pb_cj.setObjectName("pb_cj")
        self.verticalLayout.addWidget(self.pb_cj)
        self.pb_cj1 = QtWidgets.QPushButton(self.gb_base)
        self.pb_cj1.setObjectName("pb_cj1")
        self.verticalLayout.addWidget(self.pb_cj1)
        self.pb_camera1 = QtWidgets.QPushButton(self.gb_base)
        self.pb_camera1.setObjectName("pb_camera1")
        self.verticalLayout.addWidget(self.pb_camera1)
        self.pb_uploadPhoto = QtWidgets.QPushButton(self.gb_base)
        self.pb_uploadPhoto.setFlat(False)
        self.pb_uploadPhoto.setObjectName("pb_uploadPhoto")
        self.verticalLayout.addWidget(self.pb_uploadPhoto)
        self.pb_save_upload = QtWidgets.QPushButton(self.gb_base)
        self.pb_save_upload.setObjectName("pb_save_upload")
        self.verticalLayout.addWidget(self.pb_save_upload)
        self.pb_uploadPerson = QtWidgets.QPushButton(self.gb_base)
        self.pb_uploadPerson.setObjectName("pb_uploadPerson")
        self.verticalLayout.addWidget(self.pb_uploadPerson)
        self.pb_downloadPerson = QtWidgets.QPushButton(self.gb_base)
        self.pb_downloadPerson.setObjectName("pb_downloadPerson")
        self.verticalLayout.addWidget(self.pb_downloadPerson)
        self.pb_uploadtoDev = QtWidgets.QPushButton(self.gb_base)
        self.pb_uploadtoDev.setObjectName("pb_uploadtoDev")
        self.verticalLayout.addWidget(self.pb_uploadtoDev)
        self.pb_refresh_photo = QtWidgets.QPushButton(self.gb_base)
        self.pb_refresh_photo.setObjectName("pb_refresh_photo")
        self.verticalLayout.addWidget(self.pb_refresh_photo)
        self.horizontalLayout_4.addLayout(self.verticalLayout)
        self.verticalLayout_4.addWidget(self.gb_base)
        self.gb_zjxx = QtWidgets.QGroupBox(self.tab)
        self.gb_zjxx.setMinimumSize(QtCore.QSize(0, 160))
        self.gb_zjxx.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.gb_zjxx.setObjectName("gb_zjxx")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.gb_zjxx)
        self.horizontalLayout_3.setContentsMargins(5, 10, 5, 10)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setLabelAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.formLayout_2.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.formLayout_2.setHorizontalSpacing(10)
        self.formLayout_2.setVerticalSpacing(6)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label = QtWidgets.QLabel(self.gb_zjxx)
        self.label.setObjectName("label")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.le_userID = QtWidgets.QLineEdit(self.gb_zjxx)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_userID.sizePolicy().hasHeightForWidth())
        self.le_userID.setSizePolicy(sizePolicy)
        self.le_userID.setMinimumSize(QtCore.QSize(0, 0))
        self.le_userID.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.le_userID.setReadOnly(True)
        self.le_userID.setObjectName("le_userID")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.le_userID)
        self.label_13 = QtWidgets.QLabel(self.gb_zjxx)
        self.label_13.setObjectName("label_13")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_13)
        self.le_workSN = QtWidgets.QLineEdit(self.gb_zjxx)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_workSN.sizePolicy().hasHeightForWidth())
        self.le_workSN.setSizePolicy(sizePolicy)
        self.le_workSN.setMinimumSize(QtCore.QSize(0, 0))
        self.le_workSN.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.le_workSN.setReadOnly(True)
        self.le_workSN.setObjectName("le_workSN")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.le_workSN)
        self.label_14 = QtWidgets.QLabel(self.gb_zjxx)
        self.label_14.setObjectName("label_14")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_14)
        self.cb_department = QtWidgets.QComboBox(self.gb_zjxx)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cb_department.sizePolicy().hasHeightForWidth())
        self.cb_department.setSizePolicy(sizePolicy)
        self.cb_department.setMinimumSize(QtCore.QSize(0, 0))
        self.cb_department.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.cb_department.setStyleSheet("color: rgb(0, 170, 127);")
        self.cb_department.setFrame(True)
        self.cb_department.setObjectName("cb_department")
        self.cb_department.addItem("")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.cb_department)
        self.label_16 = QtWidgets.QLabel(self.gb_zjxx)
        self.label_16.setObjectName("label_16")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_16)
        self.checkbox_uploadYN = QtWidgets.QCheckBox(self.gb_zjxx)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkbox_uploadYN.sizePolicy().hasHeightForWidth())
        self.checkbox_uploadYN.setSizePolicy(sizePolicy)
        self.checkbox_uploadYN.setStyleSheet("color: rgb(0, 170, 127);")
        self.checkbox_uploadYN.setChecked(True)
        self.checkbox_uploadYN.setObjectName("checkbox_uploadYN")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.checkbox_uploadYN)
        self.horizontalLayout_3.addLayout(self.formLayout_2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setLabelAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.formLayout_3.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.formLayout_3.setHorizontalSpacing(10)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_11 = QtWidgets.QLabel(self.gb_zjxx)
        self.label_11.setObjectName("label_11")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.cb_RegType = QtWidgets.QComboBox(self.gb_zjxx)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cb_RegType.sizePolicy().hasHeightForWidth())
        self.cb_RegType.setSizePolicy(sizePolicy)
        self.cb_RegType.setMinimumSize(QtCore.QSize(0, 0))
        self.cb_RegType.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.cb_RegType.setStyleSheet("color: rgb(0, 170, 127);")
        self.cb_RegType.setObjectName("cb_RegType")
        self.cb_RegType.addItem("")
        self.cb_RegType.addItem("")
        self.cb_RegType.addItem("")
        self.cb_RegType.addItem("")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.cb_RegType)
        self.label_12 = QtWidgets.QLabel(self.gb_zjxx)
        self.label_12.setObjectName("label_12")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.cb_userType = QtWidgets.QComboBox(self.gb_zjxx)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cb_userType.sizePolicy().hasHeightForWidth())
        self.cb_userType.setSizePolicy(sizePolicy)
        self.cb_userType.setMinimumSize(QtCore.QSize(0, 0))
        self.cb_userType.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.cb_userType.setStyleSheet("color: rgb(0, 170, 127);")
        self.cb_userType.setObjectName("cb_userType")
        self.cb_userType.addItem("")
        self.cb_userType.addItem("")
        self.cb_userType.addItem("")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.cb_userType)
        self.label_17 = QtWidgets.QLabel(self.gb_zjxx)
        self.label_17.setObjectName("label_17")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_17)
        self.rb_personStatus1 = QtWidgets.QRadioButton(self.gb_zjxx)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rb_personStatus1.sizePolicy().hasHeightForWidth())
        self.rb_personStatus1.setSizePolicy(sizePolicy)
        self.rb_personStatus1.setStyleSheet("color: rgb(0, 170, 127);")
        self.rb_personStatus1.setChecked(True)
        self.rb_personStatus1.setObjectName("rb_personStatus1")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.rb_personStatus1)
        self.rb_personStatus2 = QtWidgets.QRadioButton(self.gb_zjxx)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rb_personStatus2.sizePolicy().hasHeightForWidth())
        self.rb_personStatus2.setSizePolicy(sizePolicy)
        self.rb_personStatus2.setStyleSheet("color: rgb(0, 170, 127);")
        self.rb_personStatus2.setObjectName("rb_personStatus2")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.rb_personStatus2)
        self.horizontalLayout_3.addLayout(self.formLayout_3)
        self.verticalLayout_4.addWidget(self.gb_zjxx)
        self.gb_photos = QtWidgets.QGroupBox(self.tab)
        self.gb_photos.setObjectName("gb_photos")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.gb_photos)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.lb_photo = QtWidgets.QLabel(self.gb_photos)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lb_photo.sizePolicy().hasHeightForWidth())
        self.lb_photo.setSizePolicy(sizePolicy)
        self.lb_photo.setMinimumSize(QtCore.QSize(200, 200))
        self.lb_photo.setMaximumSize(QtCore.QSize(200, 200))
        self.lb_photo.setText("")
        self.lb_photo.setScaledContents(False)
        self.lb_photo.setObjectName("lb_photo")
        self.horizontalLayout.addWidget(self.lb_photo)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.lb_photo2 = QtWidgets.QLabel(self.gb_photos)
        self.lb_photo2.setMinimumSize(QtCore.QSize(200, 200))
        self.lb_photo2.setMaximumSize(QtCore.QSize(200, 200))
        self.lb_photo2.setText("")
        self.lb_photo2.setObjectName("lb_photo2")
        self.horizontalLayout.addWidget(self.lb_photo2)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        self.lb_photo3 = QtWidgets.QLabel(self.gb_photos)
        self.lb_photo3.setMinimumSize(QtCore.QSize(200, 200))
        self.lb_photo3.setMaximumSize(QtCore.QSize(200, 200))
        self.lb_photo3.setText("")
        self.lb_photo3.setScaledContents(True)
        self.lb_photo3.setObjectName("lb_photo3")
        self.horizontalLayout.addWidget(self.lb_photo3)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.verticalLayout_4.addWidget(self.gb_photos)
        self.tabWidget.addTab(self.tab, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        self.verticalLayout_3.addWidget(self.info_main)

        self.retranslateUi(infoCollectionForm)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(infoCollectionForm)

    def retranslateUi(self, infoCollectionForm):
        _translate = QtCore.QCoreApplication.translate
        infoCollectionForm.setWindowTitle(_translate("infoCollectionForm", "Form"))
        self.gb_base.setTitle(_translate("infoCollectionForm", "人员基本信息"))
        self.label_2.setText(_translate("infoCollectionForm", "姓        名"))
        self.label_5.setText(_translate("infoCollectionForm", "出  生  日  期"))
        self.label_6.setText(_translate("infoCollectionForm", "身  份  证  号"))
        self.label_7.setText(_translate("infoCollectionForm", "证件有效期开始"))
        self.label_3.setText(_translate("infoCollectionForm", "性        别"))
        self.label_4.setText(_translate("infoCollectionForm", "民        族"))
        self.label_9.setText(_translate("infoCollectionForm", "发  证  机  关"))
        self.label_10.setText(_translate("infoCollectionForm", "证件有效期结束"))
        self.label_8.setText(_translate("infoCollectionForm", "住        址"))
        self.pb_cj.setText(_translate("infoCollectionForm", "读身份证信息（中控）"))
        self.pb_cj1.setText(_translate("infoCollectionForm", "读身份证信息"))
        self.pb_camera1.setText(_translate("infoCollectionForm", "从摄像头拍照"))
        self.pb_uploadPhoto.setText(_translate("infoCollectionForm", "使用电脑中的照片"))
        self.pb_save_upload.setText(_translate("infoCollectionForm", "保存数据到本地"))
        self.pb_uploadPerson.setText(_translate("infoCollectionForm", "上传至住建平台"))
        self.pb_downloadPerson.setText(_translate("infoCollectionForm", "从平台下载人员信息"))
        self.pb_uploadtoDev.setText(_translate("infoCollectionForm", "上传至考勤设备"))
        self.pb_refresh_photo.setText(_translate("infoCollectionForm", "刷新人脸照片"))
        self.gb_zjxx.setTitle(_translate("infoCollectionForm", "住建平台信息"))
        self.label.setText(_translate("infoCollectionForm", "统一编号"))
        self.label_13.setText(_translate("infoCollectionForm", "用户工号"))
        self.label_14.setText(_translate("infoCollectionForm", "所属班组"))
        self.cb_department.setItemText(0, _translate("infoCollectionForm", "请选择人员所属班组"))
        self.label_16.setText(_translate("infoCollectionForm", "是否上传"))
        self.checkbox_uploadYN.setText(_translate("infoCollectionForm", "人员信息是否上传至住建平台"))
        self.label_11.setText(_translate("infoCollectionForm", "注册类别"))
        self.cb_RegType.setItemText(0, _translate("infoCollectionForm", "人脸采集"))
        self.cb_RegType.setItemText(1, _translate("infoCollectionForm", "刷卡采集"))
        self.cb_RegType.setItemText(2, _translate("infoCollectionForm", "指纹采集"))
        self.cb_RegType.setItemText(3, _translate("infoCollectionForm", "其他采集"))
        self.label_12.setText(_translate("infoCollectionForm", "注册人员类型"))
        self.cb_userType.setItemText(0, _translate("infoCollectionForm", "劳务人员"))
        self.cb_userType.setItemText(1, _translate("infoCollectionForm", "岗位人员"))
        self.cb_userType.setItemText(2, _translate("infoCollectionForm", "其他人员"))
        self.label_17.setText(_translate("infoCollectionForm", "人员状态"))
        self.rb_personStatus1.setText(_translate("infoCollectionForm", "正常"))
        self.rb_personStatus2.setText(_translate("infoCollectionForm", "冻结"))
        self.gb_photos.setTitle(_translate("infoCollectionForm", "人像信息"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("infoCollectionForm", "人员信息采集"))
