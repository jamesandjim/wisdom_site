from PyQt5.QtWidgets import QWidget

from views import attendanceManagementUi


class AttendanceManagementWindow(QWidget, attendanceManagementUi.Ui_Form):
    def __init__(self, parent=None):
        super(AttendanceManagementWindow, self).__init__(parent)
        self.setupUi(self)