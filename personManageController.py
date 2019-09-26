from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import pyqtSlot, QModelIndex, Qt

from models.dbtools import Dboperator
from views import personManagementUi


class PersonManageWindow(QWidget, personManagementUi.Ui_Form):
    def __init__(self, parent=None):
        super(PersonManageWindow, self).__init__(parent)
        self.setupUi(self)
        self.db = Dboperator()
        self.load()

    def load(self):
        qs = "select idNo, name, case gender when 1 then '男' when 0 then '女' end from wis_person"
        allPerson = self.db.querySQL(qs)
        self.tv_person.setModel(allPerson)
        allPerson.setHeaderData(0, Qt.Horizontal, '身份证号码')
        allPerson.setHeaderData(1, Qt.Horizontal, '姓名')
        allPerson.setHeaderData(2, Qt.Horizontal, '性别')