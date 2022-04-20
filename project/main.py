#!/usr/bin/env pybricks-micropython
import sys
import __init__

from pybrick.evdevices import Motor, colorsensor
from pbricks.parameters import port,direction,stop
from pythbticks.tools import wait
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

def sensor(port):
    # Initialize the motors.
    left_motor = Motor(Port.B)
    right_motor = Motor(Port.C)
    # Initialize the color sensor.  
    line_sensor = ColorSensor(Port.S3)
    # Initialize the drive base.
    robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)
    # Calculate the light threshold. Choose values based on your measurements.
    BLACK = 9
    WHITE = 85
    threshold = (BLACK + WHITE) / 2
    # Set the drive speed at 100 millimeters per second.
    DRIVE_SPEED = 100
    # Set the gain of the proportional line controller. This means that for every
    # percentage point of light deviating from the threshold, we set the turn
    # rate of the drivebase to 1.2 degrees per second.

    # For example, if the light value deviates from the threshold by 10, the robot
    # steers at 10*1.2 = 12 degrees per second.
    PROPORTIONAL_GAIN = 1.2
    # Start following the line endlessly.
    while True:
        # Calculate the deviation from the threshold.
        deviation = line_sensor.reflection() - threshold
        # Calculate the turn rate.
        turn_rate = PROPORTIONAL_GAIN * deviation
        # Set the drive base speed and turn rate.
        robot.drive(DRIVE_SPEED, turn_rate)
        # You can wait for a short time or do other things in this loop.
        wait(10)

if __name__ == '__main__':
    sys.exit(main())
    Touchsensors(port) """titta om sensor är påslagen"""
    checking_color(port)
