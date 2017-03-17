import RPi.GPIO as gpio
import robot
import time
import sys

gpio.setmode(gpio.BOARD)

# initialize pins
gpio.setup(7, gpio.OUT)
gpio.setup(11, gpio.OUT)
gpio.setup(13, gpio.OUT)
gpio.setup(15, gpio.OUT)

def listen():
	key = event.char
	if (key.lower() == "w"):
		robot.forward()
	else:
		gpio.cleanup()
	time.sleep(0.025)
gpio.cleanup()

import tty
import termios

orig_settings = termios.tcgetattr(sys.stdin)

tty.setraw(sys.stdin)
x = 0
while True: # ESC
    key = sys.stdin.read(1)[0]
    if (key == chr(119)):
	#robot.forward()
	print("W")
    elif (key == char(27)):
	break
	gpio.cleanup()

    time.sleep(0.025)

termios.tcsetattr(sys.stdin, termios.TCSADRAIN, orig_settings)   
