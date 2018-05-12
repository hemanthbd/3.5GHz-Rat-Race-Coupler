/*
    test_fft.c - Example to test floating-point Complex FFT
*/

#include <math.h>   
//#include "fcomplex.h"   /* floating-point complex.h header file */
#include "sine_f.dat"  /* Experiment floating-point data */
#include "fbit_rev.c" // Importing the bit-rev file
#include "fft_float.c" // Importing the FFT_float file
#include <stdio.h>

#define N 256           /* Number of FFT points */
#define EXP 8           /* EXP=log2(N) */
#define pi 3.1415926535897     

complex X[N];           /* Declare input array  */
complex W[EXP];         /* Twiddle e^(-j2pi/N) table */    
complex temp;
float spectrum[N];
float re1[N],im1[N];                                   

void main()
{
    unsigned int i,j,L,LE,LE1;
	char  wavHd[44];
	FILE  *inFile;
	short inData[4];
    
    for (L=1; L<=EXP; L++) /* Create twiddle factor table */
    {
        LE=1<<L;         /* LE=2^L=points of sub DFT */
        LE1=LE>>1;       /* Number of butterflies in sub DFT */
        W[L-1].re = cos(pi/LE1);
        W[L-1].im = -sin(pi/LE1);
    }

	inFile = fopen("a.wav", "rb"); // Taking the input .wav file
	if (inFile == NULL)
	{
		exit(0);
	}
	            
	// Skip input wav file header                
	fread(wavHd, sizeof(char), 44, inFile);
    
    j=0;          
    while( (fread(inData, sizeof(char), 4, inFile) == 4) )
    {
		X[j].re = inData[3];
		X[j].im = 0;
		j++;
		if (j>N){
        
	        /* DIT-FFT */
	     
	        bit_rev(X,EXP); // First bit reversal
	        fft(X,EXP,W,1); // Then calulate the FFT
	        
            
	        /* Verify FFT result */
	        for (i=0; i<N; i++)  
	        {
	            /* Compute spectrum */
	            temp.re = X[i].re*X[i].re;
	            temp.im = X[i].im*X[i].im;        
	            spectrum[i] = (temp.re+temp.im);
	        }

			// helpful to set DC to zero to see formants
			spectrum[0] = 0;

			j=0; // put breakpoint here
		}        	
    }
}

