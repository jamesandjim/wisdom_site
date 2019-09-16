import sys

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtCore import pyqtSlot

from views import mainUi
from controllers import infoCollectionController
from controllers import sysSetController


class MyMainWindow(QWidget, mainUi.Ui_mainForm):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.tree_menu.expandAll()
        # self.tree_menu.itemClicked['QTreeWidgetItem*', 'int'].connect(self.tree_menu_itemClicked)

    def removeC(self):
        for i in range(self.verticalLayout_3.count()):
            self.verticalLayout_3.itemAt(i).widget().deleteLater()

    @pyqtSlot('QTreeWidgetItem*', 'int')
    def on_tree_menu_itemClicked(self):
        # print(self.tree_menu.currentItem().text(0))
        selected = self.tree_menu.currentItem().text(0)

        if selected == '人员信息采集':
            widget = infoCollectionController.InfoCollectionCls()
            self.removeC()
            self.verticalLayout_3.addWidget(widget)

        elif selected == '系统参数设置':
            widget = sysSetController.SysSetWindow()
            self.removeC()
            self.verticalLayout_3.addWidget(widget)

        elif selected == '住建平台信息设置':
            pass

        elif selected == '人员信息查询':
            pass

        elif selected == '人员考勤数据管理':
            pass

        elif selected == '系统参数设置':
            pass

        elif selected == '采集设备':
            pass

        elif selected == '考勤设备':
            pass

        elif selected == '显示屏设备':
            pass

        elif selected == '显示屏内容设置':
            pass

        elif selected == 'LCD显示':
            pass

        elif selected == '数据备份':
            pass

        elif selected == '系统人员管理':
            pass

        elif selected == '班组信息管理':
            pass

        else:
            pass

    @pyqtSlot()
    def on_pushButton_clicked(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MyMainWindow()
    form.show()

    sys.exit(app.exec_())

