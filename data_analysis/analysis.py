
import math


def baseStat(fileName):
	f = open(fileName, "r")

	#loops through the numbers to find the greatest and lowest numbers - eventually, these statistics will be gathered while
	# the data is being streamed so as to avoid needless computation
	greatest = 0
	lowest = 0
	for num in f:
		intNum = int(num)
		print(num)
		if(intNum > greatest):
			greatest = intNum
		elif (intNum < lowest):
			lowest = intNum
	print("lowest: ", lowest)
	print("greatest: ", greatest)


	data_range = abs(lowest - greatest)
	print("range: ", data_range)

	return [lowest, greatest, data_range]


def main():
	dataInfo = baseStat("raw_data.txt")
	print("first data: ", dataInfo[1])

main()