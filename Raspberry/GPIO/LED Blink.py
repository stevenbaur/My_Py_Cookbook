import RPi.GPIO as GPIO         #import the RPi.GPIO
import time.sleep               #import sleep-function to wait x seconds
GPIO.setmode(GPIO.BCM)          #configure GPIO as BCM
GPIO.setup(4, GPIO.OUT)         #Set BCM Pin 4 as Output-Pin (3.3V)

limit = int(input("How often blink the LED? "))
seconds = int(input("How many seconds for the cycle? "))
i = 0                           #Setup Counter i as 0
while i < limit:                #start loop that runs 10 times
    GPIO.Output(4, True)        #Set Output of BCM Pin 4 on High/True) -> LED ON
    time.sleep(seconds)         #Wait Seconds after turning on
    GPIO.Output(4, False)       #Set Output of BCM Pin 4 on Low/False -> LED OFF
    time.sleep(seconds)         # Wait Seconds after turning off
    i += 1                      #Add 1 to the counter of the loop
GPIO.Output(4, False)           #If loop stopped, make shure, that there is no power on BCM Pin 4
GPIO.cleanup()                  #Clean up after using GPIO