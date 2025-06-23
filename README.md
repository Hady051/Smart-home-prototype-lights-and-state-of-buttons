# 🏠 Raspberry Pi Smart Home Prototype

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

This project is a simple **smart home prototype** using a **Raspberry Pi 4**, **LEDs**, a **push button**, and a **Flask-based web server**.

The goal is to:
- Remotely **control home lighting** (represented by LEDs).
- **Monitor the state of a button** (e.g., a doorbell or physical switch) via a browser.

## 🧰 Hardware Components

- Raspberry Pi 4 (any model with GPIO support will work)
- 3 LEDs (connected to GPIO pins 36, 38, 40)
- 1 Push Button (connected to GPIO pin 32 or 40)
- Breadboard and jumper wires
- Resistors (220Ω for LEDs, 10kΩ for pull-down on the button)

## 📁 Project Structure

### 1. `push_button_state.py`

A simple Flask web server that:
- Initializes GPIO pin 40 as input.
- Starts a Flask server.
- Provides an endpoint to read and return the push button state.

#### 🔗 Endpoint:


