/*
int led = 13;
int num;

void setup(){
  Serial.begin(9600);
  pinMode(led, OUTPUT);
}

void loop(){
  if(Serial.available() > 0){
    num = int(Serial.read());
    Serial.println(num);
    if(num == 'l'){
      digitalWrite(led, HIGH);
    }
    else if (num == 'd'){
      digitalWrite(led, LOW);
    }
  }
}
*/
/*
int led = 13;

void setup(){
  Serial.begin(9600);
  pinMode(led, OUTPUT);
}

void loop(){
  if(Serial.available() > 0){
    Serial.println(Serial.read());
  }
}
*/
/*
char frase[1000];

void setup(){
  Serial.begin(9600);
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
  Serial.println(frase);
}
*/
void setup(){
  Serial.begin(9600);
}

void loop(){
  Serial.println("1, 2, 3, testando...");
  delay(100);
}
