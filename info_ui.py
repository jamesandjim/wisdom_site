from ctypes import *

from PyQt5.QtWidgets import QWidget
from PyQt5 import QtSql
from PyQt5.QtCore import pyqtSlot

import info_collection


class Info_Ui(QWidget, info_collection.Ui_info_collect_Form):
    def __init__(self, parent=None):
        super(Info_Ui, self).__init__(parent)
        self.setupUi(self)

    @pyqtSlot()
    def on_pushButton_clicked(self):
        self.querydb()
        print('xxx')

    def opendb(self):
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')

        db.setDatabaseName('./db/wisdom.db')
        db.open()

    def querydb(self):
        self.opendb()
        # query = QtSql.QSqlQuery()
        query = QtSql.QSqlQueryModel()
        query.setQuery('select bookname as 书名, bookid as 书号, auth as 作者, category as 书类, publisher as 出版社 from book')
        # query.setQuery('select * from book')
        self.tableView.setModel(query)
        self.readCard()

    def readCard(self):
        dll = WinDLL('./dll/termb.dll')
        re = dll.InitComm(0)
        if re <= 0:
            print('打开失败！')
        else:
            print('打开成功！')
            x = dll.Authenticate()
            if x == 1:
                re = dll.Read_Content(1)
                if re == 1:
                    da = ''
                    dll.getName(da, 64)
                    print(da)


