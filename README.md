Smart Home Prototype: Web-Controlled GPIO with Raspberry Pi
This project demonstrates a basic smart home prototype using a Raspberry Pi 4, Python Flask web server, and simple electronic components (buttons and LEDs). The goal is to control LEDs and monitor the state of a push button remotely via a web interface.

Table of Contents
Introduction

Features

Hardware Requirements

Software Requirements

Setup Instructions

Hardware Connections

Software Installation

Running the Servers

Web Interface Usage

File Descriptions

Troubleshooting

Future Enhancements

1. Introduction
This repository contains Python scripts that turn your Raspberry Pi 4 into a simple web server. This server exposes endpoints to read the state of a connected push button and to control the on/off state of multiple LEDs. This serves as a foundational step for building more complex IoT and smart home applications.

2. Features
Web-based Control: Control LEDs (turn on/off) from any web browser.

Real-time Button Status: Monitor the state of a physical push button from a web page.

Simple RESTful API: Easy-to-understand URL structure for interactions.

Scalable: Easily extendable to include more sensors, actuators, and complex logic.

3. Hardware Requirements
Raspberry Pi 4 (or compatible Raspberry Pi model with GPIO pins)

MicroSD Card (with Raspberry Pi OS installed)

Power Supply for Raspberry Pi

Breadboard (optional, for easier prototyping)

Jumper Wires

Push Button

LEDs (e.g., 1-3 LEDs for demonstration)

Resistors (e.g., 220 Ohm for LEDs to protect them)

4. Software Requirements
Raspberry Pi OS (or any Debian-based Linux distribution for Raspberry Pi)

Python 3

Flask library

RPi.GPIO library

5. Setup Instructions
Hardware Connections
Important: Always power off your Raspberry Pi before making or changing any hardware connections. Refer to the Raspberry Pi GPIO pinout diagram for exact pin numbers. The provided scripts use BOARD pin numbering.

For 12_web_server_led_state.py:

Push Button:

Connect one leg of the push button to GPIO 32 (BOARD pin).

Connect the other leg of the push button to a GND pin.

(Optional but recommended for stability): Add a pull-up or pull-down resistor if not using internal pull-up/down resistors. The RPi.GPIO library can handle internal pull-ups.

LEDs:

Connect the anode (longer leg) of the first LED to GPIO 36 (BOARD pin) via a current-limiting resistor (e.g., 220 Ohm).

Connect the cathode (shorter leg) of the first LED to a GND pin.

Repeat for the second LED on GPIO 38 (BOARD pin) and the third LED on GPIO 40 (BOARD pin).

For 11_web_server_push_button_state.py:

Push Button:

Connect one leg of the push button to GPIO 40 (BOARD pin).

Connect the other leg of the push button to a GND pin.

Software Installation
Update Raspberry Pi OS:

sudo apt update
sudo apt upgrade

Install Python pip (if not already installed):

sudo apt install python3-pip

Install Flask:

pip3 install Flask

Install RPi.GPIO:

pip3 install RPi.GPIO

Transfer Files: Copy 12_web_server_led_state.py and 11_web_server_push_button_state.py to your Raspberry Pi, for example, in a directory like /home/pi/smart_home_prototype/.

Running the Servers
Note: You cannot run both 11_web_server_push_button_state.py and 12_web_server_led_state.py simultaneously on the same port (2100) as they would conflict. The 12_web_server_led_state.py script includes the push button functionality, so it's generally sufficient for demonstrating both features.

Open a Terminal on your Raspberry Pi.

Navigate to the project directory:

cd /home/pi/smart_home_prototype/

Run the main server script (recommended):

python3 12_web_server_led_state.py

You should see output indicating that the Flask server is running on http://0.0.0.0:2100/.

6. Web Interface Usage
Once the Flask server is running on your Raspberry Pi, you can access it from any device on the same local network using your Raspberry Pi's IP address.

Find your Raspberry Pi's IP address:
Open a terminal on your Raspberry Pi and type:

hostname -I

Let's assume your Raspberry Pi's IP address is 192.168.1.100.

Open a web browser on a computer or smartphone connected to the same network and navigate to:

Home Page: http://192.168.1.100:2100/ (will display "Hello from Flask")

Check Push Button State: http://192.168.1.100:2100/push-button

This page will display "Button is pressed" or "Button is not pressed" based on the physical button's state.

Control LEDs:

Turn LED ON: http://192.168.1.100:2100/led/<LED_PIN>/state/1

Replace <LED_PIN> with the GPIO pin number of the LED you want to control (e.g., 36, 38, or 40).

Example: To turn on the LED connected to GPIO 36: http://192.168.1.100:2100:2100/led/36/state/1

Turn LED OFF: http://192.168.1.100:2100/led/<LED_PIN>/state/0

Example: To turn off the LED connected to GPIO 36: http://192.168.1.100:2100/led/36/state/0

7. File Descriptions
**12_web_server_led_state.py**:

This is the primary Flask web server script.

Initializes GPIO pins for one input (button) and multiple outputs (LEDs).

Sets up routes:

/: Simple welcome message.

/push-button: Reports the current state of the button connected to button_pin (GPIO 32).

/led/<int:led_pin>/state/<int:led_state>: Controls the state of an LED. It expects the led_pin to be one of the predefined led_pin_list ([36, 38, 40]) and led_state to be 0 (off) or 1 (on).

Runs the Flask application on 0.0.0.0:2100.

Includes GPIO.cleanup() to reset GPIOs on script exit (when run with debug=True this might not always execute, for production, consider a try-finally block).

**11_web_server_push_button_state.py**:

A simpler Flask web server script focusing solely on the push button state.

Initializes GPIO pin 40 for button input.

Sets up routes:

/: Simple welcome message.

/push-button: Reports the current state of the button connected to button_pin (GPIO 40).

Runs the Flask application on 0.0.0.0:2100.

8. Troubleshooting
"Wrong GPIO number" error: Ensure you are using one of the specified LED pins (36, 38, 40) in your URL for the /led route.

LEDs not lighting up:

Check your wiring carefully (anode/cathode, resistor).

Ensure the LED pin in the URL matches your wiring.

Verify the resistor value is appropriate.

Button state not changing:

Check button wiring.

Ensure the button is correctly connected to the specified button_pin.

"Connection Refused" or page not loading:

Verify your Raspberry Pi is powered on and connected to the network.

Confirm the Flask server script (12_web_server_led_state.py) is running in the terminal.

Double-check the Raspberry Pi's IP address and the port (2100) in the URL.

Make sure no firewall is blocking port 2100 on your Raspberry Pi.

GPIO warnings/errors: If you get "RuntimeWarning: This channel is already in use," it means the GPIO pins were not cleanly released from a previous run. This is often handled by GPIO.cleanup() but can occur if the script was stopped abruptly. Restarting the Pi often resolves this, or manually calling GPIO.cleanup() in a separate script before running your main one.

9. Future Enhancements
Interactive Web UI: Instead of just direct URL access, create a simple HTML page with buttons and status indicators to provide a more user-friendly interface.

Authentication: Add user authentication to secure your smart home control.

Database Integration: Store historical data (e.g., button press times, LED usage).

MQTT Integration: For more robust IoT communication, integrate an MQTT broker and client for device-to-device messaging.

Error Handling: Implement more robust error handling within the Flask application.

Multi-threading/Asynchronous Operations: For more complex scenarios, consider using threading or asyncio to prevent blocking the web server during long-running GPIO operations.

Systemd Service: Configure the Flask app to run as a systemd service, so it automatically starts on boot and can be managed easily.
