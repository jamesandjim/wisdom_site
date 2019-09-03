from PyQt5 import QtSql
from PyQt5.QtSql import QSqlQuery, QSql, QSqlQueryModel, QSqlTableModel


class Dboperator:
    """
    为对数据库进行CRUD操作的封装，传入的SQLSTR需要做好拼接
    """
    def __init__(self):
        self.db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('./db/wisdom.db')
        self.db.open()
        self.query = QSqlQuery()

    def __del__(self):
        self.db.close()

    def excuteSQl(self, sqlstr):
        """操作除查询外的所有数据库操作"""
        try:
            self.query.exec_(sqlstr)
            self.db.commit()
        except Exception as e:
            print(e)

    def querySQL(self, sqlstr):
        """执行查询数据库的操作，返回一个"QSqlQueryModel"实例"""
        query = QSqlQueryModel()
        query.setQuery(sqlstr)
        return query

