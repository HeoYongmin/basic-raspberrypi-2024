import sys
import time
import datetime
import RPi.GPIO as GPIO
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
from PyQt5.QtCore import QTimer
from picamera2 import Picamera2, Preview

# LED 및 세그먼트 초기화
led_pins = {
    'red': 5,
    'green': 4,
    'blue': 12
}

segments = [20, 24, 19, 13, 6, 21, 26]  # a, b, c, d, e, f, g 핀
digits = [18, 23, 25, 22]  # 4자리 디스플레이 핀
num = [
    [1, 1, 1, 1, 1, 1, 0],  # 0
    [0, 1, 1, 0, 0, 0, 0],  # 1
    [1, 1, 0, 1, 1, 0, 1],  # 2
    [1, 1, 1, 1, 0, 0, 1],  # 3
    [0, 1, 1, 0, 0, 1, 1],  # 4
    [1, 0, 1, 1, 0, 1, 1],  # 5
    [1, 0, 1, 1, 1, 1, 1],  # 6
    [1, 1, 1, 0, 0, 0, 0],  # 7
    [1, 1, 1, 1, 1, 1, 1],  # 8
    [1, 1, 1, 1, 0, 1, 1],  # 9
]

# GPIO 설정 초기화
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# LED 및 세그먼트 초기화
for color, pin in led_pins.items():
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, True)

for segment in segments:
    GPIO.setup(segment, GPIO.OUT)
    GPIO.output(segment, 0)

for digit in digits:
    GPIO.setup(digit, GPIO.OUT)
    GPIO.output(digit, 1)

# PyQt5로 생성한 UI 파일 불러오기
form_class = uic.loadUiType("/home/pi/Work/project/main.ui")[0]

# Picamera2 객체 생성
picam2 = Picamera2()
config = picam2.create_still_configuration()
picam2.configure(config)
picam2.start()

# 메인 윈도우 클래스 정의
class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # LCDNumber 초기화
        self.lcdNumber.display(0)

        # LED 초기화
        self.setup_led()

        # 버튼 클릭 이벤트 연결
        self.RedButton.clicked.connect(lambda: self.toggle_led('red'))
        self.GreenButton.clicked.connect(lambda: self.toggle_led('green'))
        self.BlueButton.clicked.connect(lambda: self.toggle_led('blue'))
        self.OffButton.clicked.connect(lambda: self.toggle_led('off'))

        self.CountButton.clicked.connect(self.start_counting)
        self.StopButton.clicked.connect(self.stop_counting)
        self.ResetButton.clicked.connect(self.reset_counter)

        self.CameraButton.clicked.connect(self.take_picture)  # 카메라 버튼 클릭 시 촬영

        # 카운터 초기화
        self.count = 0
        self.counting = False

        # QTimer 초기화 및 연결
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_count)

    def setup_led(self):
        # LED 및 세그먼트 초기화 함수
        for pin in led_pins.values():
            GPIO.output(pin, True)

        for segment in segments:
            GPIO.output(segment, 0)

        for digit in digits:
            GPIO.output(digit, 1)

    def toggle_led(self, color):
        # LED 제어 함수
        for pin in led_pins.values():
            GPIO.output(pin, True)

        if color == 'red':
            GPIO.output(led_pins['red'], False)
        elif color == 'green':
            GPIO.output(led_pins['green'], False)
        elif color == 'blue':
            GPIO.output(led_pins['blue'], False)
        elif color == 'off':
            for pin in led_pins.values():
                GPIO.output(pin, True)

    def start_counting(self):
        # 카운터 시작 함수
        self.counting = True
        self.timer.start(1000)  # 1초마다 타이머 이벤트 발생

    def stop_counting(self):
        # 카운터 정지 함수
        self.counting = False
        self.timer.stop()

    def reset_counter(self):
        # 카운터 초기화 함수
        self.count = 0
        self.display_number(self.count)
        self.lcdNumber.display(self.count)

    def update_count(self):
        # 카운터 업데이트 함수
        self.display_number(self.count)
        self.lcdNumber.display(self.count)
        self.count += 1

    def display_number(self, number):
        # 세그먼트 디스플레이에 숫자 표시하는 함수
        for i in range(4):
            digit_value = number % 10
            number //= 10
            for j in range(7):
                GPIO.output(segments[j], num[digit_value][j])
            GPIO.output(digits[3 - i], 0)
            time.sleep(0.001)
            GPIO.output(digits[3 - i], 1)

    def take_picture(self):
        # 카메라 촬영 함수
        now = datetime.datetime.now()
        fileName = now.strftime('%Y-%m-%d_%H-%M-%S')
        picam2.capture_file(f"/home/pi/Pictures/{fileName}.jpg")
        print(f"사진 촬영 완료: {fileName}.jpg")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    sys.exit(app.exec_())