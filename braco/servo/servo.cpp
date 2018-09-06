#include <stdio.h>
#include <stdlib.h>
#include <Servo.h> 
 
Servo myservo[2];

char frase[1000];

int s1, s2;

void setup(){
  Serial.begin(9600);
  myservo[0].attach(9);
  myservo[1].attach(10);
}

void loop(){
  int i = 0;
  while(!Serial.available());
  while(Serial.available() > 0){
    frase[i] = (char) Serial.read();
    delay(2);
    i++;
  }
  frase[i] = '\0';
  sscanf(frase, "%d.%*s%d.%*s", &s1, &s2);
  s1 = map(s1, 0, 1023, -101, -44);
  s2 = map(s2, 0, 1023, 150, 180);
  myservo[0].write(s1);
  myservo[1].write(s2);
  Serial.println(s1);
}