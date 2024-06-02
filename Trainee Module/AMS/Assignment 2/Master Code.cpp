#include<SPI.h>                        
#define push 3
#define LED 2          

int x;
int value;

void setup()
{
  Serial.begin(9600);
  pinMode(push,INPUT);
  pinMode(LED,OUTPUT);
  SPI.begin();                            
  SPI.setClockDivider(SPI_CLOCK_DIV8); 
  digitalWrite(SS,HIGH); 
}

void loop()
{
  bool mSend,mReceive;          

  //taking in value from the button in master board
  value = digitalRead(push); 

  if(value == HIGH)                
  {
    x = 1;
  }
  else
  {
    x = 0;
  }
  
  digitalWrite(SS, LOW);//SS is setiing low to select the slave               
  
  mSend = x; //MOSI                           
  mReceive=SPI.transfer(mSend); //MISO
  //Processing the recived data from the slave
  if(mReceive == 1)                 
  {
    digitalWrite(LED,HIGH);             
  }
  else
  {
   digitalWrite(LED,LOW);              
  }
  delay(1000);
}
