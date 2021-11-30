import paho.mqtt.subscribe as subscribe


def callback(client, userdata, message):
    print("message received ", str(message.payload.decode("utf-8")))


try:
    subscribe.callback(callback, "mqtt_events/test",
                       hostname="pi").loop_forever()
except KeyboardInterrupt:
    exit(0)
