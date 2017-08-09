#line 1 "Code.asm"
#line 1 "Code.asm"
                                                
  
 void delay( unsigned int );
 
 void main()
 {
         TRISD=0x00;
 
        
 
  while(1)
  {
            
             
 
       PORTD = 0B11000000; 
       delay(100);
 
             PORTD = 0B11111001; 
             delay(100);
 
             PORTD = 0B10100100; 
             delay(100);
 
             PORTD = 0B10110000; 
             delay(100);
 
             PORTD = 0B10011001; 
             delay(100);
 
             PORTD = 0B10010010; 
             delay(100);
 
             PORTD = 0B10000010; 
             delay(100);
 
             PORTD = 0B11111000; 
             delay(100);
 
             PORTD =0B10000000; 
             delay(100);
 
             PORTD =0B10010000; 
             delay(100);
  }
 }
 
 
 void delay( unsigned int time )
 {
     unsigned int i;
    unsigned int j;
   for( i=0; i<time; i++ )
   for( j=0; j<200; j++ )
                 {   }
 }