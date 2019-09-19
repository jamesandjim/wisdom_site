from PyQt5.QtWidgets import QWidget

from views import sysSetUi


class SysSetWindow(QWidget, sysSetUi.Ui_sysSetForm):
    def __init__(self, parent=None):
        super(SysSetWindow, self).__init__(parent)
        self.setupUi(self)
        self.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius:5px;")