# This example will make sure our device meets some specifications or thresholds
# that we want to be true for every future version of our code. In other words,
# we wanna make sure that these are always tested and we never end up exceeding
# them.
#
# In this particular example this is a battery-powered device and we want to
# make sure that any chances we make in our algorithm (such as functionality, or
# measuring frequency) will not result in us reducing the battery life below the
# advertised on.
#
# Our Testboard is connected with a coulomb counter module (LTC4150)
# https://learn.sparkfun.com/tutorials/ltc4150-coulomb-counter-hookup-guide
# that allow us to measure the total power consumption in a given time period.
#
# Both tests assume an average consumption of 55mA with a 20mA threshold, due
# to consumption variations during the device's power cycles. With this in your
# mind, you can alter this test accordingly to suit your product's needs.
#

import time

from SpannerTestboard import SpannerTestboard

INT_PIN = "A2"
testboard = SpannerTestboard("testboard_name")


def teardown_module(module):
    # Clear any pending interrupts
    testboard.stopInterruptCounter(INT_PIN)


# This is the first method of calculating power consumption and is encouraged to
# be used for precise measurements. The measuring interval (period_ms) is given
# as an argument in ms in which the interrupt counter is used to count (ticks)
# from the LTC4150 module.
#
# Other configuration arguments are the interrupt pin (INT_PIN), which is the pin the
# LTC4150 module is connected to the testboard, the input mode (i.e. INPUT, NPUT_PULLUP,
# INPUT_PULLDOWN) and finally the interrupt mode (i.e. CHANGE, RISING, FALLING).

def test_consumption_period():
    period_ms = 60 * 1000
    # Start the interrupt count period
    counter = testboard.startInterruptCounterPeriod(
        INT_PIN,
        testboard.PinMode.INPUT,
        testboard.InterruptMode.FALLING,
        period_ms
    )
    assert counter >= 0

    # Calculate consumption
    mA = (counter * 614.4) / (period_ms / 1000)
    assert abs(mA - 55) < 20


# This method referred as `dynamic`, is a more flexible approach of the first, since
# the tests execution is not halted, more suitable for longer and more complex tests.
# That is because you can initiate the interrupt counter, and perform other tasks which can trigger
# actions to your product, while you keep getting interrupts for your product's power
# on-going consumption measurements.

def test_consumption_dynamic():
    period = 60
    testboard.startInterruptCounter(
        INT_PIN,
        testboard.PinMode.INPUT,
        testboard.InterruptMode.FALLING,
    )
    # do whatever
    time.sleep(period)

    # Read the interrupt counter
    counter = testboard.stopInterruptCounter(INT_PIN)
    assert counter >= 0

    # Calculate consumption
    mA = (counter * 614.4) / period
    assert abs(mA - 55) < 20
