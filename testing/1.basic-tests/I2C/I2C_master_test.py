# This example will show case our Product's I2C function capabilities
#
# The goal of this example is to show you how you can mock a communication protocol
# over I2C, and specifically act as the master device on the bus. For this example,
# the LIS3DH 3axis Accelerometer was used, from Adafruit (http://adafru.it/2809).
# Pin layout and documentation of this chip can be found at the link above.
#
# I2C interface is available via the Testboard's SCL => D1, SDA => D0 pins. If you want
# to replicate this setup, connect the SCL, SDA pins of the LIS3DH to the D1, D0 respectively,
# while using the 3V3 output pin of the Testboard to power up the LIS3DH. Finally
# leave the SD0 pin open and ground the chip using the Tesboard's GND pin.
#
# The address of the LIS3DH, would be 0x18, by initiating the connection on
# CLK=100KHz we can access the data by sending the 0xa8 byte as described in the
# documentation of this chip. The values of the 3axis are received in little-endian format
# and represent a singed 16bit integer. Thus by reading 6 Bytes we can get a complete
# reading of the accelerometer's x-y-z axis data. Please note, that to retrieve this data
# you should supply the withResults = True flag, when executing your procedure. The data
# would be contained in a bytearray python object.
#
# Reading and writing more than 32Bytes at a time, would be handled internally
# by the testboard which would preserve the connection open by utilizing the
# restart signal and preventing other master devices from acquiring the bus.
#
import pytest
from SpannerTestboard import SpannerTestboard

testboard = SpannerTestboard("testboard_name")

def test_z_axis_check():

    # Start the I2C bus with CLK=100KHz
    my_procedure = testboard.createProcedure('I2C-Master') \
        .setSpeed(100000) \
        .begin()

    # Write to address => 0x18, data => 0xa8
    # Read from address => 0x18, number of bytes to read => 6
    for _ in range(3):
        my_procedure \
            .write(0x18, bytearray([0xa8])) \
            .read(0x18, 6) \
            .doWait(1000)

    # Execute the mock function with results
    exit_code, results = my_procedure.run(withResults=True)

    for result in results:
        x = int.from_bytes(result[0:2], byteorder='little', signed=True)
        y = int.from_bytes(result[2:4], byteorder='little', signed=True)
        z = int.from_bytes(result[4:6], byteorder='little', signed=True)
        print("X: %.2f, Y: %.2f, Z: %.2f" % (x, y, z))
        assert abs(z - 8000) < 100
