import machine
from time import sleep
from DCMotor import DCMotor
from hcsr04 import HCSR04

motorA = DCMotor(13, 4, 5)
motorB = DCMotor(14, 26, 27)

# sleep(5)
# 
# motorA.forward()
# motorB.forward()
# sleep(5)
# 
# motorA.reverse()
# motorB.reverse()
# sleep(5)



# try:
#     import usocket as socket
# except:
#     import socket
#     
#     
# import network

# def web_page():
#     html = """<html><head><meta name="viewport"
# content="width=device-width, initial-scale=1"></head>
# <style>
# .button {
#   border: 3px black;
#   color: 3px black;
#   padding: 30px 32px;
#   text-align: center;
#   font-size: 16px;
#   margin: 10px 80px;
#   cursor: pointer;
# }
# .on {background-color: lime;} 
# .off {background-color: red;} 
# </style>
# <body>
# <a href =\"?car=on\"><button class="on"><b>on</b></button></a>&nbsp;
# <a href =\"?car=off\"><button class="off"><b>off</b></button></a>
# </body></html>"""
#     return html
# 
# 
#wifi access control - creating a socket.
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.bind(('', 80))
# s.listen(5)
# 
# # Defining motor pins
# motorA = DCMotor(13, 4, 5)
# motorB = DCMotor(14, 26, 27)
# 
# Defining sensor Trigger and Echo pins.
sensor = HCSR04(trigger_pin=23, echo_pin=18, echo_timeout=10000)
# print('ok')
# 
# Defining  Servo pin.
pin22 = machine.Pin(22)
servo = machine.PWM(pin22,freq=50)

#servo.duty(70)#right
#sleep(5)

#     servo.duty(30) #right
#     sleep(5)
#     servo.duty(110) #left
#     sleep(5)
#     servo.duty(70)#front
#     sleep(5)

# 
# conn, addr = s.accept()
# print('Got a connection from %s' % str(addr))
# request = conn.recv(1024)
# request = str(request)
# print('Content = %s' % request)
# car_on = request.find('/?car=on')
# car_off = request.find('/?car=off')
# 
# response = web_page()
# conn.send('HTTP/1.1 200 OK\n')
# conn.send('Content-Type: text/html\n')
# conn.send('Connection: close\n\n')
# conn.sendall(response)
# conn.close()
# 
while True:
#     
#     conn, addr = s.accept()
#     print('Got a connection from %s' % str(addr))
#     request = conn.recv(1024)
#     request = str(request)
#     print('Content = %s' % request)
#     car_on = request.find('/?car=on')
#     car_off = request.find('/?car=off')
#     print('index found is ', car_on)
#     
#     if 1: #car_on == 6:
#          motorA.forward()
#          motorB.forward()
#         
#     if 0: #car_off == 6:
#         motorA.stop()
#         motorB.stop()
#                
#     response = web_page()
#     conn.send('HTTP/1.1 200 OK\n')
#     conn.send('Content-Type: text/html\n')
#     conn.send('Connection: close\n\n')
#     conn.sendall(response)
#     conn.close()       
#         
        #Getting distance in cm.
        servo.duty(70)
        sleep(0.1)
        distance = sensor.distance_cm()
        if distance < 50 and distance > 0:
            motorA.stop()
            motorB.stop()
            sleep(1)
            
            motorA.reverse()
            motorB.reverse()
            sleep(1)
            
            motorA.stop()
            motorB.stop()
            sleep(1)
            
            #Turn servo to one side.
            servo.duty(30) 
            sleep(1)
            right_distance = sensor.distance_cm()
            sleep(0.5)
            
            #Turn servo the other side.
            servo.duty(110) 
            sleep(1)
            left_distance = sensor.distance_cm()
            sleep(0.5)
            
        
            if (right_distance > left_distance) or (right_distance <0):
                #turning right
                motorB.forward()  
                sleep(1)
                motorA.stop()
                motorB.stop()
               # servo.duty(90)
        
            else:
                #turning left
                motorA.forward()  
                sleep(1)
                motorA.stop()
                motorB.stop()
        else:
            motorA.forward()
            motorB.forward()

        sleep(0.1)
        
#      if car_off == 6:
#         motorA.stop()
#         motorB.stop()
#         
# sleep(0.1)
#         
#     response = web_page()
#     conn.send('HTTP/1.1 200 OK\n')
#     conn.send('Content-Type: text/html\n')
#     conn.send('Connection: close\n\n')
#     conn.sendall(response)
#     conn.close()           