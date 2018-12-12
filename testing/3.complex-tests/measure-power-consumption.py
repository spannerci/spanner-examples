# This example will make sure our device meets some specifications or thresholds
# that we want to be true for every future version of our code. In other words,
# we wanna make sure that these are always tested and we never end up exceeding
# them.
#
# In this particular example this is a battery-powered device and we want to
# make sure that any chances we make in our algorithm (such as functionality, or
# measuring frequency) will not result in us reducing the battery life below the
# advertised on.

# Our Testboard is connected with a Power Control circuit that allows us to turn
# the Power to our device On and Off programmatically. It's also connected to a
#power consumption measurement circuit that allow us to measure the total power
#consumption in a given time period.

# The goal of this example is to show you how you can run much more advanced
# tests than environmental mocks, inputs and outputs. Power Consumption is,
# after all, an "output" or "functionality" of our devices, and we want to make
# sure that functionality is tested.

# This is one real world example of a complex, but realistic, functional test
# you would run for your devices.

import time
import Spanner
from Testboard import Testboard

testboard = Testboard("testboard_name")
# Our Testboard's D3 Pin is connected to a power switching circuit that controls
# the power going to the device. When we toggle it HIGH, the device will be
# powered, when LOW, the device will shut down
OUTPUT_PIN = "D3"

def measure_power_consumption():

    # Turn the device off
    testboard.digitalWrite(OUTPUT_PIN, "LOW");

    # Wait for a while for it to shut down
    time.sleep(10)

    # Turn the device back on
    testboard.digitalWrite(OUTPUT_PIN, "HIGH");

    # The device runs some initialization actions in the beginning, which are
    # not indicative of the true power consumption. Therefore we wait for a
    # while for the initial conditions to pass
    time.sleep(90)

    # Start measuring power consumption
    testboard.startPowerMeasurement()

    # Measure for 5 minutes
    time.sleep(5*60)

    # Stop measuring power consumption
    testboard.stopPowerMeasurement()

    # Make sure the total power consumption didn't exceed 100mAh. The
    # measuredPowerConsumption() will return the total power consumption
    # measured in the measuring period, in mAh. Then we use the assertLessThan()
    # function to assert that this is less than the target value of 100.
    Spanner.assertLessThan(100, testboard.measuredPowerConsumption())

if __name__ == "__main__":
    measure_power_consumption()
