x= sin (t);
T=2*pi;
ak=fourier(x,T);
xt=Inversefourier(ak,T);

subplot(3,1,1)
ezplot(x)
hold on
subplot(3,1,2)
stem(abs(ak))
hold on
subplot(3,1,3)
ezplot(xt)
hold on
end
function ak=fourier(x,T)
syms t

for k=-10:10
    ak(k+11)=(1/T)*int(x*exp(-1i*k*((2*pi)/T)*t),t,0,T);
end
end

function xt=Inversefourier(ak,T)
syms t
xt=0;
for k=-10:10
    xt=xt+ak(k+11).*exp(1i*k*((2*pi)/T)*t);
end
end