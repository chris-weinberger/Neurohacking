from pyfirmata import Arduino, util
import time
# Config:
board = Arduino('/dev/ttyACM0')
servo_one_pin = 2
# board.digital[2].write(1)

board.digital[servo_one_pin].mode = SERVO
board.servo_config(servo_one_pin, min_pulse=544, max_pulse=2400, angle=0)


def setServoAngle(pin, angle):
    board.digital[pin].write(angle)
    time.sleep(0.015)
