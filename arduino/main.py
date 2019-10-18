import time
import pyfirmata
board = pyfirmata.Arduino('/dev/ttyACM1')  # usb port
servo = board.get_pin('d:9:s')  # pin PWM no 2

__copyright__ = "Copyright 2014, http://letsmakearobot.blogspot.com/"
__version__ = "0.1.0"
__license__ = "GPL"
__email__ = "sebastian.dziak@gmail.com"


def info():
    print("INFO")


def validate(position):
    if not position is None and (float(position) < 0 or float(position) > 255):
        return "Invalid parameter!"


info()
while True:
    value = input('Position (0-255):')
    if value == 'exit': break
    resp = validate(value)
    if resp is None:
        servo.write(int(value))
    else:
        print
        resp

print
"goodbye"
