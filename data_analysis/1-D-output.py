#this will be the first attempt to use the EEG signals to output 1-dimensional control (linear read)

#structured as follows:
# 1) start program
# 2) read signals for 20 seconds to calibrate settings - during this time the user will be prompted to concentrate
# 		on different stimulis
# 3) use calibrated settings to control 1-D output (color on screen or something else)
import math
import pygame, sys
from pygame.locals import *
from pyOpenBCI import OpenBCICyton
import time

#global variable set here that will be altered in calibrate
MEAN = 0

#function to compute the average sample value over a 30 second period
def calibrate(sample):
	startTime = time.time()
	currTime = time.time()
	timeDiff = currTime - startTime

	#first 15 seconds - calibrate using meditation

	print("Focus on your breath during this time")

	for element in sample.channels_data:
		#first gather time statistics 
		currTime = time.time()
		timeDiff = currTime - startTime
		if(timeDiff > 15):
			break
		val = int(element)
		if(intNum > greatest):
			greatest = intNum
		elif (intNum < lowest):
			lowest = intNum

	#seconds 16-30 - calibrate to wild crazy thoughts (can change the metrics later)


	for element in sample.channels_data:
		#gather time statistics
		currTime = time.time()
		timeDiff = currTime - startTime
		if(timeDiff > 30):
			break
		val = int(element)
		if(intNum > greatest):
			greatest = intNum
		elif (intNum < lowest):
			lowest = intNum

	#compute relevant statistics for computing the average value... 
	# if value is above average, rect = red, else rect = blue
	MEAN = (greatest + lowest) / 2

#displays output. If sample is below mean, draws blue rectangle, otherwise draws red rectangle
#test this program next time
def displayOutput(sample):

	for element in sample.channels_data:
		#first gather time statistics 
		val = int(element)
		if val > MEAN:
			redRect()
		else:
			blueRect()


def main():
    pygame.init()

    DISPLAY=pygame.display.set_mode((500,400),0,32)

    WHITE=(255,255,255)
    DISPLAY.fill(WHITE)

	board = OpenBCICyton(daisy = False)

	print("Welcome to 1-D output test!!\n")
	print("Here's what will happen:\n")

	#calibrate the stream
	board.start_stream(calibrate)

	#after calibrating, start stream again to 
	board.start_stream(displayOutput)

    while True:
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

#draws a blue rectangle on the display when called
def blueRect():
	BLUE=(0,0,255)
	pygame.draw.rect(DISPLAY,BLUE,(200,150,100,50))

#draws a red rectangle on the display when called
def redRect():
	RED=(255,0,0)
	pygame.draw.rect(DISPLAY,RED,(200,150,100,50))

#calls main
if __name__ == '__main__':
	main()

	