from PyQt5 import QtCore
import time


class EmationThread(QtCore.QThread):  # 继承QThread
    resSignal = QtCore.pyqtSignal(str)  # 注册一个信号

    def __init__(self, parent=None, model_path="", emationText=""):  # 从前端界面中传递参数到这个任务后台
        super(EmationThread, self).__init__(parent)
        self.model_path = model_path
        self.emationText = emationText

    def run(self):  # 重写run  比较耗时的后台任务可以在这里运行
        print(self.model_path)

        time.sleep(3)
        print(self.emationText)
        self.Resematin = "Prostive"
        self.resSignal.emit(self.Resematin)  # 任务完成后，发送信号
