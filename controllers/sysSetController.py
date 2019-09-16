from PyQt5.QtWidgets import QWidget

from views import sysSetUi


class SysSetCls(QWidget, sysSetUi.Ui_sysSetForm):
    def __init__(self, parent=None):
        super(SysSetCls, self).__init__(parent)
        self.setupUi(self)