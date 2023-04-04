#code for switch testing, med prioirty low difficulty
import RPi.GPIO as gpio
from time import sleep

SW = 22

DIR = 20
STEP = 21
CW =1
CCW =0

gpio.setmode(gpio.BCM)
gpio.setup(DIR, gpio.OUT)
gpio.setup(STEP, gpio.OUT)
gpio.output(DIR,CW)

gpio.setmode(gpio.BCM)
gpio.setup(SW, gpio.IN)

try:
    while(True):


        gpio.output(DIR,CW) #2300
        for x in range(50):
            gpio.output(STEP,gpio.HIGH)
            sleep(.00100)
            gpio.output(STEP,gpio.LOW)
            sleep(.00100)

        if gpio.input(SW):
            print("switch closed")
            gpio.cleanup()
            break
        # else:
        #     print("opeN")
        

except KeyboardInterrupt: # If there is a KeyboardInterrupt (when you press ctrl+c), exit the program and cleanup
    print("Cleaning up!")
    gpio.cleanup()
