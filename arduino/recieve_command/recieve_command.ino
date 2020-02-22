/*

*/



#include <Servo.h>             //Servo library
 
Servo servo_test;        //initialize a servo object for the connected servo  
                
//int angle = 0;    
// 
//void loop() 
//{ 
//  for(angle = 0; angle < 180; angle += 1)    // command to move from 0 degrees to 180 degrees 
//  {                                  
//    servo_test.write(angle);                 //command to rotate the servo to the specified angle
//    delay(15);                       
//  } 
// 
//  delay(1000);
//  
//  for(angle = 180; angle>=1; angle-=5)     // command to move from 180 degrees to 0 degrees 
//  {                                
//    servo_test.write(angle);              //command to rotate the servo to the specified angle
//    delay(5);                       
//  } 
//
//    delay(1000);
//}


int angle = 0; 
 
void setup() {
  Serial.begin(9600);
  pinMode(LED_BUILTIN, OUTPUT);  
  Serial.print("Program ready!\n");
   servo_test.attach(9);      // attach the signal pin of servo to pin9 of arduino
}

void loop() {
  serialRead();
}

void serialRead()
{
  if(Serial.available() > 0)
  {
    char var = Serial.read();
    if(var == '|')
    {
      servo_test.write(angle);
      angle += 180;
      digitalWrite(LED_BUILTIN, HIGH);
      Serial.print("LED on!\n");
    }
    else if (var == 'P')
    {
      servo_test.write(angle);
      angle = angle - 180;
      digitalWrite(LED_BUILTIN, LOW);
      Serial.print("LED off!\n");
    }
  }
}
