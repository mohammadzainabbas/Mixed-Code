#include<p18f4550.h>                                                // Include Header for PIC18f455          
  
 void delay( unsigned int );
 
 void main()
 {
         TRISD=0x00;
 
        // unsigned int DELAY = 500;
 
  while(1)
  {
            // PORTB = 0xFE; //Hex code for dot
             //delay(5000);
 
       PORTD = 0B11000000; //GFEDCBAHex code for 0
       delay(100);
 
             PORTD = 0B11111001; //Hex code for 1
             delay(100);
 
             PORTD = 0B10100100; //Hex code for 2
             delay(100);
 
             PORTD = 0B10110000; //Hex code for 3
             delay(100);
 
             PORTD = 0B10011001; //Hex code for 4
             delay(100);
 
             PORTD = 0B10010010; //Hex code for 5
             delay(100);
 
             PORTD = 0B10000010; //Hex code for 6
             delay(100);
 
             PORTD = 0B11111000; //Hex code for 7
             delay(100);
 
             PORTD =0B10000000; //Hex code for 8
             delay(100);
 
             PORTD =0B10010000; //Hex code for 9
             delay(100);
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