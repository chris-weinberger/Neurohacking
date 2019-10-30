#This is a first example program, we will be expanding this to read the data well
#with this file, we would like to be able to determine at least one feature

#Currently, the stream data from the OpenBCI is being saved to a file called raw_data.txt

#next updates: we need to accurately see 

from pyOpenBCI import OpenBCICyton
import time


def print_raw(sample):
    print(sample.channels_data)


#function that saves sample stream data to a csv file... currently doesn't format correctly
def save_raw_csv(sample):
	f = open("raw_data.csv", "a") #write in append mode so it doesn't delete the previous content
	#f.write(sample.channels_data)
	count = 0
	for element in sample.channels_data:
		f.write(str(element))
		f.write(" ")
		if count % 8 == 0:
			f.write("\n")
		count = count + 1

#function that saves sample stream data to txt file
def save_raw_txt(sample):
	f = open("raw_data_new.txt", "a")
	count = 0
	for element in sample.channels_data:
		f.write(str(element))
		f.write(" ")
		if count % 8 == 0:
			f.write("\n")
		count = count + 1
	#print(sample.channels_data)

#Set (daisy = True) to stream 16 ch 
board = OpenBCICyton(daisy = False)

board.start_stream(save_raw_txt)
f.close()

#not sure if this is correct, but this is to start the data filtering. Create a method to save the data to a csv, then we can filter from there
#if(board.filtering_data):
#	stuff here