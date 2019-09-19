import sys

from PyQt5 import QtWidgets, QtCore

from tmp.ht import EmationThread


class MyForm(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(492, 386)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(40, 120, 341, 80))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.emationText = QtWidgets.QTextEdit(self.horizontalLayoutWidget_2)
        self.emationText.setObjectName("emationText")
        self.horizontalLayout_2.addWidget(self.emationText)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(40, 37, 341, 81))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Model_But = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.Model_But.setObjectName("Model_But")
        self.horizontalLayout.addWidget(self.Model_But)
        self.Model_path = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.Model_path.setObjectName("Model_path")
        self.horizontalLayout.addWidget(self.Model_path)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(100, 210, 201, 80))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.emationRes = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        self.emationRes.setObjectName("emationRes")
        self.horizontalLayout_3.addWidget(self.emationRes)
        self.submitBut = QtWidgets.QPushButton(self.horizontalLayoutWidget_3)
        self.submitBut.setObjectName("submitBut")
        self.horizontalLayout_3.addWidget(self.submitBut)
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 492, 23))
        self.menubar.setObjectName("menubar")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)
        self.widgetUnit()
        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def widgetUnit(self):
        self.Model_But.clicked.connect(self.ModelButSolt)
        self.submitBut.clicked.connect(self.SubmitButSlot)

    def ModelButSolt(self):
        self.fileName, tpye = QtWidgets.QFileDialog.getOpenFileName(caption="选择文件夹", directory="./",
                                                                    filter="All Files (*);;Text Files (*.txt)")
        self.Model_path.setText(self.fileName)

    def SubmitButSlot(self):
        emationText = self.emationText.toPlainText()
        modelPath = self.Model_path.text()
        self.ThreadEmation = EmationThread(model_path=modelPath, emationText=emationText)
        self.ThreadEmation.resSignal.connect(self.ResSlot)  # 把任务完成的信号与任务完成后处理的槽函数绑定
        self.ThreadEmation.start()

    def ResSlot(self, res):
        self.emationRes.setText(res)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "情感分析"))
        self.label_2.setText(_translate("mainWindow", "情感分析文本："))
        self.Model_But.setText(_translate("mainWindow", "选择Model:"))
        self.emationRes.setText(_translate("mainWindow", "情感分析结果"))
        self.submitBut.setText(_translate("mainWindow", "分析"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QMainWindow()
    ui = MyForm()
    ui.setupUi(widget)
    widget.show()
    sys.exit(app.exec_())
