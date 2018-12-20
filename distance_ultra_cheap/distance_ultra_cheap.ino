
#define trigPin1 3
#define echoPin1 2
#define trigPin2 4
#define echoPin2 5
#define trigPin3 7
#define echoPin3 12
 
long duration, distance, RightSensor,MiddleSensor,LeftSensor;
 
void setup()
{
Serial.begin (9600);
pinMode(trigPin1, OUTPUT);
pinMode(echoPin1, INPUT);
pinMode(trigPin2, OUTPUT);
pinMode(echoPin2, INPUT);
pinMode(trigPin3, OUTPUT);
pinMode(echoPin3, INPUT);
}
 
void loop() {
SonarSensor(trigPin1, echoPin1);
LeftSensor = distance;
SonarSensor(trigPin2, echoPin2);
MiddleSensor = distance;
SonarSensor(trigPin3, echoPin3);
RightSensor = distance;

Serial.print(" - ");
Serial.print("left:");
Serial.print(LeftSensor);
Serial.print(" - ");
Serial.print("middle: ");
Serial.print(MiddleSensor);
Serial.print(" - ");
Serial.print("right: ");
Serial.println(RightSensor);
Serial.print(" - ");

delay(100);
}
 
void SonarSensor(int trigPin,int echoPin)
{
digitalWrite(trigPin, LOW);
delayMicroseconds(2);
digitalWrite(trigPin, HIGH);
delayMicroseconds(10);
digitalWrite(trigPin, LOW);
duration = pulseIn(echoPin, HIGH);
distance = (duration/2) / 29.1;
 
}
