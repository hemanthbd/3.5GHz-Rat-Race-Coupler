
clear all;
close all;
[Y,Fs,N] = wavread('a.wav');
x=Y(5001:5512);

x_fft=fft(x,512);
power_spec = abs(x_fft).^2;
auto_corr = ifft(power_spec,512);
auto_corr = real(auto_corr(1:256));

auto_corr(1)=0;


max_num=auto_corr(1);
for i=2:length(auto_corr)
if auto_corr(i)>max_num
max_num = auto_corr(i);
index_max=i;
end
end

plot(x)
xlabel('Samples')
ylabel('Amplitude')
title('256 Samples for the vowel ''a''')

figure
plot(auto_corr)
xlabel('Samples')
ylabel('Amplitude')
title('Autocorrelation Function')
disp('Estimated Pitch is')
index_max


% Generating .dat file for probe point

x_fixed = floor(x*(2^15-1));
header = [1651 2 0 1 0];  %header needed for CCS to recognize the file when probing
fid=fopen('a.dat','w');% open file for writing
fprintf(fid,'%d %d %d %d %d\n',header); % write formatted header to file
fprintf(fid,'%d\n',double(x_fixed));  % write values to file
fclose(fid); % close file