import RPi.GPIO as GPIO
import time

segments = {
    'a': 20,
    'b': 24,
    'c': 19,
    'd': 13,
    'e': 6,
    'f': 21,
    'g': 26
}

digits = {
    0: (1, 1, 1, 1, 1, 1, 0),
    1: (0, 1, 1, 0, 0, 0, 0),
    2: (1, 1, 0, 1, 1, 0, 1),
    3: (1, 1, 1, 1, 0, 0, 1),
    4: (0, 1, 1, 0, 0, 1, 1),
    5: (1, 0, 1, 1, 0, 1, 1),
    6: (1, 0, 1, 1, 1, 1, 1),
    7: (1, 1, 1, 0, 0, 0, 0),
    8: (1, 1, 1, 1, 1, 1, 1),
    9: (1, 1, 1, 1, 0, 1, 1)
}

GPIO.setmode(GPIO.BCM)

for segment in segments.values():
    GPIO.setup(segment, GPIO.OUT)
    GPIO.output(segment, GPIO.LOW)

def Display(digit):
    for i, segment in enumerate(segments.values()):
        GPIO.output(segment, digits[digit][i])

try:
    while True:
        for digit in range(10):
            Display(digit)
            time.sleep(1)  

except KeyboardInterrupt:
    GPIO.cleanup()
