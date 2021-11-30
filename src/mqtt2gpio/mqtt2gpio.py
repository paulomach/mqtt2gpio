"""Subscribe to topic, write IO and return message on topic."""
import argparse
import logging
import sys
from time import sleep

import paho.mqtt.client as mqtt
import paho.mqtt.subscribe as subscribe
from gpiozero import LED

logging.basicConfig(stream=sys.stdout, format='%(asctime)s:%(levelname)s:%(message)s')
logger = logging.getLogger()


def log(message: str):
    """Log message.

    Args:
        message: message to log
    """
    logger.info(message)


def publish_gpio2topic(client, topic, payload):
    """Publish to topic.

    Args:
        client: mqtt client connection instance
        topic: topic for publishing
        payload: message payload
    """
    response = client.publish(topic, payload)
    if response.rc != mqtt.MQTT_ERR_SUCCESS:
        client.reconnect()
        sleep(1)
        publish_gpio2topic(client, topic, payload)


def write_gpio_callback(client, instance, message):
    """Write to GPIO.

    Args:
        client: mqtt client connection
        instance: Mqtt2gpio object
        message: binary message
    """
    if message.payload == b'1':
        instance.led.on()
        log('LED ON')
    else:
        instance.led.off()
        log('LED OFF')

    publish_gpio2topic(client, instance.args.pubtopic, "on" if instance.led.is_lit else "off")


class Mqtt2gpio():
    """Mqtt2gpio translator class."""

    def __init__(self):
        """Parameter initialization from cmdline."""
        parser = argparse.ArgumentParser(description='MQTT to GPIO')
        parser.add_argument('-s', '--substopic', type=str, required=True,
                            help='MQTT topic to subscribe to')
        parser.add_argument('-p', '--pubtopic', type=str, required=True,
                            help='MQTT topic to publish to')
        parser.add_argument('-g', '--gpio', type=int, required=True,
                            help='GPIO pin to use')
        parser.add_argument('-b', '--host', type=str, required=True,
                            help='Broker hostname')
        try:
            self.args = parser.parse_args()
        except argparse.ArgumentError:
            parser.print_help()
            exit(0)

        self.client = mqtt.Client(client_id="queue2io", clean_session=True)

    def run(self):
        """Execute IO connection and subscribe loop."""
        self.led = LED(self.args.gpio)
        self.client.connect(self.args.host)

        try:
            subscribe.callback(write_gpio_callback, self.args.substopic,
                               hostname=self.args.host, userdata=self).loop_forever()
        except KeyboardInterrupt:
            self.client.disconnect()
            exit(0)


def main():
    """Script entrypoint."""
    logger.setLevel(logging.INFO)

    m = Mqtt2gpio()
    m.run()


if __name__ == '__main__':
    main()
