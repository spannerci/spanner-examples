# This example will make sure our device meets some specifications or thresholds
# that we want to be true for every future version of our code. In other words,
# we wanna make sure that these are always tested and we never end up exceeding
# them.
#
# In this particular example this is a battery-powered device and we want to
# make sure that any chances we make in our algorithm (such as functionality, or
# measuring frequency) will not result in us reducing the battery life below the
# advertised on.

# Our Testboard is connected with a Power Control circuit (INA219) that allows 
# us to turn the Power to our device On and Off programmatically. It's also
# connected to a power consumption measurement circuit that allow us to measure
# the total power consumption in a given time period.

# The goal of this example is to show you how you can run much more advanced
# tests than environmental mocks, inputs and outputs. Power Consumption is,
# after all, an "output" or "functionality" of our devices, and we want to make
# sure that functionality is tested.

# This is one real world example of a complex, but realistic, functional test
# you would run for your devices.

import time
import pytest
from SpannerTestboard import SpannerTestboard

testboard = SpannerTestboard("testboard_name")

def test_measure_power_consumption():

    #  Initialize the Power Control circuit (INA219)
    INA219 = SpannerTestboard.INA219
        
    # Start measuring power consumption. The interval (msecs) can be used to
    # set the desired interval between measurements.
    testboard.ina219_startMeasurement(INA219.CURRENT_MA, interval=1000)
    testboard.ina219_startMeasurement(INA219.BUS_VOLTAGE_V)
    testboard.ina219_startMeasurement(INA219.SHUNT_VOLTAGE_MV)

    # Measure for 30 seconds
    time.sleep(30)
    
    # Get an instant measurement
    print(testboard.ina219_getValue(INA219.SHUNT_VOLTAGE_MV))
    
    # Stop measuring power consumption
    testboard.ina219_stopMeasurement(INA219.CURRENT_MA)
    testboard.ina219_stopMeasurement(INA219.BUS_VOLTAGE_V)
    testboard.ina219_stopMeasurement(INA219.SHUNT_VOLTAGE_MV)

    # Get average measurements
    avg_ma =  testboard.ina219_getAverage(INA219.CURRENT_MA)
    avg_v =  testboard.ina219_getAverage(INA219.BUS_VOLTAGE_V)
    assert testboard.ina219_getAverage(INA219.SHUNT_VOLTAGE_MV) > 0
    
    print(avg_ma)
    print(avg_v)

    # Make sure the total power consumption didn't exceed 100mAh
    assert avg_ma < 100
    
    # Make sure the total voltage didn't exceed 5.2V
    assert avg_v < 5.2
