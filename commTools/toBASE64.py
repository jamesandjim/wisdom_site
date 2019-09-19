# 将图片用BASE64转换为字符串
# 将图片转化的字符串进行url编码
import base64
import os
from urllib import parse

BaseDIR = os.path.abspath(os.path.dirname(__file__))
photofile =  os.path.join(BaseDIR, 'photos', '1.jpg')
textfile = os.path.join(BaseDIR, 'outjpg', '1.txt')
outjpg = os.path.join(BaseDIR, 'outjpg', 'out.jpg')
# 图片转为BASE64码
def jpgtostr():
    with open(photofile, "rb") as f:#转为二进制格式
        base64_data = base64.b64encode(f.read())#使用base64进行加密
        str_base64_data = str(base64_data, encoding="utf-8")
        print(str_base64_data)
        url_base64_data = parse.quote(str_base64_data, encoding="utf-8")
        print(url_base64_data)
        txt = url_base64_data.replace('/', '%2F')
        file = open(textfile, 'wt')#写成文本格式
        file.write(txt)
        # file.write(base64_data.decode())#以字符串方式写入
        file.close()
        return txt

# BASE64转换为图片
def strtojpg():
    with open(textfile, 'r') as f:
        imgdata = base64.b64decode(f.read())
        file = open(outjpg, 'wb')
        file.write(imgdata)
        file.close()


