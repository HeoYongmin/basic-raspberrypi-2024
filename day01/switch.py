import RPi.GPIO as GPIO
import time

red = 21
green = 6
blue = 5
switch = 19  

GPIO.setmode(GPIO.BCM)

GPIO.setup(red, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)
GPIO.setup(switch, GPIO.IN, pull_up_down=GPIO.PUD_UP) 

led_state = 0
previous_input = GPIO.input(switch)

try:
    while True:
        current_input = GPIO.input(switch)
        if previous_input and not current_input:
            led_state = (led_state + 1) % 3 

            print(f"Switch pressed! Current LED state: {led_state}")

            if led_state == 0:
                GPIO.output(red, True)
                GPIO.output(green, False)
                GPIO.output(blue, False)
            elif led_state == 1:
                GPIO.output(red, False)
                GPIO.output(green, False)
                GPIO.output(blue, True)
            elif led_state == 2:
                GPIO.output(red, False)
                GPIO.output(green, True)
                GPIO.output(blue, False)
                
            time.sleep(0.3) 

        previous_input = current_input
        time.sleep(0.1)

except KeyboardInterrupt:  
    GPIO.cleanup() 
    print("Cleanup done. Exiting...")
