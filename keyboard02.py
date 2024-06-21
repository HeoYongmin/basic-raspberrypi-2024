import RPi.GPIO as GPIO
import time

piezoPin = 13
melody = [261, 293, 329, 349, 392, 440, 493, 523]  

GPIO.setmode(GPIO.BCM)
GPIO.setup(piezoPin, GPIO.OUT)

# 아날로그 출력을 위한 객체 생성
Buzz = GPIO.PWM(piezoPin, 440) 

try:
    while True:
        user_input = input()  

        #try:
        melody_index = int(user_input) - 1  
        if 0 <= melody_index < len(melody):
            Buzz.start(50) 
            Buzz.ChangeFrequency(melody[melody_index])  
            time.sleep(0.5) 
            Buzz.stop()  
        
        #except ValueError:
         #   pass

except KeyboardInterrupt:
    GPIO.cleanup()
