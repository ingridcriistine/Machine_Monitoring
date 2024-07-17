import machine
from machine import Pin
import time

sensor = 25  # The pin the encoder is connected to
pulses = 0  # Number of pulses
pulses_per_turn = 1  # Number of pulses per revolution
rpm = 0  # RPM reading
timeold = 0  # Variable to store previous time
velocimetro = Pin(sensor, Pin.IN)
motor = Pin(12, Pin.OUT)
 
def counter(pin):
    global pulses                                   
    # Update count
    pulses += 1

def setup():
    global sensor, pulses, timeold
    # Setup serial communication
    uart = machine.UART(0, baudrate=9600)
    # Setup encoder pin as input
    
    velocimetro.irq(trigger=Pin.IRQ_FALLING, handler=counter)
    # Initialize variables
    pulses = 0
    rpm = 0
    timeold = time.ticks_ms()

def loop():
    
    global pulses, rpm, timeold
    
    while True:
        if time.ticks_ms() - timeold >= 1000:
            # Don't process interrupts during calculations
            velocimetro.irq(handler=None)
            
            # Calculate RPM
            rpm = int(60 * 1000 / pulses_per_turn / (time.ticks_ms() - timeold) * pulses)
            timeold = time.ticks_ms()
            pulses = 0
            
            # Write RPM to serial port
            print("RPM =", rpm)
            
            # Restart interrupt processing
            velocimetro.irq(trigger=Pin.IRQ_FALLING, handler=counter)
        
        time.sleep(0.01)

motor.on()
loop()
    
