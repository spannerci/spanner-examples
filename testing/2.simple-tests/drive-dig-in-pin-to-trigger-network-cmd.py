# This example will toggle one of our device's inputs, which will respond
# accordingly by sending a network command, to showcase a product's actual usage.
#
# In this particular example the device we are testing is a Water Flooding
# Alarm, which responds by sending an "alarm_triggered" command with a value of
# "water" when the water flooding sensor pin is triggered.

# The goal of this example is to show you how you can receive network commands
# to your devices though Particle events, after
# setting one of the device's environmental inputs.
#
# This is one real world example of a very simple functional test you would run
# for your devices.

import os
import sys
import time
import pytest
from SpannerTestboard import SpannerTestboard

testboard = SpannerTestboard("testboard_name")

# Our Product's Input will be connected the Testboard's Pin D3, making it our
# Output Pin
OUTPUT_PIN = "D3"

particle_token = os.environ['SPN_PARTICLE_TOKEN']

def with_urllib3(url):
    """Get a streaming response for the given event feed using urllib3."""
    import urllib3
    http = urllib3.PoolManager()
    return http.request('GET', url, preload_content=False)


def test_test_raise_flooding_alarm():
    # set PIN state
    testboard.digitalWrite(OUTPUT_PIN, HIGH)

    time.sleep(2)

    url = 'https://api.particle.io/v1/devices/events?access_token='+particle_token
    response = with_urllib3(url)  # or with_requests(url)
    client = sseclient.SSEClient(response)
        # acts like a while loop
    for event in client.events():
        data = json.loads(event.data)
        # e.g data['data'] = 'alarm'
        command = data['data']
        # Double check the name of the command
        assert "alarm_triggered" == command.name
        assert "water_flooding" == command.value

        sys.exit(0)
