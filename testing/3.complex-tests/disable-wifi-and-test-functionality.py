# This example will test the functionality of our device when we shut down the
# WiFi network. That's important because it's one of the core functionalities
# of our device, and it's one of the unique environmental inputs that our
# testing infrastructure allows when testing a product.
#
# In this particular example the device we are testing is a Smart Switch, which
# responds by toggling one of its pins On of Off whenever the user manually
# presses the button on the device..
#
# Our Testboard is acting as the Access Point that provides network connectivity
# to our device. So by turning off the Access Point our device should get into
# Network Discovery mode. However, it should still operate properly.
#
# The goal of this example is to show you how you can control more exotic (but
# absolutely critical) "inputs" in a test. Besides sensors, inputs and outputs,
# the network connectivity is an important part of the environment that needs to
# be mocked/tested in a functional test.
#
# This is one real world example of a complex, but realistic, functional test
# you would run for your devices.
# 
# Note: To use this example a special Testboard that can operate in Access Point
# mode is required. 

import time
import sys
from Spanner import Spanner
from Testboard import Testboard

testboard = Testboard("testboard_name")

# Our device's Output Pin will be connected to the Testboard's D7, making it our
# Input Pin
INPUT_PIN = "D7"

# Our Product's Input will be connected the Testboard's Pin D3, making it our
# Output Pin
OUTPUT_PIN = "D3"

def initialize_switch_off():
    # check PIN state
    switch_status = testboard.digitalRead(INPUT_PIN)

    # If the switch is currently on, toggle the device's button (through our
    # Testboards OUTPUT) 100 miliseconds, simulating a user input.
    if(switch_status == 1):
        testboard.toggle(OUTPUT_PIN, 100)

    time.sleep(2)

    # check PIN state again
    switch_status = testboard.digitalRead(INPUT_PIN)

    # If the switch is still on, we have some kind of problem so there's no
    # point in running our tests. So we are exiting
    if(switch_status == 1):
        sys.exit()

def wififoff_toggle_button_toggle_switch():
    # We are turning off the Access Point, so our device will now be in Network
    # Discovery mode. 
    testboard.wifiOff()
    time.sleep(10)

    # check PIN state, make sure it's OFF
    switch_status = testboard.digitalRead(INPUT_PIN)
    spanner.assertFalse(switch_status)

    # Simulate a real-life button press. We toggle the device's button (through
    # our Testboards OUTPUT) 100 miliseconds
    testboard.toggle(OUTPUT_PIN, 100)

    # check PIN state, make sure it's now ON
    switch_status = testboard.digitalRead(INPUT_PIN)
    spanner.assertTrue(switch_status)

    # Simulate a real-life button press. We toggle the device's button (through
    # our Testboards OUTPUT) 100 miliseconds
    testboard.toggle(OUTPUT_PIN, 100)

    # check PIN state, make sure it's now OFF again
    switch_status = testboard.digitalRead(INPUT_PIN)
    spanner.assertFalse(switch_status)


if __name__ == "__main__":

    initialize_switch_off()

    time.sleep(2)

    wififoff_toggle_button_toggle_switch()
