# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lcdMonitorUi.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1434, 820)
        Form.setStyleSheet("background-color: rgb(51, 13, 134);")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_header = QtWidgets.QGroupBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.groupBox_header.sizePolicy().hasHeightForWidth())
        self.groupBox_header.setSizePolicy(sizePolicy)
        self.groupBox_header.setStyleSheet("QGroupBox#groupBox_header\n"
"{\n"
"   border:0px\n"
"}")
        self.groupBox_header.setTitle("")
        self.groupBox_header.setObjectName("groupBox_header")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_header)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_title = QtWidgets.QLabel(self.groupBox_header)
        self.label_title.setStyleSheet("font: 75 36pt \"微软雅黑\";\n"
"color: rgb(255, 255, 255);")
        self.label_title.setObjectName("label_title")
        self.horizontalLayout.addWidget(self.label_title)
        self.lcdNumber_date = QtWidgets.QLCDNumber(self.groupBox_header)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcdNumber_date.sizePolicy().hasHeightForWidth())
        self.lcdNumber_date.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(28)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.lcdNumber_date.setFont(font)
        self.lcdNumber_date.setStyleSheet("font: 75 28pt \"微软雅黑\";")
        self.lcdNumber_date.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lcdNumber_date.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lcdNumber_date.setLineWidth(0)
        self.lcdNumber_date.setDigitCount(10)
        self.lcdNumber_date.setSegmentStyle(QtWidgets.QLCDNumber.Outline)
        self.lcdNumber_date.setProperty("value", 20191212.0)
        self.lcdNumber_date.setProperty("intValue", 20191212)
        self.lcdNumber_date.setObjectName("lcdNumber_date")
        self.horizontalLayout.addWidget(self.lcdNumber_date)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_4 = QtWidgets.QLabel(self.groupBox_header)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMinimumSize(QtCore.QSize(200, 200))
        self.label_4.setMaximumSize(QtCore.QSize(200, 200))
        self.label_4.setStyleSheet("image: url(:/ico/resource/ico/阴转晴.png);")
        self.label_4.setLineWidth(0)
        self.label_4.setText("")
        self.label_4.setScaledContents(False)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.widget = QtWidgets.QWidget(self.groupBox_header)
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_xq = QtWidgets.QLabel(self.widget)
        self.label_xq.setStyleSheet("font: 20pt \"方正姚体\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.label_xq.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_xq.setObjectName("label_xq")
        self.verticalLayout_2.addWidget(self.label_xq)
        self.label_tq = QtWidgets.QLabel(self.widget)
        self.label_tq.setStyleSheet("font: 20pt \"方正姚体\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.label_tq.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_tq.setObjectName("label_tq")
        self.verticalLayout_2.addWidget(self.label_tq)
        self.label_wd = QtWidgets.QLabel(self.widget)
        self.label_wd.setStyleSheet("font: 20pt \"方正姚体\";\n"
"color: rgb(255, 255, 255);\n"
"")
        self.label_wd.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_wd.setObjectName("label_wd")
        self.verticalLayout_2.addWidget(self.label_wd)
        self.label_fengli = QtWidgets.QLabel(self.widget)
        self.label_fengli.setStyleSheet("font: 20pt \"方正姚体\";\n"
"color: rgb(255, 255, 255);")
        self.label_fengli.setText("")
        self.label_fengli.setObjectName("label_fengli")
        self.verticalLayout_2.addWidget(self.label_fengli)
        self.horizontalLayout.addWidget(self.widget)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addWidget(self.groupBox_header)
        self.groupBox_center = QtWidgets.QGroupBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(7)
        sizePolicy.setHeightForWidth(self.groupBox_center.sizePolicy().hasHeightForWidth())
        self.groupBox_center.setSizePolicy(sizePolicy)
        self.groupBox_center.setStyleSheet("QGroupBox#groupBox_center \n"
"{\n"
"   border:0px\n"
"}")
        self.groupBox_center.setTitle("")
        self.groupBox_center.setObjectName("groupBox_center")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox_center)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(15)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox_center)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy)
        self.groupBox_4.setStyleSheet("QGroupBox#groupBox_4\n"
"{\n"
"   border:0px\n"
"}")
        self.groupBox_4.setTitle("")
        self.groupBox_4.setFlat(False)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_5.setSpacing(10)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.groupBox_photo = QtWidgets.QGroupBox(self.groupBox_4)
        self.groupBox_photo.setStyleSheet("QGroupBox#groupBox_photo\n"
"\n"
"{\n"
"   border:1px solid #11045e;\n"
"   border-radius:10px;\n"
"   border-style:groove;\n"
"   float:left;\n"
"        \n"
"}")
        self.groupBox_photo.setTitle("")
        self.groupBox_photo.setFlat(False)
        self.groupBox_photo.setObjectName("groupBox_photo")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox_photo)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_idphoto = QtWidgets.QLabel(self.groupBox_photo)
        self.label_idphoto.setStyleSheet("image: url(:/img/resource/img/ymg.jpg);")
        self.label_idphoto.setText("")
        self.label_idphoto.setObjectName("label_idphoto")
        self.horizontalLayout_3.addWidget(self.label_idphoto)
        self.label_photo = QtWidgets.QLabel(self.groupBox_photo)
        self.label_photo.setStyleSheet("image: url(:/img/resource/img/420124197802025936.jpg);")
        self.label_photo.setText("")
        self.label_photo.setScaledContents(True)
        self.label_photo.setObjectName("label_photo")
        self.horizontalLayout_3.addWidget(self.label_photo)
        self.verticalLayout_5.addWidget(self.groupBox_photo)
        self.groupBox_info = QtWidgets.QGroupBox(self.groupBox_4)
        self.groupBox_info.setStyleSheet("QGroupBox#groupBox_info\n"
"\n"
"{\n"
"   border:1px solid #11045e;\n"
"   border-radius:10px;\n"
"   border-style:groove;\n"
"   float:left;\n"
"        \n"
"}")
        self.groupBox_info.setTitle("")
        self.groupBox_info.setObjectName("groupBox_info")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.groupBox_info)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_about = QtWidgets.QLabel(self.groupBox_info)
        self.label_about.setTextFormat(QtCore.Qt.RichText)
        self.label_about.setWordWrap(True)
        self.label_about.setObjectName("label_about")
        self.verticalLayout_12.addWidget(self.label_about)
        self.verticalLayout_5.addWidget(self.groupBox_info)
        self.horizontalLayout_2.addWidget(self.groupBox_4)
        self.groupBox_5 = QtWidgets.QGroupBox(self.groupBox_center)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_5.sizePolicy().hasHeightForWidth())
        self.groupBox_5.setSizePolicy(sizePolicy)
        self.groupBox_5.setStyleSheet("QGroupBox#groupBox_5\n"
"{\n"
"   border:0px\n"
"}")
        self.groupBox_5.setTitle("")
        self.groupBox_5.setObjectName("groupBox_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_3.setContentsMargins(-1, 5, -1, -1)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox_bzTotal = QtWidgets.QGroupBox(self.groupBox_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.groupBox_bzTotal.sizePolicy().hasHeightForWidth())
        self.groupBox_bzTotal.setSizePolicy(sizePolicy)
        self.groupBox_bzTotal.setStyleSheet("QGroupBox#groupBox_bzTotal\n"
"\n"
"{\n"
"   border:1px solid #11045e;\n"
"   border-radius:10px;\n"
"   border-style:solid;\n"
"   float:left;\n"
"        \n"
"}")
        self.groupBox_bzTotal.setTitle("")
        self.groupBox_bzTotal.setFlat(True)
        self.groupBox_bzTotal.setObjectName("groupBox_bzTotal")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.groupBox_bzTotal)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_6 = QtWidgets.QLabel(self.groupBox_bzTotal)
        self.label_6.setStyleSheet("\n"
"background-color:#11045e;\n"
"font: 75 28pt \"微软雅黑\";\n"
"color: white;\n"
"")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_6.addWidget(self.label_6)
        self.lcdNumber_all = QtWidgets.QLCDNumber(self.groupBox_bzTotal)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcdNumber_all.sizePolicy().hasHeightForWidth())
        self.lcdNumber_all.setSizePolicy(sizePolicy)
        self.lcdNumber_all.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.lcdNumber_all.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lcdNumber_all.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lcdNumber_all.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lcdNumber_all.setLineWidth(0)
        self.lcdNumber_all.setMidLineWidth(0)
        self.lcdNumber_all.setSmallDecimalPoint(False)
        self.lcdNumber_all.setDigitCount(5)
        self.lcdNumber_all.setSegmentStyle(QtWidgets.QLCDNumber.Outline)
        self.lcdNumber_all.setProperty("intValue", 1)
        self.lcdNumber_all.setObjectName("lcdNumber_all")
        self.verticalLayout_6.addWidget(self.lcdNumber_all)
        self.verticalLayout_3.addWidget(self.groupBox_bzTotal)
        self.groupBox_bzDetail = QtWidgets.QGroupBox(self.groupBox_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.groupBox_bzDetail.sizePolicy().hasHeightForWidth())
        self.groupBox_bzDetail.setSizePolicy(sizePolicy)
        self.groupBox_bzDetail.setStyleSheet("QGroupBox#groupBox_bzDetail\n"
"\n"
"{\n"
"   border:1px solid #11045e;\n"
"   border-radius:10px;\n"
"   border-style:groove;\n"
"   float:left;\n"
"        \n"
"}")
        self.groupBox_bzDetail.setTitle("")
        self.groupBox_bzDetail.setObjectName("groupBox_bzDetail")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.groupBox_bzDetail)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_10 = QtWidgets.QLabel(self.groupBox_bzDetail)
        self.label_10.setStyleSheet("background-color:#11045e;\n"
"font: 75 28pt \"微软雅黑\";\n"
"color: white;\n"
"border-radius:10px,10px;")
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_7.addWidget(self.label_10)
        self.groupBox_bz = QtWidgets.QGroupBox(self.groupBox_bzDetail)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.groupBox_bz.sizePolicy().hasHeightForWidth())
        self.groupBox_bz.setSizePolicy(sizePolicy)
        self.groupBox_bz.setStyleSheet("QGroupBox#groupBox_bz\n"
"{\n"
"   border:0px\n"
"}")
        self.groupBox_bz.setTitle("")
        self.groupBox_bz.setObjectName("groupBox_bz")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.groupBox_bz)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.flayout_bz = QtWidgets.QFormLayout()
        self.flayout_bz.setLabelAlignment(QtCore.Qt.AlignCenter)
        self.flayout_bz.setObjectName("flayout_bz")
        self.verticalLayout_11.addLayout(self.flayout_bz)
        self.verticalLayout_7.addWidget(self.groupBox_bz)
        self.verticalLayout_3.addWidget(self.groupBox_bzDetail)
        self.horizontalLayout_2.addWidget(self.groupBox_5)
        self.groupBox_6 = QtWidgets.QGroupBox(self.groupBox_center)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_6.sizePolicy().hasHeightForWidth())
        self.groupBox_6.setSizePolicy(sizePolicy)
        self.groupBox_6.setStyleSheet("QGroupBox#groupBox_6\n"
"{\n"
"   border:0px\n"
"}")
        self.groupBox_6.setTitle("")
        self.groupBox_6.setObjectName("groupBox_6")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_6)
        self.verticalLayout_4.setSpacing(10)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.groupBox_time = QtWidgets.QGroupBox(self.groupBox_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.groupBox_time.sizePolicy().hasHeightForWidth())
        self.groupBox_time.setSizePolicy(sizePolicy)
        self.groupBox_time.setStyleSheet("QGroupBox#groupBox_time\n"
"\n"
"{\n"
"   border:1px solid #11045e;\n"
"   border-radius:10px;\n"
"   border-style:groove;\n"
"   float:left;\n"
"        \n"
"}")
        self.groupBox_time.setTitle("")
        self.groupBox_time.setObjectName("groupBox_time")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.groupBox_time)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_time = QtWidgets.QLabel(self.groupBox_time)
        self.label_time.setStyleSheet("background-color:#11045e;\n"
"font: 75 28pt \"微软雅黑\";\n"
"color: white;\n"
"border-radius:10px,10px;")
        self.label_time.setAlignment(QtCore.Qt.AlignCenter)
        self.label_time.setObjectName("label_time")
        self.verticalLayout_8.addWidget(self.label_time)
        self.label_12 = QtWidgets.QLabel(self.groupBox_time)
        self.label_12.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 18pt \"方正姚体\";\n"
"")
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_8.addWidget(self.label_12)
        self.label_7 = QtWidgets.QLabel(self.groupBox_time)
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 18pt \"方正姚体\";\n"
"")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_8.addWidget(self.label_7)
        self.label_11 = QtWidgets.QLabel(self.groupBox_time)
        self.label_11.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 18pt \"方正姚体\";\n"
"")
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_8.addWidget(self.label_11)
        self.verticalLayout_4.addWidget(self.groupBox_time)
        self.groupBox_shift = QtWidgets.QGroupBox(self.groupBox_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.groupBox_shift.sizePolicy().hasHeightForWidth())
        self.groupBox_shift.setSizePolicy(sizePolicy)
        self.groupBox_shift.setStyleSheet("QGroupBox#groupBox_shift\n"
"{\n"
"   border:0px\n"
"}")
        self.groupBox_shift.setTitle("")
        self.groupBox_shift.setObjectName("groupBox_shift")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.groupBox_shift)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(5)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.groupBox_shift1 = QtWidgets.QGroupBox(self.groupBox_shift)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.groupBox_shift1.sizePolicy().hasHeightForWidth())
        self.groupBox_shift1.setSizePolicy(sizePolicy)
        self.groupBox_shift1.setStyleSheet("QGroupBox#groupBox_shift1\n"
"\n"
"{\n"
"   border:1px solid #11045e;\n"
"   border-radius:10px;\n"
"   border-style:groove;\n"
"   float:left;\n"
"        \n"
"}")
        self.groupBox_shift1.setTitle("")
        self.groupBox_shift1.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_shift1.setObjectName("groupBox_shift1")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.groupBox_shift1)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_14 = QtWidgets.QLabel(self.groupBox_shift1)
        self.label_14.setStyleSheet("background-color:#11045e;\n"
"font: 75 28pt \"微软雅黑\";\n"
"color: white;\n"
"border-radius:10px,10px;")
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_9.addWidget(self.label_14)
        self.groupBox_l = QtWidgets.QGroupBox(self.groupBox_shift1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.groupBox_l.sizePolicy().hasHeightForWidth())
        self.groupBox_l.setSizePolicy(sizePolicy)
        self.groupBox_l.setStyleSheet("QGroupBox#groupBox_l\n"
"{\n"
"   border:0px\n"
"}")
        self.groupBox_l.setTitle("")
        self.groupBox_l.setObjectName("groupBox_l")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.groupBox_l)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.listWidget_l = QtWidgets.QListWidget(self.groupBox_l)
        self.listWidget_l.setStyleSheet("QListWidget#listWidget_l\n"
"{\n"
"   border:0px\n"
"}")
        self.listWidget_l.setLineWidth(0)
        self.listWidget_l.setViewMode(QtWidgets.QListView.IconMode)
        self.listWidget_l.setObjectName("listWidget_l")
        self.verticalLayout_13.addWidget(self.listWidget_l)
        self.verticalLayout_9.addWidget(self.groupBox_l)
        self.horizontalLayout_5.addWidget(self.groupBox_shift1)
        self.groupBox_shift2 = QtWidgets.QGroupBox(self.groupBox_shift)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.groupBox_shift2.sizePolicy().hasHeightForWidth())
        self.groupBox_shift2.setSizePolicy(sizePolicy)
        self.groupBox_shift2.setStyleSheet("QGroupBox#groupBox_shift2\n"
"\n"
"{\n"
"   border:1px solid #11045e;\n"
"   border-radius:10px;\n"
"   border-style:groove;\n"
"   float:left;\n"
"        \n"
"}")
        self.groupBox_shift2.setTitle("")
        self.groupBox_shift2.setObjectName("groupBox_shift2")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.groupBox_shift2)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.label_15 = QtWidgets.QLabel(self.groupBox_shift2)
        self.label_15.setStyleSheet("background-color:#11045e;\n"
"font: 75 28pt \"微软雅黑\";\n"
"color: white;\n"
"border-radius:10px,10px;")
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setObjectName("label_15")
        self.verticalLayout_10.addWidget(self.label_15)
        self.groupBox_r = QtWidgets.QGroupBox(self.groupBox_shift2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.groupBox_r.sizePolicy().hasHeightForWidth())
        self.groupBox_r.setSizePolicy(sizePolicy)
        self.groupBox_r.setStyleSheet("QGroupBox#groupBox_r\n"
"{\n"
"   border:0px\n"
"}")
        self.groupBox_r.setTitle("")
        self.groupBox_r.setObjectName("groupBox_r")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.groupBox_r)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.listWidget_r = QtWidgets.QListWidget(self.groupBox_r)
        self.listWidget_r.setStyleSheet("QListWidget#listWidget_r\n"
"{\n"
"   border:0px\n"
"}")
        self.listWidget_r.setObjectName("listWidget_r")
        self.verticalLayout_14.addWidget(self.listWidget_r)
        self.verticalLayout_10.addWidget(self.groupBox_r)
        self.horizontalLayout_5.addWidget(self.groupBox_shift2)
        self.verticalLayout_4.addWidget(self.groupBox_shift)
        self.horizontalLayout_2.addWidget(self.groupBox_6)
        self.verticalLayout.addWidget(self.groupBox_center)
        self.groupBox_botton = QtWidgets.QGroupBox(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.groupBox_botton.sizePolicy().hasHeightForWidth())
        self.groupBox_botton.setSizePolicy(sizePolicy)
        self.groupBox_botton.setStyleSheet("QGroupBox#groupBox_botton\n"
"{\n"
"   border:0px\n"
"}")
        self.groupBox_botton.setTitle("")
        self.groupBox_botton.setObjectName("groupBox_botton")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.groupBox_botton)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_8 = QtWidgets.QLabel(self.groupBox_botton)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setStyleSheet("QGroupBox{ border: 1px groove grey; border-radius:5px;border-style: outset;}")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_4.addWidget(self.label_8)
        self.pb_max = QtWidgets.QPushButton(self.groupBox_botton)
        self.pb_max.setMinimumSize(QtCore.QSize(80, 80))
        self.pb_max.setMaximumSize(QtCore.QSize(80, 80))
        self.pb_max.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ico/resource/ico/max.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pb_max.setIcon(icon)
        self.pb_max.setIconSize(QtCore.QSize(80, 80))
        self.pb_max.setFlat(True)
        self.pb_max.setObjectName("pb_max")
        self.horizontalLayout_4.addWidget(self.pb_max)
        self.pb_exit = QtWidgets.QPushButton(self.groupBox_botton)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pb_exit.sizePolicy().hasHeightForWidth())
        self.pb_exit.setSizePolicy(sizePolicy)
        self.pb_exit.setMinimumSize(QtCore.QSize(80, 80))
        self.pb_exit.setMaximumSize(QtCore.QSize(80, 80))
        self.pb_exit.setStyleSheet("")
        self.pb_exit.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/ico/resource/ico/exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pb_exit.setIcon(icon1)
        self.pb_exit.setIconSize(QtCore.QSize(80, 80))
        self.pb_exit.setFlat(True)
        self.pb_exit.setObjectName("pb_exit")
        self.horizontalLayout_4.addWidget(self.pb_exit)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.verticalLayout.addWidget(self.groupBox_botton)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_title.setText(_translate("Form", "成都市锦江河道绿化工程一期"))
        self.label_xq.setText(_translate("Form", "星期四"))
        self.label_tq.setText(_translate("Form", "最高温度10C\n"
"最低温度5度"))
        self.label_wd.setText(_translate("Form", "多云转晴"))
        self.label_about.setText(_translate("Form", "TextLabel"))
        self.label_6.setText(_translate("Form", "总计在场人数"))
        self.label_10.setText(_translate("Form", "班组人员统计"))
        self.label_time.setText(_translate("Form", "时间：20：22：10"))
        self.label_12.setText(_translate("Form", "现场人数：30"))
        self.label_7.setText(_translate("Form", "总计人数：100"))
        self.label_11.setText(_translate("Form", "打卡人数：30"))
        self.label_14.setText(_translate("Form", "上班签到"))
        self.label_15.setText(_translate("Form", "下班签到"))
import resource_rc
