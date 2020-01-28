import Numpy as np
from pyOpenBCI import OpenBCICyton


Nfft = 256 #set resolution oof FFT. Use N = 256 for normal, N= 512 for Mu waves

fftBuff = []

fftBuff[]


#function based on OpenBCI_GUI code... I need to inspect it very closely to try and figure out what's going pnm
def process(sample):
	int Nfft = 0; #this is 

	nChan = len(sample.channels_data)
	#loop over each EEG channel
	for chan in range(nChan):
		