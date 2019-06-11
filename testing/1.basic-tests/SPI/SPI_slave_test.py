# This example will show case our Product's SPI function capabilities
#
# The goal of this example is to show you how you can mock a communication protocol
# over SPI, and specifically act as the slave device on the bus. Please note that currently
# only the `Photon` Testboards support slave mode. For this example, a slave testboard is
# connected with the master device (which can represent your product).
#
# For this example a simple string message is sent from the slave to the master. The master would
# first send some command bytes which the slave will `assertRead` them (using a timeout of 10secs).
# If the master hasn't send the required data in that period the slave will terminate with failure.
# After the slave read the command Bytes he writes back to the master the `MESSAGE_TEXT`. Again here,
# the write command has a timeout, which requires of the master to read the data, and prevents the slave
# from blocking.
#

from multiprocessing import Process
from time import sleep

from Mocks import SPI
from SpannerTestboard import SpannerTestboard

mode = SPI.DATA_MODE.MODE0  # MODE 0
bit_order = SPI.BIT_ORDER.MSBFIRST  # MSB First
frequency = 200000  # Speed = 200KHz

master = SpannerTestboard("master_testboard")
slave = SpannerTestboard("slave_testboard")

MESSAGE_TEXT = "Hello Master ;)"
CMD_CODE = bytearray([0x26, 0x46])


def start_slave():
    # Start the slave, using A2 as the SE pin
    exit_code, results = slave.createProcedure('SPI-Slave'). \
        setBitOrder(bit_order). \
        setClockSpeed(frequency). \
        setDataMode(mode). \
        begin('A2'). \
        assertRead(CMD_CODE, timeout=10000). \
        write(bytearray([ord(c) for c in MESSAGE_TEXT]), timeout=3000). \
        run(withResults=True)

    # Assert on valid execution of the slave or else print the received command
    assert exit_code == 0, results[0]


def test_master_slave_communication():
    ss_pin = 'D7'
    # Set the Slave select pin to HIGH (disable slaves on bus)
    master.digitalWrite(ss_pin, 'HIGH')

    # Start the slave process
    p = Process(target=start_slave)
    p.start()
    sleep(2)

    # Start the master procedure
    exit_status, results_bytearray = master.createProcedure('SPI-Master'). \
        setBitOrder(bit_order). \
        setClockSpeed(frequency). \
        setDataMode(mode). \
        begin(ss_pin). \
        enableSlave(). \
        write(CMD_CODE). \
        doWait(1). \
        read(len(MESSAGE_TEXT)). \
        disableSlave(). \
        run(withResults=True)

    # Wait for the slave process to terminate
    p.join()

    # Check the results we got back from the slave device
    assert exit_status == 0, "Master finished with errors"
    assert (results_bytearray[0]).decode('ascii') == MESSAGE_TEXT, "Message text mismatch"
