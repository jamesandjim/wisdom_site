from PyQt5 import QtCore
import time
import web_server

class EmationThread(QtCore.QThread):  # 继承QThread
    resSignal = QtCore.pyqtSignal(dict)  # 注册一个信号

    def __init__(self, parent=None, dic={}):  # 从前端界面中传递参数到这个任务后台
        super(EmationThread, self).__init__(parent)
        self.dic = dic

    def run(self):  # 重写run  比较耗时的后台任务可以在这里运行

        time.sleep(1)
        self.resSignal.emit(self.dic)  # 任务完成后，发送信号
