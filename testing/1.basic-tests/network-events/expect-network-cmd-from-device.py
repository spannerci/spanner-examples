# This example will expect a command from our device, as it should send during
# a product's actual usage
#
# The goal of this example is to show you how you can expect a network command
# from your devices.
#
# In our particular example, we are only wait for a "heartbeat" command
# through Particle events.
# Of course this would never be a real world example, it's only for
# educational purposes

import time
import json
import pprint
import sseclient
import os
import sys
from Spanner import Spanner

particle_token = os.environ['SPN_PARTICLE_TOKEN']

def with_urllib3(url):
    """Get a streaming response for the given event feed using urllib3."""
    import urllib3
    http = urllib3.PoolManager()
    return http.request('GET', url, preload_content=False)

def expect_network_cmd():

    url = 'https://api.particle.io/v1/devices/events?access_token='+particle_token
    response = with_urllib3(url)  # or with_requests(url)
    client = sseclient.SSEClient(response)
    # acts like a while loop
    for event in client.events():
        data = json.loads(event.data)
        # e.g data['data'] = 'heartbeat'
        # when event arrives fire spanner.assertEqual
        spanner.assertEqual("heartbeat", data['data'])
        sys.exit(0)


if __name__ == "__main__":

    expect_network_cmd()
