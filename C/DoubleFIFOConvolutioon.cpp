#include <iostream>

using namespace std;

#define H_Length 4
#define X_Length 6

void DoubleFIFO()
{
    int h[]={1, 2, 3, 4};                //h[n]
    int x[]={1, 2, 3, 4, 5, 6};          //x[n]

    cout<<"h[n] is :\n";
    for (int a=0;a<H_Length;a++)
    {
        cout<<h[a]<<"\t";
    }
    cout<<endl;

    cout<<"x[n] is :\n";
    for (int a=0;a<X_Length;a++)
    {
        cout<<x[a]<<"\t";
    }
    cout<<endl;

    int y[X_Length];                     //declaring y[n]
    int Buffer[2*H_Length]={0};          //declaring buffer

    int Index=H_Length;                //declaring index=length of h + 1
    int sum=0;
    int temp[H_Length];
    for(int i=0;i<X_Length+H_Length-1;i++,Index++)
    {
        if(Index>2*H_Length)
        {
            for (int j=0;j<H_Length;j++)
            {
                Buffer[j]=Buffer[j+H_Length];
            }
            Index=H_Length;
        }
        if(i<=X_Length)
        {
            Buffer[Index]=x[i];
        }
        else
        {
            Buffer[Index]=0;
        }

        temp[H_Length]={0};
        sum=0;

        for (int k=0;k<H_Length;k++)
        {
            temp[k]=h[k]*Buffer[Index-k+1];
            sum=sum+temp[k];
        }
        y[i]=sum;
    }





    cout<<"Result of convolution is :\n";
    for (int b=0;b<X_Length+H_Length-1;b++)
    {
        cout<<y[b]<<"\t";
    }
}






int main()
{
   DoubleFIFO();

   return 0;
}
