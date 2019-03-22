# This example will show case our Product's I2C function capabilities
#
# The goal of this example is to show you how you can mock a communication protocol
# over I2C, and specifically act as a slave device on the bus. Thus, you can test
# your product's interface with peripheral devices, by mocking them. Each write command would
# be performed when a master device on the bus requests for data on the slave's address.
# Defining which data to write is up to you, and the length of these is limited to
# 32Bytes per write command.
#
# Please note that the 'I2C-Slave' interface is currently limited as opposed to
# the master interface, and cannot support `read` commands. Other than that,
# the slave device can make use of the stretchClock(False) command to disable
# the I2C clock stretching, before joining the bus.
#
# In the example bellow, the Testboard join's the bus, on the 0x20 address, and
# would finish execution when all of its three byte buffers are read by a master device
# or when the provided timeout has elapsed. The slave device, flushes all incoming
# data, so there is no need to double think on what to send before reading.
# Failed writes, or execution timeouts would result in non-zero exit codes.
# Please note that the execution of the procedure is blocking, thus you may need to
# consider, spawning a thread or a process to initialize the Testboard, before
# invoking your product's tests.
#
import pytest
from SpannerTestboard import SpannerTestboard

testboard = SpannerTestboard("testboard_name")

def test_i2c_slave_device():

    # Join the bus on address 0x20 with CLK=100KHz
    my_procedure = testboard.createProcedure('I2C-Slave') \
        .setSpeed(100000) \
        .begin(0x20) \
        .write(bytearray([10] * 6)) \
        .write(bytearray([11] * 6)) \
        .write(bytearray([12] * 6))

    # Timeout of 50 seconds
    exit_code = my_procedure.run(timeout=50000)
    assert exit_code == 0