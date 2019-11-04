import tornado.web
import tornado.httpserver
import tornado.ioloop
import tornado.options

from uuid import uuid4
import json


# 服务器端保存的字符串
class Announce():
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

        print(bo3)


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


# StatusHandler的处理是异步的
class StatusHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def post(self):
        bo = self.request.body
        ip = self.get_body_argument('ipaddr')
        print(bo.decode('utf-8'))

        self.application.announce.register(self.async_callback(self.on_message))
        print('%s 相机正在联接' % ip)

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
        handlers = [
            (r'/', MainHandler),
            (r'/chat', ChatHandler),
            (r'/addFace', AddFace),
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