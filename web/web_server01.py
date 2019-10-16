from flask import Flask, request
from ftp.ftp import myFtp
import json
import time
import base64

from models.dbtools import Dboperator

db = Dboperator()


app = Flask(__name__)
@app.route('/getFace', methods=["POST"])
def getFace():
    j = request.get_json()
    r = j['newImgPath']
    print(r)
    ftp = myFtp('192.168.0.105')
    ftp.Login('', '')
    ftp.DownLoadFile('./photos_face/{}.jpg'.format(j['personId']), './faceRegister/{}_{}.jpg'.format(j['personId'], j['faceId']))
    ftp.close()

    print(j)
    return j


@app.route('/getRecord', methods=["POST"])
def getRecord():

    r = request.get_data().decode('utf-8')

    rstr = r.replace('accessRecord=', '')
    jn = json.loads(rstr)

    faceId = jn['faceId']
    act = jn['act']
    qs = '''
        insert into wis_records values ('%s', %d, %d, %d, '%s', '%s', %d, %d, %d, %d, %d, %d, %d, %d, %d, '%s', '%s')
        ''' % (jn['faceId'], jn['act'], jn['score'], jn['datetime'], jn['image'], jn['ip'], jn['age'], jn['gender'],
               jn['glasses'], jn['mask'], jn['race'], jn['beard'], jn['expression'], jn['iccard'], jn['role'], jn['mac'], jn['bg_image'])
    db.excuteSQl(qs)


    with open('records.txt', 'a') as f:
        f.write(rstr)

    img = base64.b64decode(jn['image'])
    filename = "%s_%d.jpg" % (jn['faceId'], jn['datetime'])
    with open(filename, 'wb') as f:
        f.write(img)



    return 'ok'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=False)
