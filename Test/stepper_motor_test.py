import time
import RPi.GPIO as GPIO

# Pin definitions
pwm_pin = 12 # for stepper motor we are currently and going to use Pin 12
out_1_pin = 16
enable_pin = 26
out_2_pin = 4

# Use "GPIO" pin numbering
GPIO.setmode(GPIO.BCM)

# Set LED pin as output
GPIO.setup(pwm_pin, GPIO.OUT)
GPIO.setup(out_1_pin, GPIO.OUT)
GPIO.setup(out_2_pin, GPIO.OUT)
GPIO.setup(enable_pin, GPIO.OUT)


# Initialize pwm object with 50 Hz and 0% duty cycle
#pwm = GPIO.PWM(pwm_pin, 25)
#pwm.start(0)
GPIO.output(enable_pin, GPIO.HIGH)
GPIO.output(out_2_pin, GPIO.HIGH)


for i in range(0,1600):
    GPIO.output(out_1_pin, GPIO.HIGH)
    time.sleep(0.002)
    GPIO.output(out_1_pin, GPIO.LOW)
    time.sleep(0.002)
    i = i+1
# Stop, cleanup, and exit
#pwm.stop()
GPIO.cleanup()
