#include<reg51.h>
void displaywrite(unsigned char);
void delay_ms(unsigned int); 

void main (void)
{
unsigned char i;               

while (1)                      
  {
  for (i=0; i<256; i++)        
    {
    displaywrite(i);        
    delay_ms (250);            
    }
  }
}

void delay_ms(unsigned int ms)
    {    unsigned int i,j;
          for(i=0;i<ms;i++)
          for(j=0;j<=1275;j++);
       }
void displaywrite(unsigned char x) 
{	
P2 = x;  // Display to Port 2
}