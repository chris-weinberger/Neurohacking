//Basic test to send Serial command to Arduino
//Should turn on/off LED from command

import processing.serial.*;

Serial myPort;  // Create object from Serial class
boolean LEDon;

void setup() 
{
  size(200,200); //make our canvas 200 x 200 pixels big
  printArray(Serial.list());
  String portName = Serial.list()[7]; //change the 0 to a 1 or 2 etc. to match your port
  LEDon = false; //turn LED off to start
  myPort = new Serial(this, portName, 9600);
}

void draw() {
  if (mousePressed == true) 
  {                           //if we clicked in the window
    if(LEDon)   //If LED is currently on, turn it off
    {
        myPort.write('-');   //send a -, turn off LED
        LEDon = false;
        print("LED off!\n");
    }
    else        //LED is off, turn it on
    {
        myPort.write('+');  //send a +, turns on LED
        LEDon = true;
        print("LED on!\n");
    }
  }
  delay(100);
}
