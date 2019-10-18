from pyfirmata import Arduino, util
from time import sleep

board = Arduino('/dev/ttyACM0')
print
"Start blinking D13"
while True:
    board.digital[13].write(1)
    sleep(0.5)
    board.digital[13].write(0)
    sleep(0.5)
