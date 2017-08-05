
/*  //ADC
// #include <stdio.h>
//#include <stdlib.h>

#include<p18f4550.h>
#include <delays.h>
#define RS PORTCbits.RC0
#define RW PORTCbits.RC1
#define EN PORTCbits.RC2
#define LCD_PORT PORTB
	 void T0Delay(unsigned int); 
void SD1(unsigned num2);
void LCD_Initialize(void);
void LCD_Command(unsigned char command);
void LCD_Write(unsigned char data);
void main(void)
{
	    unsigned int D0=0;
    unsigned int D1=0;
    unsigned int D2=0;
    unsigned int D3=0;
	unsigned int byteH,byteL,count ;
    unsigned int big; 
	TRISB=0;
	TRISC=0;
	TRISAbits.TRISA0=1;
		TRISAbits.TRISA2=1;
	  EN=0;
    LCD_Initialize();
		ADCON0=0x01;
		ADCON1=0x1D;
                ADCON2=0xAE;
		while(1)
		{
			T0Delay(200);
			ADCON0bits.GO=1;
			while(ADCON0bits.DONE==1);
			byteL=ADRESL;
            byteH=ADRESH;
            byteH<<=8;
            big=byteH|byteL;
			count=big*(0.25);
			    D0 = count%10;
  
    D1 = (count/10)%10;
   
    D2 = (count/100) %10;
 
    D3 =  (count/1000)%10;
 
    LCD_Command(0x02);
    SD1(D3);
 
    LCD_Command(0x06);
    SD1(D2);
 
    LCD_Command(0x06);
    SD1(D1);
 
    LCD_Command(0x06);
    SD1(D0);
 
    LCD_Command(0x06);
      LCD_Write(' ');
 
    LCD_Write('c');
 
    LCD_Write('e');
  
    LCD_Write('n');
  
    LCD_Write('t');
 
    LCD_Write('i');
 
    LCD_Write('g');
 			
    LCD_Write('r');
    LCD_Write('a');
 
    LCD_Write('d');
 			
    LCD_Write('e');
 	
    T0Delay(200);
    }
    }	
    void LCD_Command(unsigned char command)
{
    RS=0;
    RW=0;
    LCD_PORT=command;
    EN=1;
    Delay1KTCYx(50  );
    EN=0;
    Delay1KTCYx(50  );
}
void LCD_Write(unsigned char data)
{
    RS=1;
    RW=0;
    LCD_PORT=data;
    EN=1;
    Delay1KTCYx(50  );
    EN=0;
}
void LCD_Initialize(void)
{
    Delay1KTCYx(500);
    LCD_Command(0x01);
    Delay1KTCYx(10);
    LCD_Command(0x80);
    Delay1KTCYx(10);
    LCD_Command(0x0F);
    Delay1KTCYx(10);
}
 
void SD1(unsigned num2)
{
    switch(num2)
   {
      case 0:
              LCD_Write('0');
         break;
      case 1:
             LCD_Write('1');
         break;
      case 2: LCD_Write('2');
         break;
      case 3:
          LCD_Write('3');
         break;
      case 4:
             LCD_Write('4');
         break;
      case 5:
             LCD_Write('5');
         break;
      case 6:
                LCD_Write('6');
         break;
      case 7:
          LCD_Write('7');
         break;
      case 8:
          LCD_Write('8');
         break;
      case 9:
               LCD_Write('9');
         break;
}
}
 
 
   void T0Delay(unsigned int time)
    {

       unsigned char i;
       unsigned char j;
       for(i=0;i<=200;i++)
         for(j=0;j<=time;j++);


	}	

*/

