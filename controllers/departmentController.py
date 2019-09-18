from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5.QtCore import pyqtSlot, QModelIndex

from models.dbtools import Dboperator

from views import departmentUi


class DepartmentWindow(QWidget, departmentUi.Ui_Form):
    def __init__(self, parent=None):
        super(DepartmentWindow, self).__init__(parent)
        self.setupUi(self)
        self.db = Dboperator()
        self.data = None
        self.load()
        self.txtDisable()

    def txtEnable(self):
        """将输入框设置为可用"""
        self.le_departmentDemo.setEnabled(True)
        self.le_departmentName.setEnabled(True)
        self.le_departmentID.setEnabled(True)
        self.pb_save.setEnabled(True)
        self.le_departmentID.setFocus()
        self.pb_add.setEnabled(False)

    def txtDisable(self):
        """将输入框设置为不可用"""
        self.le_departmentDemo.setEnabled(False)
        self.le_departmentName.setEnabled(False)
        self.le_departmentID.setEnabled(False)
        self.pb_save.setEnabled(False)
        self.pb_del.setEnabled(False)
        self.pb_update.setEnabled(False)

    def txtClear(self):
        """清除输入框内容"""
        self.le_departmentDemo.clear()
        self.le_departmentName.clear()
        self.le_departmentID.clear()

    def load(self):
        """表格装载全部的数据"""
        qs = 'select id as 部门编号, name as 部门名称, memo as 部门详细说明 from wis_department'
        alldata = self.db.querySQL(qs)
        self.data = alldata
        self.tv_department.setModel(self.data)


    @pyqtSlot()
    def on_pb_add_clicked(self):
        """增加 按钮函数"""
        self.txtEnable()

    @pyqtSlot()
    def on_pb_update_clicked(self):
        """修改 按钮函数"""
        self.txtEnable()
        self.le_departmentID.setEnabled(False)

    @pyqtSlot()
    def on_pb_esc_clicked(self):
        self.txtClear()
        self.pb_del.setEnabled(False)
        self.pb_update.setEnabled(False)
        self.pb_add.setEnabled(True)
        self.pb_save.setEnabled(False)

    @pyqtSlot()
    def on_pb_save_clicked(self):
        """保存 按钮函数"""
        departmentID = self.le_departmentID.text()
        departmentName = self.le_departmentName.text()
        departmentDemo = self.le_departmentDemo.text()
        if departmentID != '' and departmentName != '':
            qs = "select * from wis_department where id = '%s' or name = '%s'" % (departmentID, departmentName)
            data = self.db.querySQL(qs)
            if data.rowCount() == 0:
                qs = "INSERT INTO wis_department VALUES('%s','%s','%s')" % (departmentID, departmentName, departmentDemo)
                self.db.excuteSQl(qs)
                self.load()
                self.txtClear()
                self.le_departmentID.setFocus()
            else:
                QMessageBox.information(self, '提示', '编号与名称不能重复！', QMessageBox.Yes)
                self.txtClear()
                self.pb_del.setEnabled(False)
                self.pb_update.setEnabled(False)
                self.pb_add.setEnabled(True)
                self.pb_save.setEnabled(False)
                self.txtDisable()
        else:
            QMessageBox.information(self, '提示', '编号与名称不能为空！', QMessageBox.Yes)
            self.txtClear()
            self.pb_del.setEnabled(False)
            self.pb_update.setEnabled(False)
            self.pb_add.setEnabled(True)
            self.pb_save.setEnabled(False)
            self.txtDisable()


    @pyqtSlot(QModelIndex)
    def on_tv_department_clicked(self, QModelIndex):
        """选中表格中一行的处理函数"""
        rowID = self.tv_department.currentIndex().row()
        data = self.data.index(rowID, 0).data()

        self.le_departmentID.setText(data)
        self.le_departmentName.setText(self.data.index(rowID, 1).data())
        self.le_departmentDemo.setText(self.data.index(rowID, 2).data())

        self.txtDisable()

        self.pb_add.setEnabled(False)
        self.pb_update.setEnabled(True)
        self.pb_del.setEnabled(True)


    @pyqtSlot()
    def on_pb_query_clicked(self):
        """查询 按钮的函数"""
        qs = "select id as 部门编号, name as 部门名称, memo as 部门详细说明 from wis_department where 部门名称 like '%{}%'".format(self.le_queryPara.text())
        data = self.db.querySQL(qs)
        self.tv_department.setModel(data)

    @pyqtSlot()
    def on_pb_allData_clicked(self):
        """全部数据 按钮的函数"""
        self.le_queryPara.clear()
        self.load()

    @pyqtSlot()
    def on_pb_del_clicked(self):
        """删除按钮的处理函数"""
        qs = "delete from wis_department where id = '%s' " % self.le_departmentID.text()
        self.db.excuteSQl(qs)
        self.txtClear()
        self.load()









