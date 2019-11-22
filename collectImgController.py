from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.QtCore import Qt, pyqtSlot, QTimer
from PyQt5.QtGui import QPixmap

from views import collectImg
from devices.camera import CameraDev
import cv2
import qimage2ndarray
from commTools.findFile import getFiles


class CollectImgWindow(QDialog, collectImg.Ui_Dialog):
    def __init__(self, parent=None):
        super(CollectImgWindow, self).__init__(parent)
        self.setupUi(self)
        # self.setWindowFlags(Qt.FramelessWindowHint)
        self.idNo = ''
        self.photo = None
        self.photofile = None
        self.cam = CameraDev()
        self.timer = QTimer()
        self.timer.timeout.connect(self.timeoutFun)
        self.timer.start(1)

    def timeoutFun(self):
        success, self.photo = self.cam.cap.read()
        if success:
            dim = (500, 500)
            ximg = cv2.cvtColor(self.photo, cv2.COLOR_BGR2RGB)
            self.photofile = cv2.resize(ximg, dim)
            img = qimage2ndarray.array2qimage(self.photofile)
            self.lb_photo.setPixmap(QPixmap(img))
            self.lb_photo.show()
        else:
            QMessageBox.information(self, '错误提示', '无法从摄像头得到图像！', QMessageBox.Yes)

    @pyqtSlot()
    def on_pb_takePhoto_clicked(self):
        try:
            filename = "./photos_face/" + self.idNo + ".jpg"
            cv2.imwrite(filename, self.photo)
            self.timer.stop()

            self.pb_accept.setEnabled(True)
        except Exception as e:
            QMessageBox.information(self, '错误提示', e, QMessageBox.Yes)

    @pyqtSlot()
    def on_pb_accept_clicked(self):
        self.accept()

    @pyqtSlot()
    def on_pb_esc_clicked(self):
        self.lb_photo.clear()
        self.reject()
        self.destroy()
