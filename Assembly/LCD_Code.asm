;******************************************************************************
;   This file is a basic template for assembly code for a PIC18F4550. Copy    *
;   this file into your project directory and modify or add to it as needed.  *
;                                                                             *
;   The PIC18FXXXX architecture allows two interrupt configurations. This     *
;   template code is written for priority interrupt levels and the IPEN bit   *
;   in the RCON register must be set to enable priority levels. If IPEN is    *
;   left in its default zero state, only the interrupt vector at 0x008 will   *
;   be used and the WREG_TEMP, BSR_TEMP and STATUS_TEMP variables will not    *
;   be needed.                                                                *
;                                                                             *
;   Refer to the MPASM User's Guide for additional information on the         *
;   features of the assembler.                                                *
;                                                                             *
;   Refer to the PIC18FXX50/XX55 Data Sheet for additional                    *
;   information on the architecture and instruction set.                      *
;                                                                             *
;******************************************************************************
;                                                                             *
;    Filename:                                                                *
;    Date:                                                                    *
;    File Version:                                                            *
;                                                                             *
;    Author:                                                                  *
;    Company:                                                                 *
;                                                                             * 
;******************************************************************************
;                                                                             *
;    Files required: P18F4550.INC                                             *
;                                                                             *
;******************************************************************************

	LIST P=18F4550, F=INHX32	;directive to define processor
	#include <P18F4550.INC>	;processor specific variable definitions

;******************************************************************************
;Configuration bits
;Microchip has changed the format for defining the configuration bits, please 
;see the .inc file for futher details on notation.  Below are a few examples.



;   Oscillator Selection:
 ;   CONFIG	FOSC = XT_XT         ;XT oscillator, XT used by USB

;******************************************************************************
;Variable definitions
; These variables are only needed if low priority interrupts are used. 
; More variables may be needed to store other special function registers used
; in the interrupt routines.

		UDATA

WREG_TEMP	RES	1	;variable in RAM for context saving 
STATUS_TEMP	RES	1	;variable in RAM for context saving
BSR_TEMP	RES	1	;variable in RAM for context saving

;Declaring variables

COUNT RES 1
DVAR RES 1
DVAR2 RES 1


		UDATA_ACS

EXAMPLE		RES	1	;example of a variable in access RAM

;******************************************************************************
;EEPROM data
; Data to be programmed into the Data EEPROM is defined here


DATA_EEPROM	CODE	0xf00000

		DE	"Test Data",0,1,2,3,4,5

;******************************************************************************
;Reset vector
; This code will start executing when a reset occurs.

RESET_VECTOR	CODE	0x0000

		goto	Main		;go to start of main code

;******************************************************************************
;High priority interrupt vector
; This code will start executing when a high priority interrupt occurs or
; when any interrupt occurs if interrupt priorities are not enabled.

HI_INT_VECTOR	CODE	0x0008

		bra	HighInt		;go to high priority interrupt routine

;******************************************************************************
;Low priority interrupt vector and routine
; This code will start executing when a low priority interrupt occurs.
; This code can be removed if low priority interrupts are not used.

LOW_INT_VECTOR	CODE	0x0018

		bra	LowInt		;go to low priority interrupt routine

;******************************************************************************
;High priority interrupt routine
; The high priority interrupt code is placed here to avoid conflicting with
; the low priority interrupt vector.


		CODE

HighInt:

;	*** high priority interrupt code goes here ***


		retfie	FAST

;******************************************************************************
;Low priority interrupt routine
; The low priority interrupt code is placed here.
; This code can be removed if low priority interrupts are not used.

LowInt:
		movff	STATUS,STATUS_TEMP	;save STATUS register
		movff	WREG,WREG_TEMP		;save working register
		movff	BSR,BSR_TEMP		;save BSR register

;	*** low priority interrupt code goes here ***


		movff	BSR_TEMP,BSR		;restore BSR register
		movff	WREG_TEMP,WREG		;restore working register
		movff	STATUS_TEMP,STATUS	;restore STATUS register
		retfie

;******************************************************************************
;Start of main program
; The main program code is placed here.

Main:
	



LCD_DATA EQU PORTD
LCD_CNTRL EQU PORTC 

RS EQU RC0    ;RS=1 (DATA REG)  RS=0 (COMMAND REG)
RW EQU RC1    ;RW=1 (READING)  RW=0 (WRITING)
EN EQU RC2    ;ENABLE
   CLRF TRISD
   CLRF TRISC
   BCF LCD_CNTRL,EN   ;ENABLE IDLE LOW EN=0
   CALL LDELAY
   MOVLW 0X38         ;LCD INITIALIZE 2LINES 5*7 MATRIX
   CALL COMNWRT       ;COMMAND SUBROUTINE
   CALL LDELAY
   MOVLW 0X0E         ;DISPLAY ON ,CURSOR ON
   CALL COMNWRT        ;COMMAND SUBROUTINE
   CALL LDELAY         ;some time to LCD
   MOVLW 0X01          ;CLEAR LCD
   CALL COMNWRT        ;COMMAND SUBROUTINE
   CALL LDELAY
   MOVLW 0X06           ;SHIFT cursor right
   CALL COMNWRT         ;COMMAND SUBROUTINE
   CALL LDELAY
   MOVLW 0X84           ;cursor at line 1 ,pos 4
   CALL COMNWRT
   CALL LDELAY
 
   MOVLW A'Y'
   CALL DATAWRT
   CALL LDELAY
  MOVLW A'E'           ;display letter
   CALL DATAWRT            
   CALL LDELAY
   MOVLW A'A'
   CALL DATAWRT
   CALL LDELAY
  MOVLW A'R'           ;display letter
   CALL DATAWRT            
   CALL LDELAY
  
  MOVLW A' '           ;display letter
   CALL DATAWRT            
   CALL LDELAY
  
  MOVLW A'2'           ;display letter
   CALL DATAWRT            
   CALL LDELAY
   MOVLW A'0'
   CALL DATAWRT
   CALL LDELAY
  MOVLW A'1'           ;display letter
   CALL DATAWRT            
   CALL LDELAY
   MOVLW A'7'
   CALL DATAWRT
   CALL LDELAY       
AGAIN BTG LCD_CNTRL,0  ;BIT TOGGLE
      BRA AGAIN        ;stay here
COMNWRT 
      MOVWF LCD_DATA   ;w=38H
   BCF LCD_CNTRL,RS    ;rs=0 (contrl reg)
   BCF LCD_CNTRL,RW    ;rw=0 (writing)
   BSF LCD_CNTRL,EN    ;en=1  for high pulse
   CALL LDELAY
   BCF LCD_CNTRL,EN    ;en=0  for H-to-L pulse
    RETURN
DATAWRT
     MOVWF LCD_DATA    ; wreg=ascii value
   BSF LCD_CNTRL,RS    ;RS=1 (DATA REG)
   BCF LCD_CNTRL,RW    ;RW=0 (WRITE)
   BSF LCD_CNTRL,EN    ;EN=1 FOR HIGH PULSE
   CALL LDELAY
   BCF LCD_CNTRL,EN     ;EN=0  FOR HIGH TO LOW PULSE
   RETURN

;delay subroutine
LDELAY    movlw 0XFF
         movwf 	COUNT  ;MYREG=5,the counter
AGAINN    NOP
         NOP            ;no operation wastes clock cycles
         DECF COUNT,F
         BNZ  AGAINN   ;reepeat until myreg=0
          return       ;return to caller

;	*** main code goes here ***


;******************************************************************************
;End of program

		END
