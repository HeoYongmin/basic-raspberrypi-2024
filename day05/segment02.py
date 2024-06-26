# 버튼을 누를때마다 1씩 카운트
import RPi.GPIO as GPIO
import time

buttonPin = 12
segmentPin = {
    'a': 20,
    'b': 24,
    'c': 19,
    'd': 13,
    'e': 6,
    'f': 21,
    'g': 26
}

digit = [
    [1, 1, 1, 1, 1, 1, 0],  
    [0, 1, 1, 0, 0, 0, 0],  
    [1, 1, 0, 1, 1, 0, 1],  
    [1, 1, 1, 1, 0, 0, 1],  
    [0, 1, 1, 0, 0, 1, 1],  
    [1, 0, 1, 1, 0, 1, 1],  
    [1, 0, 1, 1, 1, 1, 1],  
    [1, 1, 1, 0, 0, 0, 0],  
    [1, 1, 1, 1, 1, 1, 1],  
    [1, 1, 1, 1, 0, 1, 1]   
]

count = 0
debounceTime = 0.05 # 버튼 노이즈 방지

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(buttonPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    for pin in segmentPin.values():
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.LOW)
    displayDigit(count)

def displayDigit(num):
    pattern = digit[num]
    for i, segment in enumerate(['a', 'b', 'c', 'd', 'e', 'f', 'g']):
        GPIO.output(segmentPin[segment], pattern[i])

def loop():
    global count    # 함수 내에서 젼역변수 count 사용
    lastButtonState = GPIO.input(buttonPin) # 루프 시작 전 버튼의 초기상태 읽음
    while True:
        currentButtonState = GPIO.input(buttonPin)  # 현재 버튼 상태 읽음
        if currentButtonState == GPIO.HIGH and lastButtonState == GPIO.LOW:
            time.sleep(debounceTime) 
            if GPIO.input(buttonPin) == GPIO.HIGH:
                count = (count + 1) % 10  
                displayDigit(count)
        lastButtonState = currentButtonState    # 현재 버튼 상태를 다음 반복을 위해 저장
        time.sleep(0.01) 

if __name__ == '__main__':
    try:
        setup()
        loop()
    except KeyboardInterrupt:
        GPIO.cleanup()
