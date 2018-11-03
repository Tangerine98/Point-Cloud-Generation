#include<Servo.h>

Servo servo_base;
Servo servo_1;

#define TURN_TIME 223     //170
//turn_time = (0.23 - 0.19) *(5-4.8)/(4.8 - 6.0) + 0.23 = 0.22333sec 0.23 is speed at 4.8V and 0.19 is speed at 6.0V

int time_delay,angle[2];
int i=0;

void setup() {
  Serial.begin(9600);
  servo_base.attach(9);
  servo_1.attach(10);
  servo_1.write(0);
}



void loop() {
  while (Serial.available() >=2) {
    for(int i = 0; i <2;i++){
      angle[i]=Serial.read();
    }
  }
  Serial.print(servo_1.read());
  Serial.print(angle[0]);
  Serial.print("\n");
  Serial.print(angle[1]);
  Serial.print("\n");
  if(angle[0] != 0){
    if(i ==0 ){
      time_delay = (TURN_TIME *(angle[0]*0.01746031746));  // 0.017.. is 22/(7*180) converting phi to rad and multiplying with turn time
      Serial.print(time_delay);
      servo_base.writeMicroseconds(0);
      delay(time_delay);
      servo_base.writeMicroseconds(1500);
      Serial.print("Base servo in position\n");
      i = 1;
    }
  }
  servo_1.write(angle[1]);
  Serial.print("Servo 1 in position\n");
}
