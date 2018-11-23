#include <stdio.h>
#include <string.h>

int count = 0;

void setup() {
  // Serial TX (1) is connected to Photon RX
  // Serial RX (0) is connected to Photon TX
  // Ardiuno GND is connected to Photon GND
  Serial.begin(9600);

  while(!Serial) delay(100);

  // Initiate handshake
  Serial.write("ready\n");
}

char buffer[10];

void loop() {
  // Read data from serial
  while(Serial.available()) {
    char c = Serial.read();
    if (c != '\n') {
      // count the number of characters excluding the new line
      ++ count;
    } else {
      // end of stream print the characters count
      sprintf(buffer, "%d\n", count);
      Serial.write(buffer);
    }
  }
  delay(10);
}
