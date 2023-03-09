import time
import RPi.GPIO as GPIO

# Pin definitions
pwm_pin = 12
out_1_pin = 5
out_2_pin = 6

# Use "GPIO" pin numbering
GPIO.setmode(GPIO.BCM)

# Set LED pin as output
GPIO.setup(pwm_pin, GPIO.OUT)
GPIO.setup(out_1_pin, GPIO.OUT)
GPIO.setup(out_2_pin, GPIO.OUT)

# Initialize pwm object with 50 Hz and 0% duty cycle
pwm = GPIO.PWM(pwm_pin, 100)
pwm.start(0)

while True:
    GPIO.output(out_1_pin, GPIO.HIGH)
    GPIO.output(out_2_pin, GPIO.LOW)

    # Set PWM duty cycle to 50%, wait, then to 90%
    time.sleep(5)
    GPIO.output(out_1_pin, GPIO.LOW)
    GPIO.output(out_2_pin, GPIO.LOW)

    # Set PWM duty cycle to 50%, wait, then to 90%
    time.sleep(5)
    GPIO.output(out_1_pin, GPIO.LOW)
    GPIO.output(out_2_pin, GPIO.HIGH)

    # Set PWM duty cycle to 50%, wait, then to 90%
    time.sleep(5)

    GPIO.output(out_1_pin, GPIO.LOW)
    GPIO.output(out_2_pin, GPIO.LOW)

