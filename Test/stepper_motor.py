
from time import sleep
import RPi.GPIO as gpio

DIR = 21
STEP = 20
CW =1
CCW =0

gpio.setmode(gpio.BCM)
gpio.setup(DIR, gpio.OUT)
gpio.setup(STEP, gpio.OUT)
gpio.output(DIR,CW)


# Main body of code
try:
    while True:
        sleep(1)
        gpio.output(DIR,CCW)
        for x in range(2000): #2300
            gpio.output(STEP,gpio.HIGH)
            sleep(.000500)
            gpio.output(STEP,gpio.LOW)
            sleep(.000500)
        for x in range(280): #2300
            gpio.output(STEP,gpio.HIGH)
            sleep(.00100)
            gpio.output(STEP,gpio.LOW)
            sleep(.00100)    
        sleep(0.4)
        gpio.output(DIR,CW) #2300
        for x in range(2325):
            gpio.output(STEP,gpio.HIGH)
            sleep(.000300)
            gpio.output(STEP,gpio.LOW)
            sleep(.000300)

except KeyboardInterrupt: # If there is a KeyboardInterrupt (when you press ctrl+c), exit the program and cleanup
    print("Cleaning up!")
    gpio.cleanup()
