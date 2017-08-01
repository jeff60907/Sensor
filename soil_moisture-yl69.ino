int sensor_pin = A0;
int output_value ;

void setup() {
   Serial.begin(9600);
}

void loop() {

   output_value= analogRead(sensor_pin);
   output_value =  1023 - output_value;
   //Serial.print("Mositure:");
   Serial.print(output_value);
   output_value = map(output_value,0,800,0,100);
   Serial.print(",");
   Serial.print(output_value);
   //Serial.print("%");

   delay(500);

}
