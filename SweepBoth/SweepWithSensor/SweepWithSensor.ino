
#include<Servo.h>

Servo servo_base;
Servo servo_1;

#define TURN_TIME 185     //Variation from calculated value : Trial and error of time_delay
//turn_time = (0.23 - 0.19) *(5-4.8)/(4.8 - 6.0) + 0.23 = 0.22333sec 0.23 is speed at 4.8V and 0.19 is speed at 6.0V


// defines pins numbers
const int trigPin = 5;
const int echoPin = 6;
const int base_pin = 9;
const int servo1_pin = 10;


// defines variables
long duration;
float distance;
String servo1_angle_str,servo_base_str;
int time_delay;
int angle = 5;
int finalAngle =5;
int servo1_angle=10;


void setup() {
  
  servo_base.attach(base_pin);
  servo_1.attach(servo1_pin);
  servo_1.write(0);
  pinMode(trigPin, OUTPUT); // Sets the trigPin as an Output
  pinMode(echoPin, INPUT); // Sets the echoPin as an Input
  Serial.begin(9600);
  time_delay = (TURN_TIME *(angle*0.01746031746));  // 0.017.. is 22/(7*180) converting phi to rad and multiplying with turn time
}

void loop() {
  
      while (finalAngle <= 35) {    //this makes it to rotate 360 found by trial and error
        servo_base.writeMicroseconds(1000);
        delay(200);
        //servo_base.writeMicroseconds(1500); //not working. But why??
        servo_base.write(90);
        delay(500);

        for(servo1_angle = 0; servo1_angle <= 180; servo1_angle = servo1_angle+10){
          servo_1.write(servo1_angle);
          delay(1000);
          servo1_angle_str = String(servo1_angle);
          servo_base_str = String(finalAngle);
          findDistance();
        }
        delay(2000);
    
        for(servo1_angle = 180; servo1_angle >= 0; servo1_angle = servo1_angle-10){
          servo_1.write(servo1_angle);
          delay(1000);
          servo1_angle_str = String(servo1_angle);
          servo_base_str = String(finalAngle);
         findDistance();
        }
        delay(1000);
        //delay(time_delay-75);  //8
       
        //findDistance();
        finalAngle = finalAngle + 5;
        delay(1000);
      }    
}


void findDistance(){
    // Clears the trigPin
    digitalWrite(trigPin, LOW);
    delayMicroseconds(2);

    // Sets the trigPin on HIGH state for 10 micro seconds
    digitalWrite(trigPin, HIGH);
    delayMicroseconds(10);
    digitalWrite(trigPin, LOW);
    
    // Reads the echoPin, returns the sound wave travel time in microseconds
    duration = pulseIn(echoPin, HIGH);
    
    // Calculating the distanceMM
    //Speed of sound = 340 m/s = 0.034cm/microsecond
    //Distance = (Speed * Time)/2
    distance= duration*0.034/2;
    
    String distance_string = String(distance);
    delay(500);
    Serial.println(distance_string + "," + servo_base_str + "," +servo1_angle_str);
    delay(1000);
}
