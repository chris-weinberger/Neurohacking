import pyfirmata
import time

board = pyfirmata.Arduino('/dev/cu.usbmodem14401')
test = board.servo_config(3)
servo = board.get_pin('d:3:s')
servo.write(180)