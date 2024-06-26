# 세그먼트에 1234 표시
import RPi.GPIO as GPIO
import time

segment_pins = [20, 24, 19, 13, 6, 21, 26]
digit_pins = [18, 23, 25, 22]

segment_patterns = [
    [1, 1, 1, 1, 1, 1, 0],  # 0
    [0, 1, 1, 0, 0, 0, 0],  # 1
    [1, 1, 0, 1, 1, 0, 1],  # 2
    [1, 1, 1, 1, 0, 0, 1],  # 3
    [0, 1, 1, 0, 0, 1, 1],  # 4
    [1, 0, 1, 1, 0, 1, 1],  # 5
    [0, 0, 1, 1, 1, 1, 1],  # 6
    [1, 1, 1, 0, 0, 1, 0],  # 7
    [1, 1, 1, 1, 1, 1, 1],  # 8
    [1, 1, 1, 0, 0, 1, 1]   # 9
]

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False) # GPIO 관련 경고 메시지를 비활성화
    for pin in segment_pins:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.LOW)
    for pin in digit_pins:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.HIGH) # 각 핀의 초기 값을 HIGH로 설정하여 모든 자리 핀을 비활성화

def display_digit(digit, position):
    pattern = segment_patterns[digit]
    for pin, state in zip(segment_pins, pattern):
        GPIO.output(pin, state)
    GPIO.output(digit_pins[position], GPIO.LOW) # 현재 자리(COM 핀)를 활성화하여 숫자를 표시
    time.sleep(0.005)
    GPIO.output(digit_pins[position], GPIO.HIGH) # 현재 자리(COM 핀)를 비활성화

def display_number():
    numbers = [1, 2, 3, 4]
    while True:
        for i, num in enumerate(numbers):
            display_digit(num, i)

def main():
    setup()
    try:
        display_number()
    except KeyboardInterrupt:
        pass
    finally:
        GPIO.cleanup()

if __name__ == '__main__':
    main()
