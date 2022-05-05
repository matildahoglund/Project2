#!/usr/bin/env pybricks-micropython
import sys
import __init__

from pybricks.ev3devices import Motor, ColorSensor, TouchSensor
from pybricks.parameters import Port, Direction, Stop
from pybricks.tools import wait
from pybricks.robotics import DriveBase


left_motor = Motor(Port.C, positive_direction=Direction.COUNTERCLOCKWISE, gears = [ 12,20])
right_motor = Motor(Port.B, positive_direction=Direction.COUNTERCLOCKWISE, gears = [ 12,20])
bobbe = DriveBase(left_motor, right_motor, wheel_diameter = 47, axle_track = 128)
lift_motor = Motor(Port.A, positive_direction=Direction.CLOCKWISE)
touch_sensor = TouchSensor(Port.S1)

    
def main():
    bobbe.straight(100)
    return 0
    
    
def sensor():
    left_motor = Motor(Port.B)
    right_motor = Motor(Port.C) 
    line_sensor = ColorSensor(Port.S3)
    robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)
    BLACK = 9
    WHITE = 85
    threshold = (BLACK + WHITE) / 2
    DRIVE_SPEED = -80
    PROPORTIONAL_GAIN = 2.5
    while True:
        deviation = line_sensor.reflection() - threshold
        turn_rate = PROPORTIONAL_GAIN * deviation
        robot.drive(DRIVE_SPEED, turn_rate)
        wait(30)
    return 
    

robot = DriveBase(left_motor, right_motor, wheel_diameter = 55.5, axle_track =104)
light = ColorSensor(Port.S3)


# white = [90, 95]
# Green = 14
# Blue = 16
# Blue_new = 8
# brown = 23
# lila = 18
# rosa = 85 87


# print(light.reflection())

def lift_forks(lift_motor):
    lift_motor.run_time(200,5000, then=Stop.HOLD, wait=True)
    return

def lower_forks(lift_motor):
    lift_motor.run_time(-50,1000, then=Stop.HOLD, wait=True)
    return

 
#lift when pressed#
def lift_object(lift_motor, lift_forks, lower_forks):
    lower_forks(lift_motor)
    while touch_sensor.pressed() != True:
        bobbe.straight(100)
    lift_forks(lift_motor)
    
    return

Color = {"Brown":[], "Green":[], "Red":[],"Blue":[]}


def Checking_color(Color):
    loop = True
    while loop:
        Colors = input("What color do you want to add?(If you are finish type x): ")
        for key in Color.keys():
            if key == Colors:
                Color[key].append(light.rgb())
        if Colors == "X":
            loop = False
            print("You have puted in all values")
            return Color

Checking_color(Color)
print(Color)