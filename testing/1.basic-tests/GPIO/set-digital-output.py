# This example will set one of our Testboard's outputs, first to HIGH, and then
# to LOW.
#
# The goal of this example is to show you how you can drive a digital input on
# your device from the Testboard.
#
# In our particular example, we are only setting value and not asserting
# anything. Of course this would never be a real world example, it's only for
# educational purposes

import time
from Spanner import Spanner
from Testboard import Testboard

testboard = Testboard("testboard_name")

# Our Product's Input will be connected the Testboard's Pin D3, making it our 
# Output Pin
OUTPUT_PIN = "D3"

def toggle_digital_output():
    # set PIN state
    testboard.digitalWrite(OUTPUT_PIN, 'HIGH')

    time.sleep(2)

    testboard.digitalWrite(OUTPUT_PIN, 'LOW')

if __name__ == "__main__":
    toggle_digital_output()
