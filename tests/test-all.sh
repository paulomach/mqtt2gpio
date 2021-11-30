#!/bin/bash

set -Eeuo pipefail

BROKER=$1
TOPIC_IN="mqtt_events/testin"
TOPIC_OUT="mqtt_events/test"

export GPIOZERO_PIN_FACTORY=mock

python src/mqtt2gpio/mqtt2gpio.py \
    -s ${TOPIC_IN} \
    -p ${TOPIC_OUT} \
    -g 4 \
    -b ${BROKER} &

sleep 2

python tests/mqtt2gpio_test_subscribe.py ${BROKER} ${TOPIC_OUT} &
python tests/mqtt2gpio_test_publish.py ${BROKER} ${TOPIC_IN} &

sleep 10

pkill -e -9 -f mqtt2gpio
