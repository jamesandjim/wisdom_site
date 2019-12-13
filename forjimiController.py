import sys

from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication
from PyQt5.QtCore import pyqtSlot


from views import forjimiUi


class ForjimiWindow(QWidget, forjimiUi.Ui_form_main):
    def __init__(self, parent=None):
        super(ForjimiWindow, self).__init__(parent)
        self.setupUi(self)
        self.zcm = ''

    def forzc(self, xlm):
        a = xlm.split('-')
        b = ''.join(a)
        c = int(b, 16)
        d = str(c)
        e = d[1::2]
        self.zcm = e


    @pyqtSlot()
    def on_pb_ok_clicked(self):

        xlh = self.lineEdit_xlh.text().strip()
        if xlh != '':
            self.forzc(xlh)
            self.lineEdit_zcm.setText(str(self.zcm))
        else:
            QMessageBox.information(self, '提示', '请输入正确的序列号！', QMessageBox.Yes)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    form = ForjimiWindow()
    form.show()
    sys.exit(app.exec_())
