import sys

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import pyqtSlot

import mainwindows
import info_ui


class MyMainWindow(QWidget, mainwindows.Ui_Form):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.tree_menu.itemClicked['QTreeWidgetItem*', 'int'].connect(self.tree_menu_itemClicked)


    def tree_menu_itemClicked(self):
        print(self.tree_menu.currentItem().text(0))
        for i in range(self.verticalLayout_3.count()):
            self.verticalLayout_3.itemAt(i).widget().deleteLater()
        if self.tree_menu.currentItem().text(0) == '人员信息采集':

            te = info_ui.Info_Ui()

            self.verticalLayout_3.addWidget(te)
        else:

            self.main_content.show()

    @pyqtSlot()
    def on_pushButton_clicked(self):
        print('xxx')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MyMainWindow()
    form.show()

    sys.exit(app.exec_())

