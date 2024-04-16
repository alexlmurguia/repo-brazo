#include <ESP8266WiFi.h>
#include <ModbusTCPSlave.h>
#include <Ticker.h>

byte ip[] = {192, 168, 0, 126};
byte gateway[] = {192, 168, 0, 1};
byte subnet[] = {255, 255, 255, 0};

int r0, r1, r2, r3, r4, r5, r6, r7, r8;
int r0a = 1000, r1a = 1000, r2a = 1000, r3a = 1000, r4a = 1000, r5a = 1000, r6a = 1000, r7a = 1000, r8a = 1000;

Ticker Sample;

ModbusTCPSlave Mb;

void setup()
{
  Serial.begin(115200);

  Mb.begin("IZZI-271F","F82DC011271F", ip, gateway, subnet);

  while(WiFi.status() != WL_CONNECTED)
  {
    delay(500);
  }

  Sample.attach_ms(100, Task);
}

void loop()
{
  Mb.Run();  
}

void Task()
{
  r0 = Mb.MBHoldingRegister[0];
  r1 = Mb.MBHoldingRegister[1];
  r2 = Mb.MBHoldingRegister[2];
  r3 = Mb.MBHoldingRegister[3];
  r4 = Mb.MBHoldingRegister[4];
  r5 = Mb.MBHoldingRegister[5];
  r6 = Mb.MBHoldingRegister[6];
  r7 = Mb.MBHoldingRegister[7];
  r8 = Mb.MBHoldingRegister[8];
  
  if(r0 != r0a || r1 != r1a || r2 != r2a || r3 != r3a || r4 != r4a || r5 != r5a || r6 != r6a || r7 != r7a || r8 != r8a)
  {
    Serial.print(r0);
    Serial.print(',');
    Serial.print(r1);
    Serial.print(',');
    Serial.print(r2);
    Serial.print(',');
    Serial.print(r3);
    Serial.print(',');
    Serial.print(r4);
    Serial.print(',');
    Serial.print(r5);
    Serial.print(',');
    Serial.print(r6);
    Serial.print(',');
    Serial.print(r7);
    Serial.print(',');
    Serial.print(r8);
    Serial.println(',');

    r0a = r0;
    r1a = r1;
    r2a = r2;
    r3a = r3;
    r4a = r4;
    r5a = r5;
    r6a = r6;
    r7a = r7;
    r8a = r8;
  }
}
