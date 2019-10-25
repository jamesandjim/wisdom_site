import paho.mqtt.client as mqtt

HOST = "192.168.0.100"
PORT = 1883


def on_connect(client, userdata, flags, rc):
    # client.subscribe("face/9a136d1b-8e0003fe/response")
    client.subscribe("face/response")

    # client.subscribe("will/9a136d1b-8e0003fe/response")
    # client.subscribe("online/response")


def on_message(client, userdata, msg):
    print(msg.topic+" "+msg.payload.decode('utf-8'))
    print(msg.payload.decode('utf-8'))


def test():
    client = mqtt.Client()    # 可能需要设置ClientId
    client.username_pw_set("admin", "public")  # 必须设置，否则会返回「Connected with result code 4」
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(HOST, PORT, 60)
    client.loop_forever()


if __name__ == '__main__':
    test()
