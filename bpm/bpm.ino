#include "ThingSpeak.h"
#include <ESP8266WiFi.h>
float value = 0;
int x = 0;
boolean countStatus;
int beat, bpm=0;
unsigned long millisBefore;
int lastbpm=0;
unsigned long rr_millisBefore;
int rr=0;
int st=0,i=0,st_store=0,j=0;

//----------- Enter you Wi-Fi Details---------//
char ssid[] = "MMGHEEWALE HOME";    //your network SSID (name)
char pass[] = "389cs15027";         //your network password
//-------------------------------------------//

//----------- Channel Details -------------//
unsigned long Channel_ID = 1370563; // Channel ID
const char * WriteAPIKey = "IF6HL0AQ644Y6MGK"; // Your write API Key
// ----------------------------------------//

WiFiClient  client;

void setup()
{
  Serial.begin(115200);
  internet();
  ThingSpeak.begin(client);
  rr_millisBefore = millis();
}
                                          // the loop routine runs over and over again forever:
void loop()
{                                  
  int sensorValue = analogRead(A0);       // read the input on analog pin 0:
  i++;
  st_store= st_store+sensorValue;
  if (countStatus == 0)
  {
    if (sensorValue > 600)
    {
      j++;
      st=st_store/i;
      i=0;
      st_store=0;
      if(j>1){  rr = millis() - rr_millisBefore;}
      Serial.print("rrtime:\t");
      Serial.println(rr);
      Serial.print("st:\t");
      Serial.println(st);
      rr_millisBefore = millis();
 
      countStatus = 1;
      beat++;
    }
  }
  else
  {
    if (sensorValue < 500)
    {
      countStatus = 0;
    }
  }
  if (millis() - millisBefore > 15000)
  {
    bpm = beat * 4;
    upload(bpm,rr,st);
    beat = 0;
    Serial.print("calculated BPM : ");
    Serial.println(bpm);
    millisBefore = millis();
    rr_millisBefore = millis();
    j=0;
  }
  delay(1);                           // delay in between reads for stability
}


void upload(int bpm,int rr, int st)
{
  ThingSpeak.setField(1, bpm);
  ThingSpeak.setField(2, rr);
  ThingSpeak.setField(3, st);
  
  if(bpm<150){
  internet();
  x = ThingSpeak.writeFields(Channel_ID, WriteAPIKey);
  lastbpm=bpm;
  if (x == 200){Serial.println("Data Updated.");}
  else if (x != 200)
  {
    Serial.println("Data upload failed, retrying....");
    delay(7000);
    upload(bpm,rr,st);
  }}
  else{upload(lastbpm,rr,st);}
}

void internet()
{
  if (WiFi.status() != WL_CONNECTED)
  {
    WiFi.mode(WIFI_STA);
    WiFi.begin(ssid, pass);
    Serial.print("Attempting to connect to SSID: ");
    Serial.println(ssid);
    while (WiFi.status() != WL_CONNECTED)
    {
      Serial.print(".");
      delay(1000);
    }
    Serial.println("\nConnected.");
  }
}
