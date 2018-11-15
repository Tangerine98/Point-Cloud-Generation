
#include<Servo.h>

Servo servo_base;
Servo servo_1;

#define TURN_TIME 185     //Variation from calculated value : Trial and error of time_delay
//turn_time = (0.23 - 0.19) *(5-4.8)/(4.8 - 6.0) + 0.23 = 0.22333sec 0.23 is speed at 4.8V and 0.19 is speed at 6.0V

int time_delay;
int angle = 5;
int finalAngle =5;
int servo1_angle=10;

// defines pins numbers
const int trigPin = 5;
const int echoPin = 6;

// defines variables
long duration;
float distance;

void setup() {
  
  servo_base.attach(9);
  servo_1.attach(10);
  
  servo_1.write(0);
  
  pinMode(trigPin, OUTPUT); // Sets the trigPin as an Output
  pinMode(echoPin, INPUT); // Sets the echoPin as an Input
  Serial.begin(9600);
  
  time_delay = (TURN_TIME *(angle*0.01746031746));  // 0.017.. is 22/(7*180) converting phi to rad and multiplying with turn time
}

void loop() {
  
      //Move Clockwise
      while (finalAngle <= 35) {    //this makes it to rotate 360
        servo_base.writeMicroseconds(1000);
        delay(200);
        Serial.println("Before Stop");
        //servo_base.writeMicroseconds(1500);
        servo_base.write(90);
        delay(500);
        Serial.println("After Stop");
        for(servo1_angle = 0; servo1_angle <= 170; servo1_angle = servo1_angle+10){
          servo_1.write(servo1_angle);
        }
        delay(2000);
        for(servo1_angle = 170; servo1_angle >= 0; servo1_angle = servo1_angle-10){
          servo_1.write(servo1_angle);
        }
        delay(1000);
        //delay(time_delay-75);  //8
       
        //findDistance();
        finalAngle = finalAngle + 5;
        Serial.println(finalAngle);
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

    Serial.print("\nDuration: ");
    Serial.println(duration);
    
    // Calculating the distance
    //Speed of sound = 340 m/s = 0.034cm/microsecond
    //Distance = (Speed * Time)/2
    distance= duration*0.034/2;
    
    // Prints the distance on the Serial Monitor
    Serial.print("Distance: ");
    Serial.println(distance);
}
