# basic-raspberrypi-2024
라즈베리파이

## 1일차 (2024-06-20)
- Python
- GPIO 설정함수
	- GPIO.setmode(GPIO.BOARD)-wpi
	- GPIO.setmode(GPIO.BCM)-BCM
	- GPIO.setup(channel, GPIO.mode)
	- channel: 핀번호, mode:IN/OUT
	- GPIO.cleanup()
- GPIO 출력함수
	- GPIO.output(channel, state)
	- channel: 핀번호, state: HIGH/LOW or 1/0 or True/False
- GPIO 입력함수
	- GPIO.input(channel)
	- channel: 핀번호, 반환값: H/L or 1/0 or T/F
- 시간지연 함수
	- time.sleep(secs)

- 풀업
	<img src="https://raw.githubusercontent.com/HeoYongmin/basic-raspberrypi-2024/main/day01/pull-up.png" width=730>


- 풀 다운
	<img src="https://raw.githubusercontent.com/HeoYongmin/basic-raspberrypi-2024/main/day01/pull-down.png" width=730>

## 2일차 (2024-06-21)
- 가상환경 만들기
	- python -m venv env

- 가상환경 들어가기
	- source ./env/bin/activate

- 가상환경 빠져나오기
	- deactivate

- 설치
	- sudo git clone https://github.com/WiringPi/WiringPi
	- sudo ./build
	- gpio readall

## 3일차(2024-06-24)
- 새로운 가상환경 만들기
	- python -m venv --system-site-packages env

## 4일차(2024-06-25)
- html을 이용한 led on,off 제어 웹서버 만들기
	- <img src="https://raw.githubusercontent.com/HeoYongmin/basic-raspberrypi-2024/main/day04/web.png" width=730>

- 버튼을 눌러 사진 촬영 가능한 사진기 만들기
	- <img src="https://raw.githubusercontent.com/HeoYongmin/basic-raspberrypi-2024/main/day04/cam.png" width=730>

- 세그먼트 구조와 외형
	- <img src="https://raw.githubusercontent.com/HeoYongmin/basic-raspberrypi-2024/main/images/ri001.png" width=730>

- 7세그먼트 0~9 숫자 1초 간격으로 표시

## 4일차(2024-06-26)
- 버튼을 누를때마다 숫자 1씩 카운트

- 세그먼트에 1234 표시

- 세그먼트 9999까지 카운트

## 06.27 ~ 07.01 다낭으로 휴가

## 8일차(2024-07-02)
- 개인 프로젝트

## 9일차(2024-07-03)
- 개인 프로젝트

- <img src="https://raw.githubusercontent.com/HeoYongmin/basic-raspberrypi-2024/main/project/design.png">

- https://github.com/HeoYongmin/basic-raspberrypi-2024/assets/158007383/729d6b22-e2ad-4e90-8fa1-81264a7fb7e6



- https://github.com/HeoYongmin/basic-raspberrypi-2024/assets/158007383/def0000a-ccbd-4d67-8b13-e57b30aa0b10

- LED 제어
	- 사용자가 GUI에서 빨간색, 초록색, 파란색 LED를 각각 켜고 끌 수 있음
	- 구현 방법: PyQt5의 QPushButton을 사용하여 각 LED를 제어하고, RPi.GPIO를 이용해 GPIO 핀을 제어

- 세그먼트 디스플레이
	- 7세그먼트 디스플레이를 사용하여 숫자를 표시
	- 구현 방법: PyQt5의 LCDNumber를 사용하여 현재 숫자를 표시하고, 타이머를 이용하여 카운트 업 기능을 구현했습니다. RPi.GPIO를 이용해 각각의 세그먼트를 제어

- 카메라 촬영
	- 'Camera' 버튼을 클릭하면 현재 시간을 기반으로 파일명을 생성하여 Raspberry Pi 카메라로 사진을 촬영
	- 구현 방법: PyQt5의 QPushButton을 사용하여 버튼 클릭 이벤트를 처리하고, picamera2를 이용해 사진을 촬영하고 저장

- 카운터 기능
	- 사용자가 'Count' 버튼을 클릭하면 1초마다 숫자가 증가하는 카운터 기능을 제공
	- 구현 방법: QTimer를 사용하여 1초마다 update_count 함수를 호출하여 숫자를 증가시키고, PyQt5의 LCDNumber를 통해 실시간으로 숫자를 표시
