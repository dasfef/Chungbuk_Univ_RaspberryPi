int Count = 0;

void setup() {
  Serial.begin(9600);
}

void loop() {
  if(++Count > 9) Count = 0;
  Serial.println(Count);
  delay(1000);
}
