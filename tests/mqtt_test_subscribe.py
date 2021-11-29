import paho.mqtt.subscribe as subscribe


def callback(client, userdata, message):
    print("message received ", str(message.payload.decode("utf-8")))


subscribe.callback(callback, "mqtt_events/test",
                   hostname="krusty").loop_forever()
