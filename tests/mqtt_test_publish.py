from time import sleep

import paho.mqtt.client as mqtt


client = mqtt.Client(client_id="mqtt_publish", clean_session=False)
client.connect("pi", 1883, 60)

value = True

while True:
    try:
        response = client.publish(
            "mqtt_events/testin", b"1" if value else b"0")

        if response.rc == mqtt.MQTT_ERR_SUCCESS:
            print('success')
            value = not value
            sleep(3)
        else:
            break
    except KeyboardInterrupt:
        exit(0)
