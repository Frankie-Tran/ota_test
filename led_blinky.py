from machine import Pin
from time import sleep

led = Pin(2, Pin.OUT)  # Pico onboard LED

while True:
    led.on()      # Turn LED on
    sleep(0.1)      # Wait 1 second

    led.off()     # Turn LED off
    sleep(1)      # Wait 1 second
