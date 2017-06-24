#include <iostream>

using namespace std;

#define H_Length 4
#define X_Length 6

void DoubleCircular()
{
    cout<<"\n\n\nDouble Circular Buffer :\n";

    int h[]={1, 2, 3, 4};                //h[n]
    int x[]={1, 2, 3, 4, 5, 6};          //x[n]

    cout<<"\nh[n] is :\n";
    for (int a=0;a<H_Length;a++)
    {
        cout<<h[a]<<"\t";
    }
    cout<<endl;

    cout<<"\nx[n] is :\n";
    for (int a=0;a<X_Length;a++)
    {
        cout<<x[a]<<"\t";
    }
    cout<<endl;

    int y[X_Length+H_Length-1];                     //declaring y[n]
    int Buffer[2*H_Length]={0};          //declaring buffer

    int Index1=0;
    int Index2=H_Length;                //declaring index=length of h + 1
    int sum=0;
    int temp[H_Length];
    for(int i=0;i<X_Length+H_Length-1;i++)
    {
        if(Index2>=2*H_Length)
        {
            Index1=0;
            Index2=H_Length;
        }
        if(i<=X_Length)
        {
            Buffer[Index1]=x[i];
            Buffer[Index2]=x[i];
        }
        else
        {
            Buffer[Index1]=0;
            Buffer[Index2]=0;
        }

        temp[H_Length]={0};
        sum=0;

        for (int k=0;k<H_Length;k++)
        {
            temp[k]=h[k]*Buffer[Index2-k];
            sum=sum+temp[k];
        }
        y[i]=sum;
        Index1++;
        Index2++;
    }





    cout<<"\nResult of convolution is :\n";
    for (int b=0;b<X_Length+H_Length-1;b++)
    {
        cout<<y[b]<<"\t";
    }
}

int main()
{
   DoubleCircular();
   return 0;
}
