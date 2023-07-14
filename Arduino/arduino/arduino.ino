#include <LCD.h>
#include <Wire.h>
#include <LiquidCrystal_I2C.h>
#include <SPI.h>
#include <MFRC522.h>


#define RST_PIN         9          // Configurable, see typical pin layout above
#define SS_PIN          10         // Configurable, see typical pin layout above

MFRC522 mfrc522(SS_PIN, RST_PIN);  // Create MFRC522 instance
LiquidCrystal_I2C lcd(0x27,2,1,0,4,5,6,7);

String code;


String getUid(byte *buffer, byte bufferSize) {
  String uid = "";
  for (byte i = 0; i < bufferSize; i++) {
    uid += buffer[i];
  }
  return uid;
}

void comparar(String uid){
  if (uid == "24524331161"){
    Serial.print("moon");
  }
  if (uid == "5123617912"){
    Serial.print("saturno");
  }
}
void setup() {
	Serial.begin(9600);		// Initialize serial communications with the PC
  lcd.setBacklightPin(3, POSITIVE);
  lcd.setBacklight(HIGH);
  lcd.begin(16,2);
  lcd.setCursor(0,0);
  lcd.print("WAITING...");
	while (true){
    if(Serial.available()){
      char letra = Serial.read();
      Serial.println(letra);
      if(letra == 'k'){
        Serial.println("OK");
        break;
      }
    }
  }		// Do nothing if no serial port is opened (added for Arduinos based on ATMEGA32U4)
	SPI.begin();			// Init SPI bus
	mfrc522.PCD_Init();		// Init MFRC522
	delay(4);				// Optional delay. Some board do need more time after init to be ready, see Readme
	mfrc522.PCD_DumpVersionToSerial();	// Show details of PCD - MFRC522 Card Reader details
	Serial.println(F("Scan PICC to see UID, SAK, type, and data blocks..."));
  // lcd.setBacklightPin(3, POSITIVE);
  // lcd.setBacklight(HIGH);
  // lcd.begin(16,2);
  // lcd.setCursor(0,0);
  // lcd.print("HOLA A TODOS!");
  lcd.setCursor(0, 0);
  lcd.print("CONECTED!");
}

void loop() {
	if (mfrc522.PICC_IsNewCardPresent()) {
    if (mfrc522.PICC_ReadCardSerial()) {
       // mfrc522.PICC_DumpToSerial(&(mfrc522.uid));
      code = getUid(mfrc522.uid.uidByte, mfrc522.uid.size);
       lcd.clear();
       comparar(code);
        mfrc522.PICC_HaltA();
    }
  }
  if(Serial.available()){
    char letra = Serial.read();
    if(letra == 'd'){
      lcd.setCursor(0, 0);
      lcd.print("DISCONECTED...");
    }
  }
}
