# This example will show case our Product's Mock function capabilities over UART
#
# The goal of this example is to show you how you can mock a communication protocol
# over UART. Specifically we implemented a simple character counter. The testboard
# awaits for the "ready\n" keyword to initiate the sending process to your device,
# whereas your device starts counting the incoming characters, until the "\n" char
# is read. The device responds with the character count which serves as our acknowledgement.
# Finally, you can assert on the string's length and send back the results to Spanner.
#
# If you want to replicate this setup, serial interface is available via the
# Testboard's TX and RX pins. To use them to communicate with your Product,
# connect the TX pin to your device's RX pin, the RX to your device's TX pin,
# and the ground to your device's ground.
#
# Please take into account that the voltage levels on these pins operate at 0V to
# 3.3V and should not be connected directly to a computer's RS232 serial port which
# operates at +/- 12V and will damage the Testboard.
#
# Also note that for the serial channel configuration, it is possible to specify
# the baud rate, the number of data bits, stop bits, parity, flow control and other
# settings.
#

from Testboard import Testboard
import Spanner

testboard = Testboard("testboard_name")

LOREM = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin dictum, nulla nec dictum mattis, sem tellus commodo sem, quis faucibus mauris lectus sed sapien. Duis lobortis lacus tellus, at rhoncus tellus pharetra eu. Quisque semper nisl dolor. Donec consequat mauris sit amet ante pulvinar scelerisque. Proin eu interdum augue. Nam vitae neque quis diam lobortis semper. Proin ut maximus augue.Vivamus elementum neque a lacinia fermentum. Morbi ut maximus magna, eget consectetur purus. Vestibulum ut sodales magna. Interdum et malesuada fames ac ante ipsum primis in faucibus. Phasellus vehicula metus sit amet urna finibus, vel mattis est pharetra. Praesent sed est nulla. Suspendisse pretium blandit felis id pretium. Suspendisse et pretium nulla.Vivamus nisi lorem, commodo id vulputate sed, feugiat et erat. Pellentesque massa sem, interdum non semper vitae, condimentum at augue. Vivamus sit amet convallis urna, vitae mattis arcu. Proin maximus risus in lectus auctor mattis. Proin tempor fermentum vestibulum. Ut sit amet tempus elit, et bibendum eros. Quisque pellentesque ipsum non porta interdum. Aliquam nisl est, aliquet eu tortor eget, pulvinar pulvinar magna. Donec eu purus gravida, lobortis dolor in, lobortis mi. Donec pharetra semper nibh, non eleifend risus aliquam nec.Ut tincidunt, massa finibus vulputate consectetur, quam augue luctus lacus, elementum bibendum risus leo vel velit. Morbi congue velit ac mollis sollicitudin. Integer at vestibulum justo. Vestibulum in gravida purus. Pellentesque eleifend dui quis consectetur rutrum. In faucibus in metus vel tempus. Praesent quis justo tortor. Pellentesque non ornare purus. Phasellus lacus tortor, pharetra eu facilisis in, porta vulputate mi. Suspendisse faucibus fringilla felis, vel sollicitudin eros auctor eget. Aenean auctor vitae ligula non aliquet. Sed eleifend quam velit, a eleifend tortor accumsan vel.Cras euismod, tortor eget ullamcorper sollicitudin, metus erat fermentum ex, et dapibus ipsum sapien a nisl. Cras nec leo porta, congue nisi vel turpis duis."""


def chunks(data, chunk_size):
    for i in range(0, len(data), chunk_size):
        yield data[i:i + chunk_size]


def char_count_mock():
    Serial = Testboard.Serial
    my_procedure = testboard.createProcedure('UART').\
        setup(9600, Serial.DATA_BITS_8 | Serial.STOP_BITS_1 | Serial.PARITY_NO).\
        doAssertSerialRead('ready\n').\
        doWait(1000)


    # Send the dummy text
    for piece in chunks(LOREM, my_procedure.MAX_PAYLOAD_LEN):
        my_procedure.doSerialWrite(piece)

    # Assert read on the text lengths
    my_procedure.doSerialWrite('\n').\
        doAssertSerialRead('%d\n' % (len(LOREM),))

    # Execute the mock function
    Spanner.assertEqual(my_procedure.run(), 0)


if __name__ == "__main__":
    # Start the test
    char_count_mock()
