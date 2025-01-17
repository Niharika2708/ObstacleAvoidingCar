from machine import Pin,PWM #importing PIN and PWM
import time #importing time
import utime
from dcmotor import DCMotor
from hcsr04 import HCSR04

# Define motor pins.
motor1=Pin(10,Pin.OUT)
motor2=Pin(11,Pin.OUT)
motor3=Pin(12,Pin.OUT)
motor4=Pin(13,Pin.OUT)

# Define enable pins and PWM object.
enable1=PWM(Pin(6))
enable2=PWM(Pin(7))

# Define Trigger and Echo pins.
trigger = Pin(3, Pin.OUT)
echo = Pin(2, Pin.IN)

# Define Servo pin and PWM object.
servoPin = Pin(15)
servo = PWM(servoPin)
duty_cycle = 0 # Defining and initializing duty cycle PWM

# Define frequency for servo and enable pins.
servo.freq(50)
enable1.freq(1000)
enable2.freq(1000)

# Set maximum duty cycle for maximum speed.
enable1.duty_u16(65025)
enable2.duty_u16(65025)

# Forward
def move_forward():
    motor1.low()
    motor2.high()
    motor3.high()
    motor4.low()
    
# Backward
def move_backward():
    motor1.high()
    motor2.low()
    motor3.low()
    motor4.high()
    
#Turn Right
def turn_right():
    motor1.low()
    motor2.high()
    motor3.low()
    motor4.high()
    
#Turn Left
def turn_left():
    motor1.high()
    motor2.low()
    motor3.high()
    motor4.low()
   
#Stop
def stop():
    motor1.low()
    motor2.low()
    motor3.low()
    motor4.low()

#Function to set servo angle.
def setservo(angle):
    duty_cycle = int(angle*(7803-1950)/180) + 1950
    servo.duty_u16(duty_cycle)

setservo(90)

while True:
    distance=distance_cm() #Getting distance in cm
    
    #Defining direction based on conditions
    if distance < 15:
        stop()
        move_backward()
        time.sleep(1)
        stop()
        time.sleep(0.5)
        setservo(30) #Servo angle to 30 degree
        time.sleep(1)
        right_distance=distance_cm()
        #print(right_distance)
        time.sleep(0.5)
        setservo(150) #Servo angle to 150 degree
        time.sleep(1)
        left_distance=distance_cm()
        #print(left_distance)
        time.sleep(0.5)
        setservo(90)
        
        if right_distance > left_distance:
            turn_right()
            time.sleep(2)
            stop()
        else:
            turn_left()
            time.sleep(2)
            stop()
    else:
        move_forward()

    time.sleep(0.5)


