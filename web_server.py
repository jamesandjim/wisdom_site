from flask import Flask, request
from PyQt5.Qt import QImage, QPixmap
import requests
from ftp import myFtp


app = Flask(__name__)
@app.route('/getFace', methods=["POST"])
def getFace():
    j = request.get_json()
    r = j['newImgPath']
    print(r)
    ftp = myFtp('192.168.0.105')
    ftp.Login('', '')
    ftp.DownLoadFile('./face_photos/{}.jpg'.format(j['personId']), './faceRegister/{}_{}.jpg'.format(j['personId'], j['faceId']))
    ftp.close()

    print(j)
    return j


@app.route('/getRecord', methods=["POST"])
def getRecord():
    j = request.get_json()
    print(j)
    return {"result": 1, "success": True}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=False)
