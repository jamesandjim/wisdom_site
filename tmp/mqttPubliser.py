# -*- coding: utf-8 -*-

import paho.mqtt.client as mqtt
from io import BytesIO
import json

MQTTHOST = "192.168.0.100"
MQTTPORT = 1883
mqttClient = mqtt.Client()


# 连接MQTT服务器
def on_mqtt_connect():
    mqttClient.connect(MQTTHOST, MQTTPORT, 60)
    mqttClient.loop_start()


# publish 消息
def on_publish(topic, payload, qos):
    mqttClient.publish(topic, payload, qos)



# 消息处理函数
def on_message_come(lient, userdata, msg):
    content0 = msg.payload

    j = msg.payload

    # x = json.loads(msg.payload, encoding='utf-8')
    # print(x)
    print(j)
    print(type(j))
    st = str(j, 'utf-8')
    f = BytesIO(j)
    f.readline()

    print(f)


# subscribe 消息
def on_subscribe():
    mqttClient.subscribe("face/response", 2)
    mqttClient.on_message = on_message_come  # 消息到来处理函数


def main():
    on_mqtt_connect()
    payload = {
        "cmd":"face_search",
        "cmd_id":"",
        "client_id":"mqttjs_1a5662588c"
    }
    on_publish("face/request", json.dumps(payload), 1)
    on_subscribe()
    while True:
        pass


if __name__ == '__main__':
    main()

