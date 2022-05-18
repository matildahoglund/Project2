#!/usr/bin/env pybricks-micropython
from pickle import TRUE
import sys
import __init__

from pybrick.evdevices import Motor, colorsensor
from pbricks.parameters import port,direction,stop
from pythbticks.tools import wait
from pybticks.robotics import DriveBase

left_motor = Motor(Port.C, positive_direction-direction.CLOCKWISE, gears = [ 12,20])
right_motor = Motor(Port.B, positive_direction-direction.CLOCKWISE, gears = [ 12,20])
lift_motor = Motor(Port.A, positive_direction-direction.CLOCKWISE) 
touch_sensor = Port(S1)

bobbe = DriveBase(left_motor, right_motor, wheel diameter = 47, axle_track = 128)

def main():
    bobbe.straight(100) """ 100 är i millimeter"""
    return 0

def bobbe_drive(bobbe):
    bobbe.run_until_stalled(50,then=stop.COAST, dutylimit=None)

def lift_forks(lift_motor):

    lift_motor.run_time(50, 1, then=stop.HOLD, wait=True)
    return

def lower_forks(lift_motor):

    lift_motor.run_time(-50, 1.2 , then=stop.HOLD, wait=True)
    return


#lift when pressed#
def lift_object(lift_motor, bobbe):
    lower_forks(lift_motor)
    bobbe_drive(bobbe)
    if touch_sensor.pressed(): 
        lift_forks(lift_motor)
    
    return


# Initialize the motors.
left_motor = Motor(Port.B)
right_motor = Motor(Port.C)

# Initialize the color sensor.
line_sensor = ColorSensor(Port.S3)

# Ini0tialize the drive base.

bobbe = DriveBase(left_motor, right_motor, wheel diameter = 47, axle_track = 128)

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

