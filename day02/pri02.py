import RPi.GPIO as GPIO
import time

led = 21
pirPin = 24

GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)
GPIO.setup(pirPin, GPIO.IN, pull_up_down= GPIO.PUD_DOWN)

try:
    while True:
        if GPIO.input(pirPin) == True:
            print("Detected")
            GPIO.output(led, GPIO.HIGH) 
            time.sleep(0.5)  
        else:
            GPIO.output(led, GPIO.LOW)  

except KeyboardInterrupt:
    GPIO.cleanup()
