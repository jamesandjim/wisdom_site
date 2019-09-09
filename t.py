import base64
from PyQt5.QtWidgets import QWidget, QMessageBox, QFileDialog,QApplication,QLabel
from PyQt5 import QtSql, QtGui
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.Qt import QImage, QPixmap
import requests


import sys


if __name__ == '__main__':
    app = QApplication(sys.argv)

    form = QWidget()
    form.resize(500, 500)

    s = requests_ftp.monkeypatch_session()
    s = requests.Session()

    r = s.stor('ftp://192.168.0.105:8010/faceRegister/10001_e052f9d1eda94afea998f20d9c09bd70.jpg', auth=('', ''), files={'file': open('xxx.jpg', 'rb')})
    print(r.content)
    map = QPixmap()

    map.loadFromData(r.content, "JPG")
    lb1 = QLabel(form)
    lb1.setPixmap(map)

    with open("test.jpg", "wb") as f:
        f.write(r.content)

    form.show()


    sys.exit(app.exec_())