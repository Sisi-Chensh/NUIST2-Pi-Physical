#Chen Sihan
#2026/3/30
#GPIO18 outputs a high level,turns on the LED,and then turns it off after 1 second.
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
print("LED on")
GPIO.output(18,GPIO.HIGH)
time.sleep(1)
print("LED off")
GPIO.output(18,GPIO.LOW)

