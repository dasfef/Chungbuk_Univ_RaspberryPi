#define ECHO 3
#define TRIG 4

void setup() {
  Serial.begin(9600);
  pinMode(ECHO, INPUT);
  pinMode(TRIG, OUTPUT);
}

void loop(){
//  Serial.print("Distance : ");
  Serial.println(Dist_cm());
//  Serial.println("[cm]");
  delay(500);
}

unsigned int Dist_cm() {
  unsigned long timer = 0;
  unsigned int dist = 0;

  digitalWrite(TRIG, LOW);
  delayMicroseconds(2);
  digitalWrite(TRIG, HIGH);
  delayMicroseconds(10);
  digitalWrite(TRIG, LOW);
  timer = pulseIn(ECHO, HIGH, 24000);

  if(timer == 0) dist = 400;
  else dist = timer * 0.034 / 2;

  return dist;
}
