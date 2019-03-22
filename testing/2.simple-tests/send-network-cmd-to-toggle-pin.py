# This example will send a couple of commands to our device, which will respond
# accordingly, to showcase a product's actual usage.
#
# In this particular example the device we are testing is a Smart Switch, which
# responds by toggling one of its pins On of Off based on the command.

# The goal of this example is to show you how you can send a network commands to
# your devices through Particle events, and read a
# device's output's to verify its response, using our Testboard.
#
# This is one real world example of a very simple functional test you would run
# for your devices.

# The command is generated through an applet by using a Webhook as a trigger and a compatible eWeLink as an action
# The IFTTT Key can be found on the above link https://ifttt.com/services/maker_webhooks/settings and must be registered as Environment Variable on project's UI settings page

import time
import os
import requests
import pytest
from SpannerTestboard import SpannerTestboard

ifttt_key = os.environ['IFTTT_API_KEY']

testboard = SpannerTestboard("testboard_name")

# Our device's Output Pin will be connected to the Testboard's D7, making it our
# Input Pin
INPUT_PIN = "D7"

def set_request(endpoint):
    headers = {"Content-Type": "application/json"}
    r = requests.post(endpoint, data = '', headers=headers)
    return r.text

def send_command(command):
    endpoint = 'https://maker.ifttt.com/trigger/'+command+'/with/key/'+ifttt_key
    return set_request(endpoint)

def test_switch_on_network_cmd():
    # send network command to our device
    send_command("turn_on")
    time.sleep(2)

    # check PIN state
    value = testboard.digitalRead(INPUT_PIN)
    assert value !=0

def test_switch_off_network_cmd():
    # send network command to our device
    send_command("turn_off")
    time.sleep(2)

    # check PIN state
    value = testboard.digitalRead(INPUT_PIN)
    assert value == 0
