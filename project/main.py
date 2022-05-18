#!/usr/bin/env pybricks-micropython

from math import cosh
from operator import truediv
from pybricks.ev3devices import Motor, ColorSensor, TouchSensor
from pybricks.parameters import Port, Direction, Stop
from pybricks.tools import wait
from pybricks.robotics import DriveBase


left_motor = Motor(Port.C, positive_direction=Direction.COUNTERCLOCKWISE, gears = [ 12,20])
right_motor = Motor(Port.B, positive_direction=Direction.COUNTERCLOCKWISE, gears = [ 12,20])
bobbe = DriveBase(left_motor, right_motor, wheel_diameter = 47, axle_track = 128)
lift_motor = Motor(Port.A, positive_direction=Direction.CLOCKWISE)
touch_sensor = TouchSensor(Port.S1)

def drive_foward(Sensor):
    left_motor = Motor(Port.B)
    right_motor = Motor(Port.C) 
    return robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)
    

def turn(Sensor):
    left_motor = Motor(Port.B)
    right_motor = Motor(Port.C) 
    # This turns 90 degrees/sec right while moving 100 mm/sec
    robot.drive (100, 90)
    # This turns 180 degrees/sec left while moving at 500 mm/sec for 2 seconds
    return robot.drive_time(500, -90, 2000)

    
    
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
    return print("klar")
    

# robot = DriveBase(left_motor, right_motor, wheel_diameter = 55.5, axle_track =104)
# light = ColorSensor(Port.S3)


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

# Color = {"Brown":[], "Green":[], "Red":[],"Blue":[], "Purple":[], "Yellow":[]}


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

def color_function(sensor,turn(),drive_forward()):
    """ Denna funktionen ska hoppa in i vårtconditionet om rpg är inom våra mätta intervall
    och så fort den går ut vårt färgintervall ska den antingen köra framåt i 4 sekunder
    sedan börja läsa av igen eller svänga 45 grader"""
    right_color = True 
    while not right_color: 
        color = light.rgb()
        print(color)
        while 6<color[0]<12 and 14<color[1]<36 and 22<color[2]<77:
            our_color = "Blue"
            sensor()
        turn()
        color = light.rgb()
        
        while 47<color[0]<51 and 35<color[1]<39 and 6<color[2]<8:
            our_color = "Yellow"
            sensor()
        
    
        while 14<color[0]<16 and 14<color[1]<15 and 8<color[2] <10:
            our_color ="Brown"
            sensor()

        while 3<color[0]<12 and 2<color[1]<9 and 9<color[2]<32:
            "our color = Purple"
            sensor()
        
        while 6<color[0]<10 and 19<color[1]<34 and 5<color[2]<17:
            "our color = Green"
            sensor()

        else: 
            """antingen vänd 45 grader eller kör fram någon sekund"""
        return

color_function(sensor)
