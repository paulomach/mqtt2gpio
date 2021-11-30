import sys
from time import sleep

import paho.mqtt.client as mqtt

broker = sys.argv[1]
topic = sys.argv[2]

client = mqtt.Client(client_id="mqtt_publish", clean_session=False)
client.connect(broker, 1883, 60)

value = True

while True:
    try:
        response = client.publish(
            topic, b"1" if value else b"0")

        if response.rc == mqtt.MQTT_ERR_SUCCESS:
            print(f"message published {'on' if value else 'off'}")
            value = not value
            sleep(3)
        else:
            break
    except KeyboardInterrupt:
        exit(0)
