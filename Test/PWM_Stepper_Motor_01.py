
from time import sleep
import RPi.GPIO as gpio

DIR = 20
STEP = 21
CW =1
CCW =0

gpio.setmode(gpio.BCM)
gpio.setup(DIR, gpio.OUT)
gpio.setup(STEP, gpio.OUT)
gpio.output(DIR,CW)

<<<<<<< HEAD
#
print('Initialization Completed')
#
# Could have usesd only one DURATION constant but chose two. This gives play options.
durationFwd = 5000 # This is the duration of the motor spinning. used for forward direction
durationBwd = 5000 # This is the duration of the motor spinning. used for reverse direction
print('Duration Fwd set to ' + str(durationFwd))
print('Duration Bwd set to ' + str(durationBwd))
#
delay = 0.0001 # This is actualy a delay between PUL pulses - effectively sets the mtor rotation speed.
print('Speed set to ' + str(delay))
#
cycles = 10 # This is the number of cycles to be run once program is started.
cyclecount = 0 # This is the iteration of cycles to be run once program is started.
print('number of Cycles to Run set to ' + str(cycles))
#
#
def forward():
    GPIO.output(ENA, GPIO.HIGH)
    #GPIO.output(ENAI, GPIO.HIGH)
    print('ENA set to HIGH - Controller Enabled')
    #
    sleep(.5) # pause due to a possible change direction
    GPIO.output(DIR, GPIO.LOW)
    #GPIO.output(DIRI, GPIO.LOW)
    print('DIR set to LOW - Moving Forward at ' + str(delay))
    print('Controller PUL being driven.')
    for x in range(durationFwd): 
        GPIO.output(PUL, GPIO.HIGH)
        sleep(delay)
        GPIO.output(PUL, GPIO.LOW)
        sleep(delay)
    GPIO.output(ENA, GPIO.LOW)
    #GPIO.output(ENAI, GPIO.LOW)
    print('ENA set to LOW - Controller Disabled')
    sleep(.5) # pause for possible change direction
    return
#
#
def reverse():
    GPIO.output(ENA, GPIO.HIGH)
    #GPIO.output(ENAI, GPIO.HIGH)
    print('ENA set to HIGH - Controller Enabled')
    #
    sleep(.5) # pause due to a possible change direction
    GPIO.output(DIR, GPIO.HIGH)
    #GPIO.output(DIRI, GPIO.HIGH)
    print('DIR set to HIGH - Moving Backward at ' + str(delay))
    print('Controller PUL being driven.')
    #
    for y in range(durationBwd):
        GPIO.output(PUL, GPIO.HIGH)
        sleep(delay)
        GPIO.output(PUL, GPIO.LOW)
        sleep(delay)
    # GPIO.output(ENA, GPIO.LOW)
    # #GPIO.output(ENAI, GPIO.LOW)
    # print('ENA set to LOW - Controller Disabled')
    sleep(.5) # pause for possible change direction
    return

while cyclecount < cycles:
    forward()
    #reverse()
    cyclecount = (cyclecount + 1)
    print('Number of cycles completed: ' + str(cyclecount))
    print('Number of cycles remaining: ' + str(cycles - cyclecount))
#
GPIO.cleanup()
print('Cycling Completed')
#
=======

# Main body of code
try:
    while True:
        sleep(1)
        gpio.output(DIR,CW)
        for x in range(400):
            gpio.output(STEP,gpio.HIGH)
            sleep(.0100)
            gpio.output(STEP,gpio.LOW)
            sleep(.0100)
        
        sleep(1)
        gpio.output(DIR,CCW)
        for x in range(400):
            gpio.output(STEP,gpio.HIGH)
            sleep(.0010)
            gpio.output(STEP,gpio.LOW)
            sleep(.0010)
            
        
        
except KeyboardInterrupt: # If there is a KeyboardInterrupt (when you press ctrl+c), exit the program and cleanup
    print("Cleaning up!")
    gpio.cleanup()
>>>>>>> 84a55ec61950b818440a2b5d62b444e19da19f46
