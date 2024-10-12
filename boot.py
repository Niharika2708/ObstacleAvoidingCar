try:
    import usocket as socket
except:
    import socket
    
from machine import Pin
import network

import esp
esp.osdebug(None)

import gc
gc.collect()

ssid = 'Linksys17094'
password = 'mnnfp9af9n'

station = network.WLAN(network.STA_IF)

station.active(True)
station.connect(ssid, password)

while station.isconnected() == False:
    pass
print('Connection successful')
print(station.ifconfig())

import main
