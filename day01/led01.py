import RPi.GPIO as GPIO
import time

# 각 LED의 GPIO 핀 정의
red = 21
green = 6
blue = 5

# GPIO 모드를 BCM으로 설정
GPIO.setmode(GPIO.BCM)

# 각 GPIO 핀을 출력으로 설정
GPIO.setup(red, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)

try:
    while True:
        # 빨간색 LED 켜기
        GPIO.output(red, True)
        GPIO.output(green, False)
        GPIO.output(blue, False)
        time.sleep(1)  # 1초 대기

        # 초록색 LED 켜기
        GPIO.output(red, False)
        GPIO.output(green, True)
        GPIO.output(blue, False)
        time.sleep(1)  # 1초 대기

        # 파란색 LED 켜기
        GPIO.output(red, False)
        GPIO.output(green, False)
        GPIO.output(blue, True)
        time.sleep(1)  # 1초 대기

        # 모든 LED 끄기
        GPIO.output(red, False)
        GPIO.output(green, False)
        GPIO.output(blue, False)
        time.sleep(1)  # 1초 대기

except KeyboardInterrupt:  # Ctrl + C 잡기
    GPIO.cleanup()  # GPIO 설정 정리
