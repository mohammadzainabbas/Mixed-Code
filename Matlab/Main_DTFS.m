function Main_DTFS()
x=[1:10];
N=length(x);
ak=DTFS(x,N);
xn=IDTFS(ak,N);

subplot(3,1,1);
stem(x,x);
hold on
subplot(3,1,2);
stem(x,abs(ak));
hold on
subplot(3,1,3);
stem(x,xn);
hold on

end

function [ak]= DTFS(x,N)

for k=1:N
a=0;
    for n=1:N
    
        a=a+(1/N)*x(n).*exp(-1*i*k*(2*pi/N)*n);
        
    end
        ak(k)=a;
end

end

function [x]=IDTFS(ak,N)

for n=1:N
x1=0;
    for k=1:N
    
        x1=x1+ak(k)*exp(i*k*(2*pi/N)*n);
        
    end
        x(n)=x1;
end

end