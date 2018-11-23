# This example will send a couple of commands to our device, as we would if we
# were using our Phone, or our regular Infrastructure during a product's actual
# usage
#
# The goal of this example is to show you how you can send a network command to
# your devices through the IFTTT communication infrastructure. This example turns on & off a WiFi Smart Socket.
#
# In our particular example, we are only sending a command and not asserting
# anything. Of course this would never be a real world example, it's only for
# educational purposes

# The command is generated through an applet by using a Webhook as a trigger and a compatible eWeLink as an action
# The IFTTT Key can be found on the above link https://ifttt.com/services/maker_webhooks/settings and must be registered as Environment Variable on project's UI settings page



import os
import time
import requests

ifttt_key = os.environ['IFTTT_API_KEY']

def set_request(endpoint):
    headers = {"Content-Type": "application/json"}
    r = requests.post(endpoint, data = '', headers=headers)
    return r.text

def send_command(command):
    endpoint = 'https://maker.ifttt.com/trigger/'+command+'/with/key/'+ifttt_key
    return set_request(endpoint)


def send_network_cmds():
    # send network command to our device
    send_command("turn_on")
    time.sleep(5)
    # send network command to our device
    send_command("turn_off")

if __name__ == "__main__":
    send_network_cmds()
