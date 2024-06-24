from flask import Flask
import RPi.GPIO as GPIO

app = Flask(__name__)

ledPin = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(ledPin, GPIO.OUT)

@app.route("/")
def hello():
    return "<h1>Hello</h1>"

@app.route("/led/<state>")
def led(state):
    if state == "on":
        GPIO.output(ledPin, 0)  
        return "<h1>LED is ON</h1>"
    elif state == "off":
        GPIO.output(ledPin, 1)  
        return "<h1>LED is OFF</h1>"
    elif state == "clear":
        GPIO.cleanup()  
        return "<h1>GPIO Cleanup()</h1>"

if __name__ == "__main__":
    try:
        app.run(host="0.0.0.0", port="7777", debug=True)
    except KeyboardInterrupt:
        GPIO.cleanup()  
