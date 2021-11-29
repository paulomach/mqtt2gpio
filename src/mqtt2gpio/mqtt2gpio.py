"""Subscribe to topic, write IO and return message on topic."""
import argparse
from time import sleep

import paho.mqtt.client as mqtt
import paho.mqtt.subscribe as subscribe
from gpiozero import LED


def log(message):
    """Log message."""
    print(message)


def publish_gpio_callback(client, topic, payload):
    """Publish to topic."""
    response = client.publish(topic, payload)
    if response.rc != mqtt.MQTT_ERR_SUCCESS:
        client.reconnect()
        sleep(1)
        publish_gpio_callback(client, topic, payload)


def write_gpio_callback(client, userdata, message):
    """Write to GPIO."""
    if message.payload == b'1':
        led.on()
        log('LED ON')
    else:
        led.off()
        log('LED OFF')

    # if led.is_lit else "off")
    publish_gpio_callback(client, args.pubtopic, "on")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='MQTT to GPIO')
    parser.add_argument('-s', '--substopic', type=str, required=True,
                        help='MQTT topic to subscribe to')
    parser.add_argument('-p', '--pubtopic', type=str, required=True,
                        help='MQTT topic to publish to')
    parser.add_argument('-g', '--gpio', type=int, required=True,
                        help='GPIO pin to use')
    parser.add_argument('-b', '--host', type=str, required=True,
                        help='Broker hostname')
    args = parser.parse_args()

    led = LED(args.gpio)

    client = mqtt.Client(client_id="queue2io", clean_session=True)

    client.connect(args.host)

    try:
        subscribe.callback(write_gpio_callback, args.substopic,
                           hostname=args.host).loop_forever()
    except KeyboardInterrupt:
        client.disconnect()
        exit(0)
