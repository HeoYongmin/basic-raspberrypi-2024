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