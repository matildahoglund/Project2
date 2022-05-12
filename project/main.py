#!/usr/bin/env pybricks-micropython

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


# print(light.reflection())

def lift_forks(lift_motor):
    lift_motor.run_time(200,5000, then=Stop.HOLD, wait=True)
    return

def lower_forks(lift_motor):
    lift_motor.run_time(-50,1000, then=Stop.HOLD, wait=True)
    return

 

def lift_object(lift_motor, lift_forks, lower_forks):
    lower_forks(lift_motor)
    while touch_sensor.pressed() != True:
        bobbe.straight(100)
    lift_forks(lift_motor)
    
    return

Color = {"Brown":[], "Green":[], "Red":[],"Blue":[], "Purple":[], "Yellow":[]}

# Green': [(6, 19, 5), (9, 31, 14), (10, 33, 14), (10, 33, 16), (10, 33, 14), (9, 34, 15), (9, 33, 17), (8, 30, 11), (8, 30, 12), (10, 30, 16)]

Green = 

# 'Brown': [(16, 15, 10), (15, 14, 8), (15, 15, 9), (15, 14, 8), (14, 14, 8), (15, 15, 10), (15, 15, 9), (15, 15, 9)]}

# 'Purple': [(10, 8, 21), (12, 9, 32), (11, 9, 30), (9, 7, 25), (3, 2, 9), (7, 5, 20), (10, 8, 22)]

# 'Blue': [(12, 23, 38), (9, 21, 38), (10, 21, 36), (10, 19, 33), (8, 18, 33), (8, 20, 37), (6, 14, 22), (8, 19, 37), (10, 23, 40), (9, 21, 39), (12, 33, 68), (12, 36, 77), (10, 31, 68), (11, 32, 68), (12, 30, 64)]

# Yellow': [(50, 38, 7), (51, 39, 8), (51, 39, 7), (48, 37, 7), (47, 36, 6), (49, 38, 8), (50, 36, 6), (49, 36, 6), (48, 36, 6), (47, 35, 7), (49, 39, 8)]

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

def color_function():
    """ Denna funktionen ska hoppa in i vårtconditionet om rpg är inom våra mätta intervall
    och så fort den går ut vårt färgintervall ska den antingen köra framåt i 4 sekunder
    sedan börja läsa av igen eller svänga 45 grader"""
    color = rgb()
    """ Blue"""
    if 6<color[0]<12, 14<color[1]<36, 22<color[2]<77:
        our_color = "Blue"
        sensor_two(color)
        # "Red"
    # elif <color[0] <2,0< color[1]<2, color[2] < 3:
    #     our_color = "Red"
        # sensor_two(color) 
        
    elif 0<color[0] <2,0< color[1]<2, color[2] < 3:
        our_color = "Blue"
        sensor_two(color)
 
    elif 0<color[0] <2,0< color[1]<2, color[2] < 3:
        our_color ="Brown"
        sensor_two(color)
    elif 0<color[0] <2,0< color[1]<2, color[2] < 3:
        "our color = black"
        sensor_two(color)
    else: 
        """antingen vänd 45 grader eller kör fram någon sekund"""
    return