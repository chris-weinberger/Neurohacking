README

This project is working to control a simple robotic arm using neural signals. We are interfacing an OpenBCI Cyton EEG with an Arduino Uno. The project is split into two tracks: data analysis and arduino/robot development. 

The data analysis track is working to get data and from the EEG, filter it, and provide an output command for the arduino. The robotics track will take that output signal and use it to control servos and motors. 

Dependencies: pyOpenBCI, numpy, pyFirmata