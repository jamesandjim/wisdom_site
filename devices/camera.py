import time
import cv2


# 定义摄像头类
class CameraDev(object):
    def __init__(self, filename="xxx"):
        # 获取摄像头对象，0 系统默认摄像头
        self.filename = filename
        self.cap = cv2.VideoCapture(0)
        # 判断摄像头是否打开，没有则打开
        if not self.cap.isOpened():
            self.cap.open()

    def __del__(self):
        self.releaseDevice()

    def take_photo(self):
        '''
       调用摄像头，捕捉图像
       '''

        while True:
            # 读取图像
            ret, photo = self.cap.read()
            dim = (480, 640)
            new_photo = cv2.resize(photo, dim)
            cv2.imshow('photo', new_photo)
            # 设置等待时间，若数字为0则图像定格
            key = cv2.waitKey(2)
            # 按空格获取图像
            if key == ord(" "):
                # 以当前时间存储
                filename = "./photos_face/" + self.filename + ".jpg"

                # 保存位置
                cv2.imwrite(filename, new_photo)

            # 按“q”退出程序
            if key == ord("q"):
                self.cap.release()
                cv2.destroyAllWindows()
                break

    def getFrame(self):
        ret, frame = self.cap.read()
        if ret:
            cv2.imshow("frame", frame)
            time.sleep(5)
        return frame

    # 录制一段时长的
    def saveVideo(self, filepath, delays):
        # Define the codec and create VideoWriter object
        # 视频编码
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        outputPath = filepath
        # 20fps ,640*480size
        out = cv2.VideoWriter(outputPath, fourcc, 20.0, (640, 480))
        startTime = time.time()
        while (self.cap.isOpened):
            ret, frame = self.cap.read()
            if ret:
                # 翻转图片
                # frame = cv2.flip(frame,0)
                # write the flipped frame
                out.write(frame)
                cv2.imshow('frame', frame)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            else:
                break
            if time.time() - startTime > delays:
                break
        out.release()
        cv2.destroyAllWindows()
        return True

    # 保存一个快照
    def saveSnapshot(self, filepath):
        if self.cap.isOpened:
            ret, frame = self.cap.read()
            if ret:
                cv2.imwrite(filepath, frame)
            else:
                print("save snapshot fail")
                return False
        return True

    def releaseDevice(self):
        # 释放设备
        self.cap.release()

    def reOpen(self):
        if not self.cap.isOpened():
            print("re opened device")
            self.cap = cv2.VideoCapture(0)
            if not self.cap.isOpened():
                self.cap.open()
