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
	<img src="https://raw.githubusercontent.com/HeoYongmin/basic-raspberrypi-2024/main/day01/pull-up.png">

	- 풀 다운
	<img src="https://raw.githubusercontent.com/HeoYongmin/basic-raspberrypi-2024/main/day01/pull-down.png">