#!/usr/bin/env pybricks-micropython
import sys
import __init__

from pybricks.ev3devices import Motor, ColorSensor
from pybricks.parameters import Port, Direction, Stop
from pybricks.tools import wait
from pybricks.robotics import DriveBase


left_motor = Motor(Port.C, positive_direction=Direction.COUNTERCLOCKWISE, gears = [ 12,20])
right_motor = Motor(Port.B, positive_direction=Direction.COUNTERCLOCKWISE, gears = [ 12,20])
bobbe = DriveBase(left_motor, right_motor, wheel_diameter = 47, axle_track = 128)
lift_motor = Motor(Port.A, positive_direction=Direction.CLOCKWISE)

def checking_sensor(port):
    port = TouchSensor(port)
    return pressed(port)

def checking_color():
    light = ColorSensor(Port.S2)
    return color()
    
def main():
    bobbe.straight(100)
    return 0

def lift_forks(lift_motor):
    lift_motor.run_until_stalled(50, then=Stop.HOLD, duty_limit=80)
    return

    
    
# def sensor(port):
#     # Initialize the motors.
#     left_motor = Motor(Port.B)
#     right_motor = Motor(Port.C)
#     # Initialize the color sensor.  
#     line_sensor = ColorSensor(Port.S3)
#     # Initialize the drive base.
#     robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)
#     # Calculate the light threshold. Choose values based on your measurements.
#     BLACK = 9
#     WHITE = 85
#     threshold = (BLACK + WHITE) / 2
#     # Set the drive speed at 100 millimeters per second.
#     DRIVE_SPEED = 100
#     # Set the gain of the proportional line controller. This means that for every
#     # percentage point of light deviating from the threshold, we set the turn
#     # rate of the drivebase to 1.2 degrees per second.

#     # For example, if the light value deviates from the threshold by 10, the robot
#     # steers at 10*1.2 = 12 degrees per second.
#     PROPORTIONAL_GAIN = 1.2
#     # Start following the line endlessly.
#     while True:
#         # Calculate the deviation from the threshold.
#         deviation = line_sensor.reflection() - threshold
#         # Calculate the turn rate.
#         turn_rate = PROPORTIONAL_GAIN * deviation
#         # Set the drive base speed and turn rate.
#         robot.drive(DRIVE_SPEED, turn_rate)
#         # You can wait for a short time or do other things in this loop.
#         wait(30)


"""titta om sensor är påslagen"""
# if __name__ == '__main__':
#     sys.exit(main())
    
    
# Ok = true
# while not ok:
#     answer = Input("Vad vill du få roboten att göra..?")
#     if answer = 1: 
#         sensor(port)
#     elif answer = 2:
        
#     elif answer = 3:
        
#     elif answer = 4:
    

# ev3 = EV3Brick()
# robot = DriveBase(left_motor, right_motor, wheel_diameter = 55.5, axle_track =104)
# light = ColorSensor(Port.S2)
# touch = TouchSensor(Port.S2)
# gyro = GyroSensor(Port.S1)

# While True:
#     while light.reflection() > 15:
#         robot.drive(-100,0)
#     robot.stop()
#     left_motor.brake()
#     right_motor.brake()
#     while light.reflection() < 50:
#         robot.drive(100,0)
#     robot.stop()
#     left_motor.brake()
#     right_motor.brake()

lift_forks(lift_motor)