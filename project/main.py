#!/usr/bin/env pybricks-micropython
import sys
import __init__

from pybrick.evdevices import Motor, colorsensor
from pbricks.parameters import port,direction,stop
from pythbticks.tools Import wait
from pybticks.robotics import DriveBase

def checking_sensor(port):
    port = TouchSensor(port)
    return  pressed(port)

def checking_color(port):
    return color(port) 
    lift_motor = Motor(Port.B, positive_direction-Direction.CLOCKWISE, gears = [ 12,36])
    """ A positive speed value should make the motor move clockwise. """

def driving(Port):
    left_motor = Motor(Port.B, positive_direction-Direction.CLOCKWISE, gears = [ 12,20])
    rigt_motor = Motor(Port.B, positive_direction-Direction.CLOCKWISE, gears = [ 12,20])
    nonne = DriveBase(left_motor, right_motor, wheel diameter = 47, axle_track = 128)
    return 
     
def main():
    bobbe.straight(100) """ 100 är i millimeter"""
    return 0


def main():
    return 0

if __name__ == '__main__':
    sys.exit(main())
    Touchsensors(port) """titta om sensor är påslagen"""
    checking_color(port)
    
    
    