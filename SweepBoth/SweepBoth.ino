#include<Servo.h>

Servo servo_base;
Servo servo_link;

#define TURN_TIME 185     //Variation from calculated value : Trial and error of time_delay
//turn_time = (0.23 - 0.19) *(5-4.8)/(4.8 - 6.0) + 0.23 = 0.22333sec 0.23 is speed at 4.8V and 0.19 is speed at 6.0V

int time_delay;
int angle = 5;
int finalAngle =5;
int pos = 0;    // variable to store the servo position

// defines pins numbers
const int trigPin = 5;
const int echoPin = 6;

// defines variables
long duration;
float distance;

void setup() {
  servo_base.attach(9);
  //servo_base.write(0);
  servo_link.attach(11);
  servo_link.write(0);
  pinMode(trigPin, OUTPUT); // Sets the trigPin as an Output
  pinMode(echoPin, INPUT); // Sets the echoPin as an Input
  Serial.begin(9600); // Starts the serial communication
  time_delay = (TURN_TIME *(angle*0.01746031746));  // 0.017.. is 22/(7*180) converting phi to rad and multiplying with turn time
}

void loop() {
  //Move Clockwise
  while (finalAngle <= 360) {    //this makes it to rotate 360
    servo_base.writeMicroseconds(1000);
    delay(200);
    servo_base.writeMicroseconds(1500);
    delay(500);
    for (pos = 0; pos <= 180; pos += 10) { // goes from 0 degrees to 180 degrees
      // in steps of 1 degree
      servo_link.write(pos); 
      //findDistance();             // tell servo to go to position in variable 'pos'
      Serial.println(pos);
      delay(150);                       // waits 15ms for the servo to reach the position
    }
    
    for (pos = 180; pos >= 0; pos -= 10) 
    { // goes from 180 degrees to 0 degrees
      servo_link.write(pos);
      //findDistance();              // tell servo to go to position in variable 'pos'
      Serial.println(pos);
      delay(150);                       // waits 15ms for the servo to reach the position
    }
        
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
