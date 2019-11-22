# 建立本地服务器，基于HTTPCOMET
import tornado.web
import tornado.httpserver
import tornado.ioloop
import tornado.options

from cometResultHandle import ResultHandle, RecordHandle
from uuid import uuid4
import json

from models.dbtools import Dboperator


# 服务器端保存的字符串
class Announce:
    subject = {}
    callbacks = []

    def register(self, callback):
        self.callbacks.append(callback)

    # 改变后，会推送给保存的注册的客户端
    def changeSubject(self, data):
        self.subject = data
        self.notifyCallbacks()

    def getJson(self):
        return json.dumps(self.subject)

    def notifyCallbacks(self):
        for c in self.callbacks:
            self.callbackHelper(c)

        self.callbacks = []

    def callbackHelper(self, callback):
        callback(self.subject)


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")


class ChatHandler(tornado.web.RequestHandler):
    def post(self):
        version = self.get_argument('version')
        cmd = self.get_argument('cmd')
        ctrl_type = self.get_argument('ctrl_type')
        content = {"version": version, "cmd": cmd, "ctrl_type": ctrl_type}
        self.application.announce.changeSubject(content)
        print(content)


class RecordHandler(tornado.web.RequestHandler):

    def post(self):
        bo1 = self.request.body
        # print(bo1.decode('utf-8'))
        bo2 = bo1.decode('utf-8')
        bo3 = json.loads(bo2)
        # print(bo3)

        # with open('log.txt', 'a+') as f:
        #     f.write(str(bo3))

        op = RecordHandle(bo3)
        op.insertdb()

# 增加人脸的请求处理
class AddFace(tornado.web.RequestHandler):
    def post(self):
        dic = {}
        dic['version'] = self.get_body_argument('version')
        dic['cmd'] = self.get_body_argument('cmd')
        dic['per_id'] = self.get_body_argument('per_id')
        dic['face_id'] = self.get_body_argument('face_id')
        dic['per_name'] = self.get_body_argument('per_name')
        dic['idcardNum'] = self.get_body_argument('idcardNum')
        dic['img_data'] = self.get_body_argument('img_data')
        dic['idcardper'] = self.get_body_argument('idcardper')
        dic['s_time'] = self.get_body_argument('s_time')
        dic['e_time'] = self.get_body_argument('e_time')
        dic['per_type'] = self.get_body_argument('per_type')
        dic['usr_type'] = self.get_body_argument('usr_type')
        self.application.announce.changeSubject(dic)


# 查询人脸的信息(增加人脸是否成功可由些得到数据与本地数据对比)
class QueryFace(tornado.web.RequestHandler):
    def post(self):
        dic = {}
        dic['version'] = self.get_body_argument('version')
        dic['cmd'] = self.get_body_argument('cmd')
        dic['id'] = self.get_body_argument('id')
        dic['per_id'] = self.get_body_argument('per_id')
        dic['name'] = self.get_body_argument('name')
        self.application.announce.changeSubject(dic)


# 删除注册人员
class DelFace(tornado.web.RequestHandler):
    def post(self):
        dic = {}
        dic['version'] = self.get_body_argument('version')
        dic['cmd'] = self.get_body_argument('cmd')
        dic['type'] = self.get_body_argument('type')
        dic['per_id'] = self.get_body_argument('per_id')
        # dic['ipaddr'] = self.get_body_argument('ipaddr')
        self.application.announce.changeSubject(dic)


# 修改人脸信息
class UpdateFace(tornado.web.RequestHandler):
    def post(self):
        pass


# 设置时间
class SetTime(tornado.web.RequestHandler):
    def post(self):
        pass


# 设置是否开启活体检测
class SetSpoofing(tornado.web.RequestHandler):
    def post(self):
        pass


# 设置戴帽检测
class setAttr(tornado.web.RequestHandler):
    def post(self):
        pass


# 设置语音大小
class setVoiceCFG(tornado.web.RequestHandler):
    def post(self):
        pass


# 设置屏幕睡眠时间
class setSleepTime(tornado.web.RequestHandler):
    def post(self):
        pass


# 设置验证模式 /0：刷脸，1：刷卡，2：刷身份证，3：刷脸+刷卡 4：刷脸+刷身份证，5：刷脸或刷卡，6：刷脸或刷身份证，7：过人开闸
class setRecoMode(tornado.web.RequestHandler):
    def post(self):
        pass


# 设置是否启用未带安全帽禁止通行配置
class setHatPass(tornado.web.RequestHandler):
    def post(self):
        pass


# StatusHandler的处理是异步的
class StatusHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def post(self):
        self.application.announce.register(self.async_callback(self.on_message))
        status = {}
        bo = self.request.body
        ip = self.get_body_argument('ipaddr')
        serialno = self.get_body_argument('serialno')
        last_result = self.get_body_argument('last_result')

        status['ip'] = ip
        status['serialno'] = serialno
        status['last_result'] = last_result
        print(status)

        op = ResultHandle(status)


    def on_message(self, data):
        print('ok')
        self.write(data)
        print(data)
        # 必须要finish 否则服务器会一直阻塞
        self.finish()


class Application(tornado.web.Application):
    """
    """
    def __init__(self):
        """
        """
        self.announce = Announce()
        self.db = Dboperator()
        handlers = [
            (r'/', MainHandler),
            (r'/chat', ChatHandler),
            (r'/addFace', AddFace),
            (r'/delFace', DelFace),
            (r'/queryFace', QueryFace),
            (r'/heartbeat', StatusHandler),
            (r'/getRecordx', RecordHandler),
        ]
        settings = {
            'template_path': 'templates',
            'static_path': 'static',
            'debug': True
        }
        tornado.web.Application.__init__(self, handlers, **settings)


if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = Application()
    server = tornado.httpserver.HTTPServer(app)
    server.listen(8080)
    tornado.ioloop.IOLoop.instance().start()
