function Main()
syms t
x=sin (t);

T=2*pi;

ak=CTFS(x,T);

xt=ICTFS(ak,T);

subplot(3,1,1);
ezplot(x)
hold on
subplot(3,1,2);
stem(-10,10,abs(ak))
hold on
subplot(3,1,3)
ezplot(xt)
hold on
end

function ak=CTFS(x,T)
syms t
for k=-10:1:10
    
   ak(k+11)=1/T*int(x*exp(-1i*k*((2*pi)/T)*t),t,0,T);
end
end

function xt=ICTFS(ak,T)
syms t
xt=0;
for k=-10:1:10
   xt=xt+ak(k+11).*exp(1i*k*((2*pi)/T)*t);
end
end