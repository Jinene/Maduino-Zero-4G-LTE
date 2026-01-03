#include <MaduinoZeroLTE.h>  // hypothetical library
#include <TinyGPS++.h>
#include "config.h"

TinyGPSPlus gps;
MaduinoZeroLTE lte;

void setup() {
  Serial.begin(115200);
  Serial1.begin(GPS_BAUD, SERIAL_8N1, GPS_RX_PIN, GPS_TX_PIN);

  Serial.println("Initializing LTE...");
  lte.begin(APN, LTE_USER, LTE_PASS);
  Serial.println("LTE connected!");
}

void loop() {
  while (Serial1.available() > 0) {
    gps.encode(Serial1.read());
  }

  if (gps.location.isUpdated()) {
    float lat = gps.location.lat();
    float lng = gps.location.lng();
    Serial.print("Lat: "); Serial.print(lat);
    Serial.print(", Lng: "); Serial.println(lng);

    // send to server
    String url = String(SERVER_URL) + "?lat=" + String(lat,6) + "&lng=" + String(lng,6);
    int status = lte.httpGet(url);
    Serial.print("Sent data. Status: "); Serial.println(status);
  }

  delay(INTERVAL);
}
