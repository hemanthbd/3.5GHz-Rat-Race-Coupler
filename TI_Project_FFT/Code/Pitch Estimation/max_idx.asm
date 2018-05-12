	.data

	.global _max_idx
	
	.text
_max_idx
	MOV #0,AC0 ; Clear AC0
	MOV T0, AC0 ; Move the Counter to AC0
	MOV #0, T0; Current Value
	MOV #0, T1; Max Value
	MOV #0, T2; Current Index
	MOV #0, T3; Max Index
	
Loop1:	MOV *AR0, T0 ; Autocorrelation Values -> T0
		CMP T0 > T1, TC1 ; Compare the Current Value with the Max value, if it is greater, we store that in a Max register and if it isn't, just move-on to the next position		
		BCC SETMAX, TC1 ; If the above condition satisfies, Go to label SETMAX
		
Loop2:	ADD #1, AR0 ; Go to next position of the Autocorrelation array
		ADD #1, T2 ; Increment the current index
		ADD #-1, AC0 ; Decrement your counter
		BCC Loop1, AC0!=#0 ; Conditional Branch to Loop1 till the counter becomes 0
		B  Maxind ; Branch to label Maxind

SETMAX: MOV T0, T1 ; Move the current value -> T1 
		MOV T2, T3 ; Move the Current Index -> T3
		B Loop2 ; Branch to Loop2 to compare the next value

Maxind:	MOV T3, T0 ; Move the Maximum index to T0, which represents your Max Peak Index of your autocorrelation function, and hence the Pitch

	
	RET
	

	.END
