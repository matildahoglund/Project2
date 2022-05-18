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

<<<<<<< HEAD
<<<<<<< HEAD
def color_function(sensor, lift_object):
    color = light.rgb()
    print(color)
    while True:
        color = light.rgb()
        print(color)
        if 5<color[0]<13 and 13<color[1]<37 and 21<color[2]<78:
            print("Blue")
            sensor()

        elif 46<color[0]<52 and 34<color[1]<40 and 5<color[2]<9:
            print("Yellow")
            sensor()
    
        elif 13<color[0]<17 and 12<color[1]<16 and 6<color[2] <11:
            print("Brown")
            sensor()

        elif 2<color[0]<13 and 1<color[1]<10 and 8<color[2]<33:
            print("Purple")
            sensor()
        
        elif 5<color[0]<11 and 18<color[1]<35 and 4<color[2]<18:
            print("Green")
            sensor()

        else: 
            break
    lift_object(lift_motor, lift_forks, lower_forks)
    return

color_function(sensor)
=======
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
        
    
=======
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
            color = light.rgb()
        robot.drive_time(500, -180, 2000)
        left_motor = Motor(Port.C, positive_direction=Direction.COUNTERCLOCKWISE, gears = [ 12,20])
        right_motor = Motor(Port.B, positive_direction=Direction.COUNTERCLOCKWISE, gears = [ 12,20])
        bobbe = DriveBase(left_motor, right_motor, wheel_diameter = 47, axle_track = 128) 
        color = light.rgb()
        
         
        while 47<color[0]<51 and 35<color[1]<39 and 6<color[2]<8:
            our_color = "Yellow"
            sensor()
            color = light.rgb()
            
        
    
>>>>>>> 2d2da59f47d1e68799e460cf34534d2a2cc5567a
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
<<<<<<< HEAD
>>>>>>> efc176cce7b70177d9b99787b891d2fb964e89ff
=======
>>>>>>> 2d2da59f47d1e68799e460cf34534d2a2cc5567a
