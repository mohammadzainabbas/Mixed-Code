#LCD INTERFACE ASSEMBLY LANGUAGE



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