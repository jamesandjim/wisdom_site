from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import pyqtSlot

import info_collection

class Info_Ui(QWidget, info_collection.Ui_info_collect_Form):
    def __init__(self, parent=None):
        super(Info_Ui, self).__init__(parent)
        self.setupUi(self)

    @pyqtSlot()
    def on_pushButton_clicked(self):
        print('xxx')