from machine import Pin, PWM
from time import sleep

# Define os pinos
in1 = Pin(12, Pin.OUT)
in2 = Pin(14, Pin.OUT)
ena = PWM(Pin(13), freq=1000)

# Função para parar o motor
def motor_parar():
    in1.value(0)
    in2.value(0)
    ena.duty(0)
    
def motor_forca(forca):
    in1.value(1)
    in2.value(0)
    ena.duty(int((forca*1023)/100))

motor_forca(80)