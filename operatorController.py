from PyQt5.QtWidgets import QWidget, QMessageBox, QStyledItemDelegate
from PyQt5.QtCore import pyqtSlot, QModelIndex, Qt
from PyQt5.QtGui import QIcon

from models.dbtools import Dboperator

from views import operatorUi


class OperatorWindow(QWidget, operatorUi.Ui_Form):
    def __init__(self, parent=None):
        super(OperatorWindow, self).__init__(parent)
        self.setupUi(self)
        self.db = Dboperator()
        self.data = None
        self.load()
        self.txtDisable()

    def txtEnable(self):
        """将输入框设置为可用"""
        self.le_qxz.setEnabled(True)
        self.le_name.setEnabled(True)
        self.le_password.setEnabled(True)
        self.pb_save.setEnabled(True)
        self.le_name.setFocus()
        self.pb_add.setEnabled(False)

    def txtDisable(self):
        """将输入框设置为不可用"""
        self.le_qxz.setEnabled(False)
        self.le_password.setEnabled(False)
        self.le_name.setEnabled(False)
        self.pb_save.setEnabled(False)
        self.pb_del.setEnabled(False)
        self.pb_update.setEnabled(False)

    def txtClear(self):
        """清除输入框内容"""
        self.le_qxz.clear()
        self.le_password.clear()
        self.le_name.clear()
        self.checkBox_isAdmin.setChecked(False)

    def load(self):
        """表格装载全部的数据"""
        qs = "select name as 操作员名称, password as 操作员密码, qxz as 权限组, case isAdmin when 1 then '管理员' else '普通人员' end as 是否管理员 from wis_operator"
        alldata = self.db.querySQL(qs)
        self.data = alldata
        self.tv_operator.setModel(self.data)
        delegate = MyDelegate()
        self.tv_operator.setItemDelegateForColumn(1, delegate)


    @pyqtSlot()
    def on_pb_add_clicked(self):
        """增加 按钮函数"""
        self.txtEnable()

    @pyqtSlot()
    def on_pb_update_clicked(self):
        """修改 按钮函数"""
        self.txtEnable()
        self.le_name.setEnabled(False)

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
        name = self.le_name.text()
        password = self.le_password.text()
        qxz = self.le_qxz.text()
        isAdmin = 1 if self.checkBox_isAdmin.isChecked() else 0
        if name != '' and password != '':
            qs = "select name as 操作员名称, password as 操作员密码, qxz as 权限组, case isAdmin when 1 then '管理员' else '普通人员' end as 是否管理员 from wis_operator where name = '%s'" % name
            data = self.db.querySQL(qs)
            if data.rowCount() == 0:
                qs = "INSERT INTO wis_operator VALUES('%s','%s','%s', %d)" % (name, password, qxz, isAdmin)
                self.db.excuteSQl(qs)
                self.load()
                self.txtClear()
                self.le_name.setFocus()
            else:
                QMessageBox.information(self, '提示', '操作员名称不能重复！', QMessageBox.Yes)
                self.txtClear()
                self.pb_del.setEnabled(False)
                self.pb_update.setEnabled(False)
                self.pb_add.setEnabled(True)
                self.pb_save.setEnabled(False)
                self.txtDisable()
        else:
            QMessageBox.information(self, '提示', '人员名称和密码不能为空！', QMessageBox.Yes)
            self.txtClear()
            self.pb_del.setEnabled(False)
            self.pb_update.setEnabled(False)
            self.pb_add.setEnabled(True)
            self.pb_save.setEnabled(False)
            self.txtDisable()


    @pyqtSlot(QModelIndex)
    def on_tv_operator_clicked(self, QModelIndex):
        """选中表格中一行的处理函数"""
        rowID = self.tv_operator.currentIndex().row()
        name = self.data.index(rowID, 0).data()

        self.le_name.setText(name)
        self.le_password.setText(self.data.index(rowID, 1).data())
        self.le_qxz.setText(self.data.index(rowID, 2).data())
        if self.data.index(rowID, 3).data() == '管理员':
            self.checkBox_isAdmin.setChecked(True)
        else:
            self.checkBox_isAdmin.setChecked(False)

        self.txtDisable()

        self.pb_add.setEnabled(False)
        self.pb_update.setEnabled(True)
        self.pb_del.setEnabled(True)

    @pyqtSlot()
    def on_pb_query_clicked(self):
        """查询 按钮的函数"""
        qs = "select name as 操作员名称, password as 操作员密码, qxz as 权限组, case isAdmin when 1 then '管理员' else '普通人员' end as 是否管理员 from wis_operator where name like '%{}%'".format(self.le_queryPara.text())
        data = self.db.querySQL(qs)
        self.tv_operator.setModel(data)

    @pyqtSlot()
    def on_pb_del_clicked(self):
        """删除按钮的处理函数"""
        qs = "delete from wis_operator where name = '%s' and  name != 'admin'" % self.le_name.text()
        self.db.excuteSQl(qs)
        self.txtClear()
        self.load()


class MyDelegate(QStyledItemDelegate):
    def __init__(self, parent=None):
        super(MyDelegate, self).__init__(parent)
        self._icons = QIcon(':/ico/resource/ico/mima.jpg')

    def get_icon(self):
        # get the icon according to the condition:
        # In this case, for example,
        # the icon will be repeated periodically
        icon = QIcon(':/ico/resource/ico/mima.jpg')
        return icon

    def paint(self, painter, option, index):
        icon = self.get_icon()
        icon.paint(painter, option.rect, Qt.AlignCenter)







