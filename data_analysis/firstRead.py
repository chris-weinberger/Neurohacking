#This is a first example program, we will be expanding this to read the data well
#with this file, we would like to be able to determine at least one feature... 

from pyOpenBCI import OpenBCICyton

def print_raw(sample):
    print(sample.channels_data)

def save_raw(sample):
	f = fopen("raw_data.txt", "w")
	f.write(sample.channels_data)
	f.write("\n")
	fclose(f)

#Set (daisy = True) to stream 16 ch 
board = OpenBCICyton(daisy = False)

board.start_stream(save_raw)

#not sure if this is correct, but this is to start the data filtering. Create a method to save the data to a csv, then we can filter from there
#if(board.filtering_data):
#	stuff here
