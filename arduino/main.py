from pyfirmata import Arduino, util

# Config:
board = Arduino('/dev/ttyACM0')
board.digital[2].write(1)

board.servo_config(pin, min_pulse=544, max_pulse=2400, angle=0)
#def moveOneTo(pin):
