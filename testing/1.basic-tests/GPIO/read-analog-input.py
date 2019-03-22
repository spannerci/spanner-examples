# This example will test two of our Product's Analog outputs, and make sure one
# is lower than a particular threshold, and the other one higher.
#
# The goal of this example is to show you how you can read a simple analog
# output from your device, and how you can make comparative assertions.
#
# In our particular example, we expect the pin we're connecting to our
# Testboard's A0 to be always less than a threshold value, and the pin we're
# connecting to our Testboard's A4 to be always greater than a threshold value.
# Of course this would never be a real world example, it's only for educational
# purposes
#
# If you want to replicate this setup, you can use our Particle Photon Testboard
# and connect the A0 pin to 3V3, and the A4 pin to GND.

import time
import pytest
from SpannerTestboard import SpannerTestboard

testboard = SpannerTestboard("testboard_name")
# Our device's 1st Analog Output Pin will be connected to the Testboard's A0,
# making it our Input Pin 1
INPUT_PIN_1 = "A0"
# Our device's 2nd Analog Output Pin will be connected to the Testboard's A4,
# making it our Input Pin 2
INPUT_PIN_2 = "A4"

def test_validate_analog_input_greater():
    # Check PIN state
    # analogRead will give us a value between 0 to 4095, corresponding to a
    # 0-3V3 range.
    value = testboard.analogRead(INPUT_PIN_1)

    # Let's say we want to to make sure the voltage is greater than 1.5V. Given
    # the mapping of 0-3.3V to a value of 0-4096, that means the value we have
    # should be higher than aproximately 1861. For the sake of simplicity and
    # because of possible fluctuations in the values, we'll test with 1800,
    # which is aprox. 1.45V.
    # NOTICE: We could also have used analogReadVoltage() as we do in the next
    # example.
    assert value > 1800

def test_validate_analog_input_less():
    # Check PIN state
    # In this example, we use analogReadVoltage() which gives us a Voltage value
    # directly, without having to care about the ADC converter. However, keep in
    # mind that this value could be slightly less accurate, and given that it's
    # a float it's not the best fit for checking Equality. Still, it's good
    # enough for most purposes.
    value = testboard.analogReadVoltage(INPUT_PIN_2)

    assert value < 2.0