#include <LiquidCrystal.h>

char dataReceived;
LiquidCrystal lcd(7,8,9,10,11,12);
int  c = 0;

void setup() {
   Serial.begin(9600);
   lcd.begin(16,2);
   lcd.setCursor(0,0);
   
}


void loop() {
  
  while (Serial.available() > 0) {
      c++;
      dataReceived = Serial.read();
      lcd.print(dataReceived);
      lcd.setCursor(c,0);
      if (c == 16)
        lcd.setCursor(0,1);   
       
  }
  
   
}
