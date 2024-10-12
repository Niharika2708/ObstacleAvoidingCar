# from time import sleep
# from DCMotor import DCMotor
# 
# motorA = DCMotor(13, 4, 5)
# motorB = DCMotor(14, 26, 27)
# motorA.forward()
# sleep(0.001)
# motorB.forward()
# sleep(5)
# motorA.stop()
# sleep(0.001)
# motorB.stop()
# sleep(1)
# motorA.reverse()
# sleep(0.001)
# motorB.reverse()
# sleep(5)
# motorA.stop()
# sleep(0.001)
# motorB.stop()
# sleep(5)
#

from machine import Pin,PWM 
import time
from DCMotor import DCMotor
from hcsr04 import HCSR04
from servo import Servo

# Defining motor pins
motorA = DCMotor(13, 4, 5)
motorB = DCMotor(14, 26, 27)

# Defining sensor Trigger and Echo pins.
sensor = HCSR04(trigger_pin=23, echo_pin=18, echo_timeout=10000)

# Defining  Servo pin.
pin22 = machine.Pin(22)
servo = machine.PWM(pin22,freq=50)
servo.duty(0)

servo.write_angle(90)

while True:
    #Getting distance in cm.
    distance = sensor.distance_cm()
    
    if distance < 15:
        motorA.stop()
        motorB.stop()
#         reverse()
#         sleep(1)
#         stop()
#         sleep(0.5)
#         #Turn servo to one side.
#         servo.write_angle(30) 
#         sleep(1)
#         right_distance = distance_cm()
#         time.sleep(0.5)
#         #Turn servo the other side.
#         servo.write_angle(150) 
#         sleep(1)
#         left_distance = distance_cm()
#         sleep(0.5)
#         servo.write_angle(90)
#         
#         if right_distance > left_distance:
#             turn_right()
#             sleep(2)
#             stop()
#         else:
#             turn_left()
#             sleep(2)
#             stop()
    else:
        motorA.forward()
        motorB.forward()

    sleep(0.5)




        