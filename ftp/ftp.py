import os
import sys
import ftplib  # 定义了FTP类,实现ftp上传和下载


class myFtp:
    # 定义一个ftp对象
    ftp = ftplib.FTP()

    def __init__(self, host, port=8010):  # 类似c++构造函数
        self.ftp.connect(host, port)

    # 登陆
    def Login(self, user, passwd):
        self.ftp.login(user, passwd)
        print(self.ftp.welcome)  # 打印出欢迎信息

    # 下载单个文件
    # LocalFile为本地文件路径（带文件名）,RemoteFile为ftp文件路径(不带文件名)
    def DownLoadFile(self, LocalFile, RemoteFile):
        if (os.path.exists(LocalFile)):
            os.remove(LocalFile)
        file_handler = open(LocalFile, 'wb')
        print(file_handler)
        # 下载ftp文件
        self.ftp.retrbinary('RETR ' + RemoteFile, file_handler.write)
        file_handler.close()
        return True

    # 下载整个目录下的文件
    # LocalDir为本地目录（不带文件名）,RemoteDir为远程目录(不带文件名)
    def DownLoadFileTree(self, LocalDir, RemoteDir):
        print("RemoteDir:", RemoteDir)
        if not os.path.exists(LocalDir):
            os.makedirs(LocalDir)
        # 打开该远程目录
        self.ftp.cwd(RemoteDir)
        # 获取该目录下所有文件名，列表形式
        RemoteNames = self.ftp.nlst()
        for file in RemoteNames:
            Local = os.path.join(LocalDir, file)  # 下载到当地的全路径
            print(self.ftp.nlst(file))  # [如test.txt]
            if file.find(".") == -1:  # 是否子目录 如test.txt就非子目录
                if not os.path.exists(Local):
                    os.makedirs(Local)
                self.DownLoadFileTree(Local, file)  # 下载子目录路径
            else:
                self.DownLoadFile(Local, file)
        self.ftp.cwd("..")  # 返回路径最外侧
        return

    # 关闭ftp连接
    def close(self):
        self.ftp.close()


if __name__ == "__main__":
    # 建立一个ftp连接
    ftp = myFtp('192.168.0.105')
    # 登陆
    ftp.Login('', '')
    # 下载单个文件
    ftp.DownLoadFile('xxx.jpg', './faceRegister/10001_e052f9d1eda94afea998f20d9c09bd70.jpg')
    # 下载整个目录下的文件
    # ftp.DownLoadFileTree('D:/data/', '/home/')
    # 关闭ftp连接
    ftp.close()
    print("over")