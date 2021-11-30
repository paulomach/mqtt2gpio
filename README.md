# mqtt2gpio

Very crude mqtt to gpio translator.

## Motivation

Personal raspberrypi home automation project.

### Notes

4x power relay shield configuration
* pin 19 - channel 1
* pin 26 - channel 2
* pin 20 - channel 3
* pin 21 - channel 4

# Usage

```shell
mqtt2gpio.py -s <subscribe_topic> -p <publish_topic> -g <io_pin> -b <broker>
```

* subscribe_topic - topic from where events are monitored. Message payload should be byte 0|1, e.g. `b"0"` or `b"1"`
* publish_topic - topic where result is published
* io_pin - io to be written
* broker - mqtt broker address

## Test

Given an accessible mqtt broker, it's possible to test using tox.
(you must first edit your broker address on tox.ini)

```shell
tox -e test
```


# Dependencies

* python>=3.7
* paho-mqtt
* gpio-zero

# References

* [gpiozero](https://gpiozero.readthedocs.io/en/stable/installing.html)
* [paho-mqtt](https://pypi.org/project/paho-mqtt/)
