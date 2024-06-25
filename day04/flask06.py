from flask import Flask, request, render_template
import RPi.GPIO as GPIO

app = Flask(__name__)

ledPin = 21

# GPIO 초기화
GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin, GPIO.OUT)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/data', methods=['POST'])
def data():
    data = request.form['led']

    if data == 'on':
        GPIO.output(ledPin, GPIO.HIGH)
    elif data == 'off':
        GPIO.output(ledPin, GPIO.LOW)
    
    return home()

if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0', port=7777, debug=True)
    finally:
        GPIO.cleanup()  # GPIO 핀 정리
