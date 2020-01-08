import RPi.GPIO as GPIO         #import the RPi.GPIO
import time.sleep               #import sleep-function to wait x seconds
GPIO.setmode(GPIO.BCM)          #configure GPIO as BCM
GPIO.setup(4, GPIO.OUT)         #Set BCM Pin 4 as Output-Pin (3.3V)

my_pwm = GPIO.PWM(4, 100)       #Setup PWM for BCM Pin 4 with 100 Hz
my_pwm.start(0)                #Start my_pwm with DutyCycle of 0 (basically off)

for i in range (0,100):
    my_pwm.ChangeDutyCycle(i)   #Turn LED from Off to full brightness
    time.sleep(5)               #Wait 5 Seconds before dimming the LED back again
for i in range (100,0):
    my_pwm.ChangeDutyCycle(i)   #Turn LED from ON to Off
    time.sleep(5)               #Wait 5 Seconds before exiting

GPIO.Output(4, False)           #If loop stopped, make shure, that there is no power on BCM Pin 4
GPIO.cleanup()                  #Clean up after using GPIO