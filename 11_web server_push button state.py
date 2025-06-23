from flask import Flask

import RPi.GPIO as GPIO

button_pin = 40

GPIO.setmode(GPIO.BOARD)
GPIO.setup(button_pin, GPIO.IN)

# initialize flask
app = Flask(__name__)

# create some routes
@app.route("/")
def index():
    return"Hello from Flask"

@app.route("/push-button")
def check_push_button_state():
    if GPIO.input(button_pin) == 1:
        return "Button is pressed"
    
    return "Button is not pressed"

# port should be more than 1024 (reserved)
app.run(host = "0.0.0.0", port = 2100)