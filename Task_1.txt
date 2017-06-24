/*
 * main.c
 */
#include<stdio.h>
#include<dsk6713.h>
#include<dsk6713_aic23.h>
#include<math.h>

int i;

float x[1000]={0};
DSK6713_AIC23_Config config=
{
0x0017;
0x0017;
0x01f9;
0x01f9;
0x0015;
0x0000;
0x0000;
0x0043;
0x0001;
0x0001;
}
int main()
{
	DSK6713_AIC23_CodecHandle hCodec;
	Uint32 msg;
	DSK6713_init();
	hCodec=DSK6713_AIC23_openCodec(0,&config);
	DSK6713_AIC23_setFreq(hCodec,DSK6713_AIC23_FRE_8KHZ);
	while(1)
	{
		while(!DSK6713_AIC23_read(hCodec,&msg))
		
		DSK6713_waitusec(1000000); //delay for 1000ms
			
		while(!!DSK6713_AIC23_write(hCodec,y))
		
	}
	DSK2713_AIC23_closeCodec(hCodec);




	return 0;}
