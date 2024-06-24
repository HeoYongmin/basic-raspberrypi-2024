# URL 접속을 /led/on, /led/off로 접속하면 led를 on, off하는 웹페이지를 만들자
from flask import Flask
import RPi.GPIO as GPIO

app = Flask(__name__)

ledPin = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin, GPIO.OUT)

@app.route("/led/on")
def led_on():
    GPIO.output(ledPin, 1) 
    return "<h1>LED is ON</h1>"

@app.route("/led/off")
def led_off():
    GPIO.output(ledPin, 0)
    return "<h1>LED is OFF</h1>"

if __name__ == "__main__":
    try:
        app.run(host="0.0.0.0", port="7777", debug=True)
    except KeyboardInterrupt:
        GPIO.cleanup()  
