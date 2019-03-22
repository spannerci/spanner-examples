# This example will test two of our Product's outputs, to make sure that one is
# high, and the other one is low.
#
# The goal of this example is to show you how you can read a simple digital
# output from your device, and how you can assert boolean values.
#
# In our particular example, we expect the pin we're connecting to our
# Testboard's D5 to be always LOW, and the pin we're connecting to our
# Testboard's D7 to be always HIGH. Of course this would never be a real world
# example, it's only for educational purposes
#
# If you want to replicate this setup, you can use our Particle Photon Testboard
# and connect the D5 pin to GND, and the D7 pin to 3V3.

import time
import pytest
from SpannerTestboard import SpannerTestboard

testboard = SpannerTestboard("testboard_name")

# Our device's 1st Output Pin will be connected to the Testboard's D7, making it
# our Input Pin 1
INPUT_PIN_1 = "D7"

# Our device's 2nd Output Pin will be connected to the Testboard's D5, making it
# our Input Pin 2
INPUT_PIN_2 = "D5"

def test_validate_digital_input_high():
    # check PIN state
    value = testboard.digitalRead(INPUT_PIN_1)
    
    assert value != 0

def test_validate_digital_input_low():
    # check PIN state
    value = testboard.digitalRead(INPUT_PIN_2)

    assert value == 0
