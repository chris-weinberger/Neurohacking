
import math


def baseStat(fileName):
	f = open(fileName, "r")

	#loops through the numbers to find the greatest and lowest numbers - eventually, these statistics will be gathered while
	# the data is being streamed so as to avoid needless computation
	greatest = 0
	lowest = 0
	for num in fileName:
		intNum = int(num)
		if(intNum > greatest):
			greatest = intNum
		elif (intNum < lowest):
			lowest = intNum

	data_range = abs(lowest - greatest)

	return [lowest, greatest, data_range]


def main():
	dataInfo[3] = baseStat("raw_data.txt")
	print("first data: %d", dataInfo[1])

main()