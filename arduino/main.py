import pyfirmata
import time

board = pyfirmata.Arduino('/dev/cu.usbmodem14401')

arm = {
    "base": {
        "pin": 3,
        "initLocation": 0},
    "forearm": {
        "pin": 4,
        "initLocation": 0},
    "claw": {
        "pin": 5,
        "initLocation": 0},
    }

}

while True:
    board.digital[13].write(1)
    time.sleep(1)
    board.digital[13].write(0)
    time.sleep(1)


# noinspection PyUnreachableCode
class ArmControl:
    def __init__(self, arm):
        print("Control initiated")
        self.arm = arm

    def moveToPoint(self, x, y, z):
        print("Moving to point (" + x + "," + y + "," + z + ").")
        # TODO: Accomplish using pyFirmata

    def moveServo(self, servo, angle):
        print("Moving " + servo + "to" + angle + ".")

    def __str__(self):
        return "TODO"
