function Convolution()
disp('Enter your first signal range');
start_point_1 = input ('Starting point: ');
end_point_1 = input('Ending point: ');
signal_range_1 = end_point_1-start_point_1;
disp('Enter its values: ');
for i=1:signal_range_1+1    
    signal_1(i) = input('Enter its value: ');
end


disp('Enter your second signal range');
start_point_2 = input ('Starting point: ');
end_point_2 = input('Ending point: ');
signal_range_2 = end_point_2-start_point_2;
disp('Enter its values: ');
for i=1:signal_range_2+1    
    signal_2(i) = input('Enter its value: ');
end

signal_1 = [zeros(1,signal_range_2) signal_1 zeros(1,signal_range_2)];
signal_2 = flip(signal_2);
signal_2 = [zeros(1,signal_range_1+signal_range_2) signal_2 zeros(1,signal_range_1+signal_range_2)];
disp(signal_2);
end