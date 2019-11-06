class Info:
    result = {}
    callbacks = []

    def register(self, callback):

        self.callbacks.append(callback)

    def callbacksHeper(self, callback):
        callback(Info.result)

    def notifyCallbacks(self):
        for callback in self.callbacks:
            self.callbacksHeper(callback)
        self.callbacks = []

    def sendMsg(self, msg):
        self.result = msg
        self.notifyCallbacks()

