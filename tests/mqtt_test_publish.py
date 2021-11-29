import paho.mqtt.client as mqtt

client = mqtt.Client(client_id="mqtt_publish", clean_session=False)


client.connect("krusty", 1883, 60)


response = client.publish("mqtt_events/testin", b"0")

if response.rc == mqtt.MQTT_ERR_SUCCESS:
    print('sucess')