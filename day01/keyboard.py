import RPi.GPIO as GPIO

led = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(led, GPIO.OUT)

try:
    while True:
        user_input = input("o를 누르면 ON x를 누르면 off")

        if user_input == 'o':
            GPIO.output(led, GPIO.LOW)  
        elif user_input == 'x':
            GPIO.output(led, GPIO.HIGH) 
        elif user_input == 'q':
            break

except KeyboardInterrupt:
    GPIO.cleanup()
