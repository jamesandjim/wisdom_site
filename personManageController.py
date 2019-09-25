from PyQt5.QtWidgets import QWidget

from views import personManagementUi


class PersonManageWindow(QWidget, personManagementUi.Ui_Form):
    def __init__(self, parent=None):
        super(PersonManageWindow, self).__init__(parent)
        self.setupUi(self)