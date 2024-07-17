import machine
from machine import Pin
import time

sensor = Pin(35, Pin.IN)
estado = 0

def read_nivel:
    estado = sensor.value()
    print(estado)
    time.sleep(1)
