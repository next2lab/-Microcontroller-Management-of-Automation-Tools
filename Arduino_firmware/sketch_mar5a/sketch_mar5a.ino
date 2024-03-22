#include <LiquidCrystal_I2C.h>
#include <Arduino.h>
#include <TM1637Display.h>
#include <MatrizLed.h>
#include <GyverEncoder.h>

#define REL 3
#define DISP_CLK 4
#define DISP_DIO 5
#define MOSFET 9
#define ENC_CLK 17
#define ENC_DT 16
#define ENC_SW 15
#define SOIL_DET A0
#define RAIN_DET A7
#define MATRIX_DIN 12
#define MATRIX_CLK 11
#define MATRIX_CS 10

LiquidCrystal_I2C lcd(0x27, 16, 2); // I2C1602 Liquid Crystal Display
TM1637Display tm_display(DISP_CLK, DISP_DIO); // 4-Digit 7-Segment Display
MatrizLed matrix; // 8x8 LED matrix (MAX7219)
Encoder enc(ENC_CLK, ENC_DT, ENC_SW); // Encoder

void setup() {
  Serial.begin(9600); // establish connection
  lcd.init();
  lcd.backlight();
  pinMode(REL, OUTPUT);
  tm_display.setBrightness(0x0f);
  matrix.begin(MATRIX_DIN, MATRIX_CLK, MATRIX_CS, 1); // DIN, CLK, CS, number of 8x8 matrices
  matrix.rotate(false);
  matrix.setIntensity(3); // brightness (0 - 15)
  digitalWrite(REL, 1);
}

void loop() {
  read_port(); // reading from port
  write_port(); // writing to port

  // encoder
  enc.tick();
  if (enc.isTurn()) {
    if (enc.isRight()) Serial.print("1:2,");
    if (enc.isLeft()) Serial.print("1:-2,");
    if (enc.isRightH()) Serial.print("1:10,");
    if (enc.isLeftH()) Serial.print("1:-10,");
  }
  if (enc.isClick()) Serial.print("1:99,");
  if (enc.isHolded()) Serial.print("1:00,");
}

void read_port() {
  if (Serial.available() > 0) { // checking for available data
    char incomingByte[30]; // setting buffer size
    int amountByte = Serial.readBytesUntil(',', incomingByte, 30); // ":" - terminator, recording data in incomingByte, amountByte - number of bytes
    incomingByte[amountByte] = NULL; // write null in the amountByte area
    char* str_data = strchr(incomingByte, ':'); // string starting from the delimiter ":"
    char key[5] = "";
    strncpy(key, incomingByte, str_data-incomingByte); // extracting key
    int int_data = atoi(++str_data); // extracting value
    int int_key = atoi(key); // convert key to int data type

    // distributing cases relative to devices
    switch (int_key) {
      case 1: // first line of the I2C1602 display
        lcd.setCursor(0, 0);
        lcd.print("                ");
        lcd.setCursor(1, 0);
        lcd.print(str_data); break;
      case 2: // second line of the I2C1602 display
        lcd.setCursor(0, 1);
        lcd.print("                ");
        lcd.setCursor(1, 1);
        lcd.print(str_data); break;
      case 3: // TM1637 display
        tm_display.clear();
        tm_display.showNumberDec(int_data, false); break;
      case 4: // 8x8 MAX7219 matrix
        matrix.writePhrase(str_data); break;
        matrix.turnOn(); break;
      case 5: // relay
        digitalWrite(REL, int_data); break;
      case 6: // MOSFET module
        analogWrite(MOSFET, int_data); break;
    };
  }
}

void write_port() {
  // sending low-frequency data
  static uint32_t tmr = 0;
  if (millis() - tmr > 200) {
    tmr = millis();
    Serial.print(2);
    Serial.print(':');
    Serial.print(analogRead(SOIL_DET));
    Serial.print(',');
  }

  // fast data sending
  static uint32_t tmr2 = 0;
  if (millis() - tmr2 > 100) {
    tmr2 = millis();
    Serial.print(3);
    Serial.print(':');
    Serial.print(analogRead(RAIN_DET));
    Serial.print(',');
  }
}