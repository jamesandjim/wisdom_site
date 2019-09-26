from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5.QtCore import pyqtSlot, QModelIndex

from models.dbtools import Dboperator

from views import zjptUi


class ZjptDeviceWindow(QWidget, zjptUi.Ui_Form):
    def __init__(self, parent=None):
        super(ZjptDeviceWindow, self).__init__(parent)
        self.setupUi(self)
        self.db = Dboperator()
        self.load()

    def load(self):
        qs = "select * from wis_cdzjpt where id = '99'"
        current = self.db.querySQL(qs).record(0)
        self.le_deletePersonURL.setText(current.field('deletePersonURL').value())
        self.le_downloadPersonURL.setText(current.field('downloadPersonURL').value())
        self.le_feedbackURL.setText(current.field('feedbackURL').value())
        self.le_uploadAttURL.setText(current.field('uploadAttURL').value())
        self.le_uploadPersonURL.setText(current.field('uploadPersonURL').value())

    def enableAll(self):
        self.le_uploadPersonURL.setEnabled(True)
        self.le_uploadAttURL.setEnabled(True)
        self.le_feedbackURL.setEnabled(True)
        self.le_downloadPersonURL.setEnabled(True)
        self.le_deletePersonURL.setEnabled(True)
        self.pb_save.setEnabled(True)

    def disableAll(self):
        self.le_uploadPersonURL.setEnabled(False)
        self.le_uploadAttURL.setEnabled(False)
        self.le_feedbackURL.setEnabled(False)
        self.le_downloadPersonURL.setEnabled(False)
        self.le_deletePersonURL.setEnabled(False)
        self.pb_save.setEnabled(False)

    @pyqtSlot()
    def on_pb_update_clicked(self):
        self.enableAll()

    @pyqtSlot()
    def on_pb_save_clicked(self):
        uploadPersonURL = self.le_uploadPersonURL.text()
        downloadPersonURL= self.le_downloadPersonURL.text()
        deletePersonURL = self.le_deletePersonURL.text()
        uploadAttURL = self.le_uploadAttURL.text()
        feedbackURL = self.le_feedbackURL.text()

        qs = "update wis_cdzjpt set uploadPersonURL = '%s', downloadPersonURL = '%s', deletePersonURL = '%s', uploadAttURL = '%s', feedbackURL = '%s'"%(uploadPersonURL,downloadPersonURL,deletePersonURL, uploadAttURL, feedbackURL)
        self.db.excuteSQl(qs)
        self.disableAll()



