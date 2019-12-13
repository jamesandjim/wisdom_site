import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import QPixmap
from PyQt5.QtCore import QTimer, Qt, pyqtSlot, QTime, QDate
from PyQt5.QtGui import QCursor

from commTools import weather
from views import lcdMonitorUi
from models.dbtools import Dboperator


class LcdMonitorWindow(QtWidgets.QWidget, lcdMonitorUi.Ui_Form):
    def __init__(self, parent=None):
        super(LcdMonitorWindow, self).__init__(parent)
        self.setupUi(self)
        self.listWidget_l.setHorizontalScrollBarPolicy(1)
        self.listWidget_l.setVerticalScrollBarPolicy(1)
        self.listWidget_r.setHorizontalScrollBarPolicy(1)
        self.listWidget_r.setVerticalScrollBarPolicy(1)

        self.db = Dboperator()
        self.setTitle()
        self.firstWeather()

        self.timer = QTimer()
        self.timer.timeout.connect(self.load)
        self.timer.start(1)

    def firstWeather(self):
        qs = "select * from wis_lcdConfig where id = '99'"
        confs = self.db.querySQL(qs)
        city = confs.record(0).field('location').value()
        we = weather.getWeatherBycityName(city)
        fengli = weather.getFengLi(we['fengli'])
        self.label_xq.setText(we['date'])
        self.label_tq.setText(we['type'])
        wd = "%s\n%s" % (we['high'], we['low'])
        self.label_wd.setText(wd)
        self.label_fengli.setText(r'%s' % fengli)
        date = QDate.currentDate().toString(Qt.DefaultLocaleLongDate)
        day = QDate.currentDate().day()
        self.lcdNumber_date.display(str(date))
        qs = "update wis_lcdConfig set weatherDay = '%s'" % str(day)
        self.db.excuteSQl(qs)


    def setWeather(self):
        qs = "select * from wis_lcdConfig where id = '99'"
        confs = self.db.querySQL(qs)
        day = confs.record(0).field('weatherDay').value()
        if day != str(QDate.currentDate().day()):
            city = confs.record(0).field('location').value()
            we = weather.getWeatherBycityName(city)

            fengli = weather.getFengLi(we['fengli'])
            self.label_xq.setText(we['date'])
            self.label_tq.setText(we['type'])
            wd = "%s\n%s" % (we['high'], we['low'])
            self.label_wd.setText(wd)
            self.label_fengli.setText(fengli)

    def setTitle(self):
        qs = "select lcdTitle from wis_sysSet where id = '99'"
        sy = self.db.querySQL(qs)
        title = sy.record(0).field('lcdTitle').value()
        self.label_title.setText(title)
        self.label_title.setStyleSheet("font: 75 36pt \"微软雅黑\";\n"
                                 "color: rgb(255, 255, 255);")


    def refreshNum(self):
        for i in range(self.flayout_bz.count()):
            self.flayout_bz.itemAt(i).widget().deleteLater()

        qs = "select * from wis_department where forLcd = 1"
        sumq = "select sum(currentNum) as sumq from wis_department where forLcd = 1"
        dps = self.db.querySQL(qs)
        q = self.db.querySQL(sumq)
        countq = q.record(0).field('sumq').value()
        self.lcdNumber_all.display(str(countq))
        dps_count = dps.rowCount()
        if dps_count > 0:
            i = 0
            while i < dps_count:
                name = dps.record(i).field('name').value()
                currentNum = dps.record(i).field('currentNum').value()
                label = QtWidgets.QLabel(name)
                label.setStyleSheet("font: 75 26pt \"微软雅黑\";\n"
                                    "color: rgb(255, 255, 255);")

                num = QtWidgets.QLCDNumber(5, self)
                num.setStyleSheet("font: 75 26pt \"微软雅黑\";\n"
                                  "color: rgb(255, 255, 255);")
                num.setMode(QtWidgets.QLCDNumber.Dec)
                num.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
                num.setFrameShape(QtWidgets.QLCDNumber.NoFrame)
                num.setDigitCount(5)
                num.setNumDigits(3)
                num.display(currentNum)

                self.flayout_bz.addRow(label, num)

                time = QTime.currentTime().toString(Qt.DefaultLocaleLongDate)
                self.label_time.setText("当前时间：%s" % time)

                i += 1


    def refreshPhoto(self):

        qs = '''
              select wis_recordsx.name, wis_recordsx.usec, wis_recordsx.per_id, wis_person.department, wis_person.idphoto
              from wis_recordsx, wis_person
              where wis_recordsx.per_id = wis_person.idNo 
              order by sequence desc
              limit 0, 1
             '''
        dps = self.db.querySQL(qs)
        dps_count = dps.rowCount()
        if dps_count > 0:
            i = 0
            while i < dps_count:
                # 处理需要显示的数据
                name = dps.record(i).field('name').value()
                usec = dps.record(i).field('usec').value()
                per_id = dps.record(i).field('per_id').value()
                department = dps.record(i).field('department').value()
                idphoto = dps.record(i).field('idphoto').value()

                info = "班组：%s\n 人员：%s\n 时间：%s" % (department, name, usec[11:])
                # 建立 两个LABEL 左边显示图片，右边显示信息
                idphoto_pixmap = QPixmap(idphoto).scaled(150, 200)
                label_photo = QtWidgets.QLabel()
                label_photo.setPixmap(idphoto_pixmap)
                label_info = QtWidgets.QLabel(info)

                widget = QtWidgets.QWidget()
                layout_main = QtWidgets.QVBoxLayout()
                layout_center = QtWidgets.QHBoxLayout()
                layout_center.addWidget(label_photo)
                layout_center.addWidget(label_info)
                layout_main.addLayout(layout_center)
                widget.setLayout(layout_main)

                item = QtWidgets.QListWidgetItem()
                item.setSizeHint((QtCore.QSize(150, 300)))
                self.listWidget_l.addItem(item)
                self.listWidget_l.setItemWidget(item, widget)


                i += 1

    def load(self):
        self.refreshNum()
        self.refreshPhoto()
        self.setWeather()

    @pyqtSlot()
    def on_pb_max_clicked(self):
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.showMaximized()

    @pyqtSlot()
    def on_pb_exit_clicked(self):
        self.close()

    def mousePressEvent(self, QMouseEvent):

        if QMouseEvent.button() == Qt.LeftButton:
            self.flag = True

            self.m_Position = QMouseEvent.globalPos() - self.pos()

            QMouseEvent.accept()

            self.setCursor(QCursor(Qt.OpenHandCursor))

    def mouseMoveEvent(self, QMouseEvent):

        if Qt.LeftButton and self.flag:
            self.move(QMouseEvent.globalPos() - self.m_Position)

            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):

        self.flag = False

        self.setCursor(QCursor(Qt.ArrowCursor))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    form = LcdMonitorWindow()
    form.showMaximized()
    sys.exit(app.exec_())