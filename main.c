#include<p18f4550.h>           
//#pragma config FOSC = INTOSCIO_EC
//#pragma config FCMEN = OFF    // OR this way
//#pragma config BORV = 3
//#pragma config WDT = OFF
//#pragma config CPB = OFF
//#pragma config CPD = OFF
void delay( unsigned int time );
void main()
{
    
         TRISB=0x00;
 		 TRISD=0x00;
        // unsigned int DELAY = 500
     //     PORTB = 0B00000011; 

while(1)
  {
            // PORTB = 0xFE; //Hex code for dot
             //delay(5000);
 
       		 PORTB = 0B00000011; //ABCDEFGV Hex code for 0
				PORTD = 0B00000011;
       		 delay(100);
 
             PORTB = 0B10011111; //Hex code for 1
PORTD = 0B10011111; //Hex code for 1
             delay(100);
 
             PORTB = 0B00100101; //Hex code for 2
PORTD = 0B00100101; //Hex code for 2
             delay(100);
 
             PORTB = 0B00001101; //Hex code for 3
PORTD = 0B00001101; //Hex code for 3
             delay(100);
 
             PORTB = 0B10011001; //Hex code for 4
PORTD = 0B10011001; //Hex code for 4
             delay(100);
 
             PORTB = 0B01001001; //Hex code for 5
PORTD = 0B01001001; //Hex code for 5
             delay(100);
 
             PORTB = 0B01000001; //Hex code for 6
PORTD = 0B01000001; //Hex code for 6
             delay(100);
 
             PORTB = 0B00011111; //Hex code for 7
PORTD = 0B00011111; //Hex code for 7
             delay(100);
 
             PORTB = 0B00000001; //Hex code for 8
PORTD = 0B00000001; //Hex code for 8
             delay(100);
 
             PORTB = 0B00001001; //Hex code for 9
PORTD = 0B00001001; //Hex code for 9
             delay(100);
  
            // PORTB = 0xFE; //Hex code for dot
             //delay(5000);
 
  }
 }
 
 //DELAY FUNCTION ( mS )
 void delay( unsigned int time )
 {
     unsigned int i;
    unsigned int j;
   for( i=0; i<time; i++ )
   for( j=0; j<200; j++ )
                 { /* Well its Just a Timer */ }
 }