
import math


def baseStat(fileName):
	f = open("fileName", "r")

	#loops through the numbers to find the greatest and lowest numbers - eventually, these statistics will be gathered while
	# the data is being streamed so as to avoid needless computation
	greatest = 0
	lowest = 0
	for num in fileName:
		intNum = int(num)
		if(intNum > greatest):
			greatest = intNum
		else if (intNum < lowest):
			lowest = intNum

	range = abs(lowest - greatest)
