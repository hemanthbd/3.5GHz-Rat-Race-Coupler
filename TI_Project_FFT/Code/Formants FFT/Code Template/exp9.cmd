/*
    Linker command file for Experiment 9 (C55x memory map) 
*/

MEMORY
{
    SPRAM   : origin = 00000c0h, length = 0000040
    DARAM0  : origin = 0000100h, length = 0003F00h
    DARAM1  : origin = 0004000h, length = 0004000h
    DARAM2  : origin = 0008000h, length = 0004000h
    DARAM3  : origin = 000c000h, length = 0004000h

    SARAM0  : origin = 0010000h, length = 0004000h
    SARAM1  : origin = 0014000h, length = 0004000h
    SARAM2  : origin = 0018000h, length = 0004000h
    SARAM3  : origin = 001c000h, length = 0004000h
    SARAM4  : origin = 0020000h, length = 0004000h
    SARAM5  : origin = 0024000h, length = 0004000h
    SARAM6  : origin = 0028000h, length = 0004000h
    SARAM7  : origin = 002c000h, length = 0004000h
    SARAM8  : origin = 0030000h, length = 0004000h
    SARAM9  : origin = 0034000h, length = 0004000h
    SARAM10 : origin = 0038000h, length = 0004000h
    SARAM11 : origin = 003c000h, length = 0004000h
    SARAM12 : origin = 0040000h, length = 0004000h
    SARAM13 : origin = 0044000h, length = 0004000h
    SARAM14 : origin = 0048000h, length = 0004000h
    SARAM15 : origin = 004c000h, length = 0004000h

    VECS    : origin = 0ffff00h, length = 00100h  /* reset vector */
}	

 
SECTIONS
{
    vectors  : {} > VECS             /* interrupt vector table */
    .cinit   : {} > SARAM0 
    .text    : {} > SARAM1 
    .stack   : {} > DARAM0 
    .sysstack: {} > DARAM0 
    .sysmem  : {} > DARAM1 
    .data    : {} > DARAM1 
    .bss     : {} > DARAM1 
    .const   : {} > DARAM1 

    fft_coef : {} > SARAM3         /* user defined sections */
    fft_temp : {} > DARAM2 
    fft_twdl : {} > SARAM4 
    fft_in   : {} > SARAM0 align 4 /* word boundary alignment */
    fft_out  : {} > SARAM0 align 4 /* word boundary alignment */   
    iir_code : {} > SARAM1 
    isrs     : {} > SARAM2         
}
