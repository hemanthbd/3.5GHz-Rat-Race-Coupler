fs=8192;
fin = 256;
duration=1/60;
sec = 60*duration;
n=0:1/fs:sec;
y=sin(2*pi*fin*n);
y_int = floor(y * (2^15-1) + 0.5);
fid = fopen('sine_f.dat','w');

fprintf(fid,'int sin_i[128] = {\n');
fprintf(fid,'%d,\n',y_int(1:128));
fprintf(fid,'};');
fclose(fid);