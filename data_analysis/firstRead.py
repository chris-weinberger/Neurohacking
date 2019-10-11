#This is a first example program, we will be expanding this to read the data well
#with this file, we would like to be able to determine at least one feature

#Currently, the stream data from the OpenBCI is being saved to a file called raw_data.txt

from pyOpenBCI import OpenBCICyton
import time


def print_raw(sample):
    print(sample.channels_data)


#right now, this function is only writing like 6 ints to a file. Edit it so it adds new lines
def save_raw(sample):
	f = open("raw_data.txt", "a") #write in append mode so it doesn't delete the previous content
	#f.write(sample.channels_data)
	count = 0
	for element in sample.channels_data:
		f.write(str(element))
		if count % 8 == 0:
			f.write("\n")
		count = count + 1

	#print(sample.channels_data)

#Set (daisy = True) to stream 16 ch 
board = OpenBCICyton(daisy = False)

board.start_stream(save_raw)
f.close()

#not sure if this is correct, but this is to start the data filtering. Create a method to save the data to a csv, then we can filter from there
#if(board.filtering_data):
#	stuff here
