from flask import Flask

import RPi.GPIO as GPIO

button_pin = 32
led_pin_list = [36, 38, 40]

GPIO.setmode(GPIO.BOARD)
GPIO.setup(button_pin, GPIO.IN)
for pin in led_pin_list:
    GPIO.setup(pin, GPIO.OUT)

for pin in led_pin_list:
    GPIO.output(pin, 0)
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

@app.route("/led/<int:led_pin>/state/<int:led_state>")
def trigger_led(led_pin, led_state):
    if not led_pin in led_pin_list:
        return "Wrong GPIO number: " + str(led_pin)
    if led_state == 0:
        GPIO.output(led_pin, 0)
    elif led_state == 1:
        GPIO.output(led_pin, 1)
    else:
        return "State must be 0 or 1"
    return "WOW"
# port should be more than 1024 (reserved)
if __name__ == '__main__':
    app.run(host = "0.0.0.0", port = 2100, threaded = False, debug = True)

GPIO.cleanup()