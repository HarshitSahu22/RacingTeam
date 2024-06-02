#include<SPI.h>
#define inputbutton 3
#define outputLED 2

volatile bool received;
volatile bool Slavereceived,Slavesend;
int buttonvalue;
int x;


void setup()
{
Serial.begin(9600);
  
  pinMode(inputbutton,INPUT); 
  pinMode(outputLED,OUTPUT);               
  pinMode(MISO,OUTPUT);                  

  SPCR |= _BV(SPE);                  
  received = false;

  SPI.attachInterrupt();
}

ISR (SPI_STC_vect)                        
{
  Slavereceived = SPDR;         
  received = true;                        
}

void loop()
{  
 if(received)                           
   {
      if (Slavereceived==1) 
      {
        digitalWrite(outputLED,HIGH);       
      }else
      {
        digitalWrite(outputLED,LOW);          
      }
      
      buttonvalue = digitalRead(inputbutton);  
      
      if (buttonvalue == HIGH)           
      {
        x=1;
        
      }else
      {
        x=0;
      }
      
  Slavesend=x;                             
  SPDR = Slavesend;                       
  delay(1000);
}
}
