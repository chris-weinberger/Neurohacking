import pyfirmata
import time

#board = pyfirmata.Arduino('/dev/cu.usbmodem14401')

robot = {
    "base": {
        "pin": 3,
        "location": 0},
    "shoulder": {
        "pin": 4,
        "location": 0},
    "elbow": {
        "pin": 5,
        "location": 0},
    "wrist": {
        "pin": 5,
        "location": 0},
    "claw": {
        "pin": 5,
        "location": 0},
    }

# while True:
#     board.digital[13].write(1)
#     time.sleep(1)
#     board.digital[13].write(0)
#     time.sleep(1)


# noinspection PyUnreachableCode
class Robot:
    def __init__(self, arm):
        print("Control initiated")
        self.arm = arm

    def moveToPoint(self, x, y, z):
        print("Moving to point (" + x + "," + y + "," + z + ").")
        # TODO: Accomplish using BreezyArm

    def moveComponent(self, servo, angle):
        print("Moving " + servo + "to" + angle + ".")
        # Move servo
        robot[servo]["location"] = angle

    def __str__(self):
        message = ""
        for component in robot:
            message += component + ": "
            for attribute in component:
                message += attribute + " "
            message += "\n"
        return message
