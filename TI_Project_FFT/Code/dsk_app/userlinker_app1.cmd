/*
 *  userlinker_app1.cmd
 *
 *  This file is a user specified linker command file that adds a logical
 *  memory section called coeff_sect whose contents will be placed in a
 *  block of internal memory called SARAM_A.  This definition is associated
 *  with the #pragma DATA_SECTION directive in highpass.h that tells the
 *  linker to allocate the COEFFS array in the coeff_sect logical memory
 *  section instead of the default location with the rest of the program
 *  data.  The purpose of separating the coefficients from the other data
 *  is to insure that they reside in a different block than the data buffers.
 *  The DSP uses a high performance multiply-accumulate function (MAC) in
 *  its FIR filter implementation, if the inputs to the MAX reside in
 *  different blocks the instruction can complete in a single cycle.
 *
 *  dsk_app1cfg.cmd is the auto-generated linker command file that reflects
 *  the BIOS configuration settings in the file dsk_app1.cdb.  The main
 *  memory section definitions and libraries that need to be linked in are
 *  all specified there.  The Code Composer project for dsk_app1 uses 
 *  userlinker_app1.cmd as its linker command file.  userlinker_app1.cmd
 *  in turn includes dsk_app1cfg.cmd to create a full set of linker
 *  definitions. 
 */
 
-l dsk_app1cfg.cmd

SECTIONS {

 coeff_sect > SARAM_A
 .outputpingL   : {} > DARAM PAGE 0, align(256)  /* this is due to long-word data memory access */
 .outputpingR   : {} > DARAM PAGE 0, align(256)  /* this is due to long-word data memory access */
 .outputpongL   : {} > DARAM PAGE 0, align(256)  /* this is due to long-word data memory access */
 .outputpongR   : {} > DARAM PAGE 0, align(256)  /* this is due to long-word data memory access */
} 
