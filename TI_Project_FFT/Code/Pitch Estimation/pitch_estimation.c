/*************************Program to estimate the Pitch in the Input wave in Assembly through IFFT of the FFT obtained Power Spectrum***********************************/

#include <stdio.h>
#include <math.h>
#include <tms320.h>
#include <dsplib.h> // Implementing the FFT
#include <intrindefs.h> 
#define NX 512 // FFT Length
#pragma DATA_SECTION (ac,".input")

//prototype for assembly function
extern int max_idx(DATA *, unsigned int);

DATA x[2*NX]; // input vector to be imported initially using probe point 
DATA y[2*NX];      
DATA ac[NX/2]; //auto correlation vector

unsigned char input_array[NX]; // Vector which is loaded through probe point with the input wave

int power_spectrum[NX]; // vector to hold Power Spectrum
int max_num; 
int index_max;
int pitch;

void main()
{
	int i,j;
     j=0; // Dummy variable where the probe point is placed to load a.dat into input_array
 
  	 for (i=0;i<NX;i++) // Input array which has the a.dat wave 
    {
        x[2*i] = input_array[i];
        x[2*i+1] = 0;
    }
     
      cfft(x,NX,SCALE); // DIF-FFT of the input vector
      cbrev(x, x, NX); //  Bit-reversal
	    
    for (i=0;i<NX;i++)
    {
        power_spectrum[i] =(((long)x[2*i])*((long)x[2*i]) + ((long)x[2*i+1])*((long)x[2*i+1]))>>10; // The power spectrum of the FFT signal
    }
         
	
	 for (i=0;i<NX;i++) // Take only the real-part of the power spectrum and store in y
    {
        y[2*i] = power_spectrum[i];
        y[2*i+1] = 0;
    }
     
   
   cifft(y, NX, SCALE); // DIF-IFFT of the real part of the power spectrum stored in y
   cbrev(y,y,NX); // Bit reversal
   
   	  for (i=0;i<NX/2;i++) //The Autocorrelation function, which takes in only THAT part of y which is real and ignores the 0s
    {
        ac[i] = y[2*i];
    }
    
   ac[0]=0; // DC set to zero
   
   pitch =  max_idx(ac, NX/2); // This function is used to obtain the Maximum peak of the autocrrelation function, and hence the Pitch is estimated  
  
  
}





