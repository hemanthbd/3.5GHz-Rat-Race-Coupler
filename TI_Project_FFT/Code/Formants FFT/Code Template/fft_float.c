/*
    fft_float.c - Floating-point complex radix-2 decimation-in-time FFT
    Perform in place FFT the output overwrite the input array
*/

//#include "fcomplex.h"       /* floating-point complex.h header file */

void fft(complex *X, unsigned int EXP, complex *W, unsigned int SCALE)
{
    complex temp;           /* temporary storage of complex variable */
    complex U;              /* Twiddle factor W^k */
    unsigned int i,j;
    unsigned int id;        /* Index for lower point in butterfly */
    unsigned int N=1<<EXP;  /* Number of points for FFT */
    unsigned int L;         /* FFT stage */
    unsigned int LE;        /* Number of points in sub DFT at stage L
                               and offset to next DFT in stage */
    unsigned int LE1;       /* Number of butterflies in one DFT at
                               stage L.  Also is offset to lower point
                               in butterfly at stage L */
    //unsigned int NUM_GROUPS;
    
    float scale;
    
    scale = 0.5;     
    if (SCALE == 0)         
        scale = 1.0;
    
    for (L=1; L<=EXP; L++) 	/* FFT butterfly */
    {
        LE=1<<L;        	/* LE=2^L=points of sub DFT */
        LE1=LE>>1;      	/* Number of butterflies in sub-DFT */
        U.re = 1.0;
        U.im = 0.;
        //NUM_GROUPS = 1<<(EXP-L);
        

        for (j=0; j<LE1;j++)
        {
            for(i=j; i<N; i+=LE) /* Do the butterflies */
            {
                id=i+LE1;
                
               // Compute butterfly as defined in 3b - in place computation
               temp.re = X[id].re*U.re-X[id].im*U.im;
               temp.im = X[id].re*U.im+X[id].im*U.re;
               
               X[id].re = X[i].re-temp.re;
               X[id].im = X[i].im-temp.im;
               X[i].re += temp.re;
			   X[i].im += temp.im;
            }
            
            /* Recursive compute W^k as U*W^(k-1) */
            //update twiddle factor by calculating temp.re
            temp = U;
            U.im = U.re*W[L-1].im + U.im*W[L-1].re;
            U.re = temp.re*W[L-1].re - temp.im * W[L-1].im;
        }
    }
}
