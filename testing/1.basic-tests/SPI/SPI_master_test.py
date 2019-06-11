# This example will show case our Product's SPI function capabilities
#
# The goal of this example is to show you how you can mock a communication protocol
# over SPI, and specifically act as the master device on the bus. For this example,
# the LIS3DH 3axis Accelerometer was used, from Adafruit (http://adafru.it/2809).
# Pin layout and documentation of this chip can be found at the link above.
#
# This example utilizes the SPI interface of the Testboard to set up the sensor
# module and access the raw 3d axis signals. The SPI wiring for this example is:
#  SCK -> SCL - This is the SPI Clock pin.
#  MO  -> SDA - This is the Serial Data In / Master Out Slave In pin, for data sent from your processor to the LIS3DH.
#  MI  -> SDO - This is the Serial Data Out / Master In Slave Out pin, for data sent from the LIS3DH to your processor.
#               It's 3.3V logic level out.
#  D7  -> CS  - This is the Chip Select pin.
#  3V3 -> Vin - This is the 3.3V power supply for the chip.
#  GND -> GND - This is the ground of the chip.
#
# The examples is composed of two parts the actual connection and setup of the sensor (write register part) and
# later on with the data access (read axis). Please note that setting up the sensor is only required once,
# as long the module keeps having power on.
#
from Mocks import SPI
from SpannerTestboard import SpannerTestboard

testboard = SpannerTestboard("testboard_name")


def write_register(procedure, address, value):
    """ Sends the config address byte and the value to the slave device. """
    return procedure. \
        enableSlave(). \
        write(bytearray([address & ~0x80, value])). \
        disableSlave()


def read_axis_raw(procedure):
    """ Sends the command byte for reading, and reads 6 bytes of axis values
        (2 bytes per axis) from the slave device. """
    return procedure. \
        enableSlave(). \
        write(bytearray([0x28 | 0x80 | 0x40])). \
        read(6). \
        disableSlave()


def test_z_axis():
    """ Checks if the z axis is between a confidence threshold. """
    # Setup the SPI BUS, with CS = D7, MSB first bit order,
    # clock speed set to 500KHz and SPI DATA MODE to MODE0
    my_procedure = testboard.createProcedure('SPI-Master'). \
        begin('D7'). \
        setBitOrder(SPI.BIT_ORDER.MSBFIRST). \
        setClockSpeed(500000). \
        setDataMode(SPI.DATA_MODE.MODE0)

    # Enable all axes, normal mode
    my_procedure = write_register(my_procedure, 0x20, 0x07)
    # Set data rate to 400Hz
    my_procedure = write_register(my_procedure, 0x20, 0x77)
    # High res & BDU enabled
    my_procedure = write_register(my_procedure, 0x23, 0x88)
    # DRDY on INT1
    my_procedure = write_register(my_procedure, 0x22, 0x10)
    # Enable ADCs
    my_procedure = write_register(my_procedure, 0x1F, 0x80)

    for _ in range(3):
        my_procedure = read_axis_raw(my_procedure).doWait(200)

    exit_code, results = my_procedure.run(withResults=True)

    for result in results:
        x = int.from_bytes(result[0:2], byteorder='little', signed=True)
        y = int.from_bytes(result[2:4], byteorder='little', signed=True)
        z = int.from_bytes(result[4:6], byteorder='little', signed=True)
        print("X: %.2f, Y: %.2f, Z: %.2f" % (x, y, z))
        assert abs(z - 16200) < 500
