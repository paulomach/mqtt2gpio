import sys

import paho.mqtt.subscribe as subscribe

broker = sys.argv[1]
topic = sys.argv[2]


def callback(client, userdata, message):
    print("message received ", str(message.payload.decode("utf-8")))


try:
    subscribe.callback(callback, topic,
                       hostname=broker).loop_forever()
except KeyboardInterrupt:
    exit(0)
