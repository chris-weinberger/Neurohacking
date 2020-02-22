// We should be using this class to do all of our own processing edits
//------------------------------------------------------------------------
//                       Global Variables & Instances
//------------------------------------------------------------------------

DataProcessing_User dataProcessing_user;

//------------------------------------------------------------------------
//                            Classes
//------------------------------------------------------------------------
// Chip Audette used this code in his hexBug implementation of the GUI... we copied what was useful and made out own edits as needed
//DetectedPeak class 
class DetectedPeak { 
    int bin;
    float freq_Hz;
    float rms_uV_perBin;
    float background_rms_uV_perBin;
    float SNR_dB;
    boolean isDetected;
    float threshold_dB;
    
    DetectedPeak() {
      clear();
    }
    
    void clear() {
      bin=0;
      freq_Hz = 0.0f;
      rms_uV_perBin = 0.0f;
      background_rms_uV_perBin = 0.0f;
      SNR_dB = -100.0f;
      isDetected = false;
      threshold_dB = 0.0f;
    }
    
    void copyTo(DetectedPeak target) {
      target.bin = bin;
      target.freq_Hz = freq_Hz;
      target.rms_uV_perBin = rms_uV_perBin;
      target.background_rms_uV_perBin = background_rms_uV_perBin;
      target.SNR_dB = SNR_dB;
      target.isDetected = isDetected;
      target.threshold_dB = threshold_dB;
    }
}


class DataProcessing_User {
    private float fs_Hz;  //sample rate
    private int n_chan;

    //add your own variables here
    final float min_allowed_peak_freq_Hz = 4.0f; //input, for peak frequency detection
    final float max_allowed_peak_freq_Hz = 15.0f; //input, for peak frequency detection
    final float detection_thresh_dB = 6.0f; //how much bigger must the peak be relative to the background
    final float[] processing_band_low_Hz = {4.0,  6.5,  9,  13.5}; //lower bound for each frequency band of interest (2D classifier only)
    final float[] processing_band_high_Hz = {6.5,  9,  12, 16.5};  //upper bound for each frequency band of interest
    DetectedPeak[] detectedPeak;  //output per channel, from peak frequency detection
    DetectedPeak[] peakPerBand;
    Arduino arduino;
    //class constructor
    DataProcessing_User(int NCHAN, float sample_rate_Hz, Arduino duino) {
        n_chan = NCHAN;
        fs_Hz = sample_rate_Hz;
        arduino = duino;

        detectedPeak = new DetectedPeak[nchan];
        for (int Ichan=0;Ichan<nchan;Ichan++) detectedPeak[Ichan]=new DetectedPeak();
    
        int nBands = processing_band_low_Hz.length;
        peakPerBand = new DetectedPeak[nBands];
        for (int Iband=0;Iband<nBands;Iband++) peakPerBand[Iband] = new DetectedPeak();
    }

    //add some functions here...if you'd like

    //here is the processing routine called by the OpenBCI main program...update this with whatever you'd like to do
    //data_new_uV holds raw bio data that is new since the last call
    //data_long_uV holds a longer piece of buffered EEG data, of same length as will be plotted on the screen
    //data_forDisplay_uV - this data has been filtered and is ready for plotting on the screen
    //fftData holds the FFT of the latest data
    public void process(float[][] data_newest_uV, float[][] data_long_uV, float[][] data_forDisplay_uV, 
                    FFT[] fftData) {   //holds the FFT (frequency spectrum) of the latest data

        //for example, you could loop over each EEG channel to do some sort of time-domain processing
        //using the sample values that have already been filtered, as will be plotted on the display
        float EEG_value_uV;


        //user functions here...
        int Ichan = 2-1;  //which channel to act on
        if (fftData != null) findPeakFrequency(fftData,Ichan); //find the frequency for each channel with the peak amplitude

        //REMOVED FOR NOW... I can't figure out what this does so I took it out
        // if (useClassfier_2DTraining) {
        //     //new processing for improved selectivity
        //     if (fftData != null) findBestFrequency_2DTraining(fftData,Ichan);      
        // }

        //possibly add section to print information on current Ichan object
        println("channel information: ");
        println(detectedPeak[Ichan].isDetected);
      
        //issue new command to the Hex Bug, if there is a peak that was detected
        if (detectedPeak[Ichan].isDetected) {
            println("I'm inside here - for debugging\n");                               //for debugging purposes.... where is the isDetected variable ever set?
            String txt = "";
            if (detectedPeak[Ichan].freq_Hz < processing_band_high_Hz[1-1]) {
                arduino.right();txt = "Right";
            } else if (detectedPeak[Ichan].freq_Hz < processing_band_high_Hz[2-1]) {
                arduino.left();txt = "Left";
            } else if (detectedPeak[Ichan].freq_Hz < processing_band_high_Hz[3-1]) {
                arduino.forward(); txt = "Forward";
            } else if (detectedPeak[Ichan].freq_Hz < processing_band_high_Hz[4-1]) {
                //the other way to get a LEFT command! 
                arduino.left();txt = "Left";
            }

            //print some output to help debug.... remove later if we want to 
            println("EEG_Processing_User: " + txt + "!, Chan " + (Ichan+1) + ", peak = " + detectedPeak[Ichan].rms_uV_perBin + " uV at " 
                + detectedPeak[Ichan].freq_Hz + " Hz with background at = " + detectedPeak[Ichan].background_rms_uV_perBin 
                + ", SNR (dB) = " + detectedPeak[Ichan].SNR_dB);        
        
        }
    }

    //Thought... I might want to write a calibrate function to change the SNR values to something relevant for the user, so if they're hovering 
    // around 50/60, they can still control the robot... make it relative to where they are already

    //also - another feature to add is for the user to select the serial output for arduino... just add a button and a list dropdown that can be updated

    // void calibrateSNR(){

    // }


    void findPeakFrequency(FFT[] fftData,int Ichan) {
    
        //loop over each EEG channel and find the frequency with the peak amplitude
        float FFT_freq_Hz, FFT_value_uV;
        //for (int Ichan=0;Ichan < nchan; Ichan++) {
      
        //clear the data structure that will hold the peak for this channel
        detectedPeak[Ichan].clear();
      
        //loop over each frequency bin to find the one with the strongest peak
        int nBins =  fftData[Ichan].specSize();
        for (int Ibin=0; Ibin < nBins; Ibin++){
            FFT_freq_Hz = fftData[Ichan].indexToFreq(Ibin); //here is the frequency of htis bin
        
            //is this bin within the frequency band of interest?
            if ((FFT_freq_Hz >= min_allowed_peak_freq_Hz) && (FFT_freq_Hz <= max_allowed_peak_freq_Hz)) {
                //we are within the frequency band of interest
          
                //get the RMS voltage (per bin)
                FFT_value_uV = fftData[Ichan].getBand(Ibin) / ((float)nBins); 
           
                //decide if this is the maximum, compared to previous bins for this channel
                if (FFT_value_uV > detectedPeak[Ichan].rms_uV_perBin) {
                    //this is bigger, so hold onto this value as the new "maximum"
                    detectedPeak[Ichan].bin  = Ibin;
                    detectedPeak[Ichan].freq_Hz = FFT_freq_Hz;
                    detectedPeak[Ichan].rms_uV_perBin = FFT_value_uV;
                } 
          
            } //close if within frequency band
        } //close loop over bins
   
        //loop over the bins again (within the sense band) to get the average background power, excluding the bins on either side of the peak
        float sum_pow=0.0;
        int count=0;
        for (int Ibin=0; Ibin < nBins; Ibin++){
            FFT_freq_Hz = fftData[Ichan].indexToFreq(Ibin);
            if ((FFT_freq_Hz >= min_allowed_peak_freq_Hz) && (FFT_freq_Hz <= max_allowed_peak_freq_Hz)) {
                if ((Ibin < detectedPeak[Ichan].bin - 1) || (Ibin > detectedPeak[Ichan].bin + 1)) {
                    FFT_value_uV = fftData[Ichan].getBand(Ibin) / ((float)nBins);  //get the RMS per bin
                    sum_pow+=pow(FFT_value_uV,2.0f);
                    count++;
                }
            }
        }
        //compute mean
        detectedPeak[Ichan].background_rms_uV_perBin = sqrt(sum_pow / count);
      
        //decide if peak is big enough to be detected
        detectedPeak[Ichan].SNR_dB = 20.0f*(float)java.lang.Math.log10(detectedPeak[Ichan].rms_uV_perBin / detectedPeak[Ichan].background_rms_uV_perBin);
        if (detectedPeak[Ichan].SNR_dB >= detection_thresh_dB) {
            detectedPeak[Ichan].threshold_dB = detection_thresh_dB;
            detectedPeak[Ichan].isDetected = true;
        } 
    //} // end loop over channels    
    } //end method findPeakFrequency
};
