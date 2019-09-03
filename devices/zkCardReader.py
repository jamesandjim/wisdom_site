from ctypes import *
import base64

class CardReader:
    def __init__(self):
        self.dev = WinDLL('./dll/termb.dll')
        self.cbDataSize = 128
        self.GphotoSize = 256 * 1024
        self.info = {}

    def openDevice(self):
        """大于0表示成功，返回值为端口号"""
        return self.dev.InitCommExt()


    def closeDevice(self):
        """返回值为1表示成功，为0表示失败"""
        return self.dev.CloseComm()

    def readCard(self):
        try:
            auth = self.dev.Authenticate()
            if  auth == 1:
                if self.dev.Read_Content(1) >= 1:

                    b_name = create_string_buffer(self.cbDataSize)
                    self.dev.getName(byref(b_name), self.cbDataSize)
                    name = b_name.value.decode('gbk')

                    b_sex = create_string_buffer(self.cbDataSize)
                    self.dev.getSex(byref(b_sex), self.cbDataSize)
                    sex = b_sex.value.decode('gbk')

                    b_Nation = create_string_buffer(self.cbDataSize)
                    self.dev.getNation(byref(b_Nation), self.cbDataSize)
                    nation = b_Nation.value.decode('gbk')

                    b_Birthdate = create_string_buffer(self.cbDataSize)
                    self.dev.getBirthdate(byref(b_Birthdate), self.cbDataSize)
                    birthdate = b_Birthdate.value.decode('gbk')

                    b_Address = create_string_buffer(self.cbDataSize)
                    self.dev.getAddress(byref(b_Address), self.cbDataSize)
                    address = b_Address.value.decode('gbk')

                    b_IDNum = create_string_buffer(self.cbDataSize)
                    self.dev.getIDNum(byref(b_IDNum), self.cbDataSize)
                    idNum = b_IDNum.value.decode('gbk')

                    b_Issue = create_string_buffer(self.cbDataSize)
                    self.dev.getIssue(byref(b_Issue), self.cbDataSize)
                    issue = b_Issue.value.decode('gbk')

                    b_EffectedDate = create_string_buffer(self.cbDataSize)
                    self.dev.getEffectedDate(byref(b_EffectedDate), self.cbDataSize)
                    effectedDate = b_EffectedDate.value.decode('gbk')

                    b_ExpiredDate = create_string_buffer(self.cbDataSize)
                    self.dev.getExpiredDate(byref(b_ExpiredDate), self.cbDataSize)
                    expiredDate = b_ExpiredDate.value.decode('gbk')

                    self.info['name'] = name
                    self.info['nation'] = nation
                    self.info['sex'] = sex
                    self.info['birthdate'] = birthdate
                    self.info['address'] = address
                    self.info['idNum'] = idNum
                    self.info['issue'] = issue
                    self.info['effectedDate'] = effectedDate
                    self.info['expiredDate'] = expiredDate

                    self.dev.GetBmpPhotoExt()
                    b_Photo = create_string_buffer(self.GphotoSize)
                    self.dev.getBMPPhotoBase64(byref(b_Photo), self.GphotoSize)
                    print(len(str(b_Photo, encoding='utf-8')))

                    self.info['b_Photo'] = b_Photo

            return auth
        except Exception:
            print(Exception)













