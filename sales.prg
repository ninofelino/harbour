
#include "achoice.ch"
#include "inkey.ch"
#include "dbedit.ch"
local pilih,aAttr,aDate,aName,aSize,aTime
local nlen
set defa to "/mnt/posserver/sales"
nLen := ADir( "*.DBF" )  
//clear
set color to "w+/B"
? nLen
    aName := Array( nLen )   // make room to store the information
    aSize := Array( nLen )
    aDate := Array( nLen )
    aTime := Array( nLen )
    aAttr := Array( nLen )
ADir( "*.DBF", aName, aSize, aDate, aTime, aAttr )
@ 0,0,maxrow(),16 BOX 1
@ 0,17,maxrow(),maxcol() BOX 1
@ maxrow(),20 SAY "F3 PLU"
pilih:=achoice(1,1,maxrow()-1,15,aName,.t.,"cUserFunction")
USE &(aName[pilih]) READONLY
DBEDIT(1,18,maxrow()-2,maxcol()-1,"UserFunc")
do case
endcase

FUNCTION UserFunc( nMode, nCol )
    LOCAL nKey := LastKey()
    LOCAL nRetVal := DE_CONT         // Default return value

    @ maxrow(),20 SAY nkey
    DO CASE
    CASE nMode == DE_IDLE
      // nRetVal := IdleFunc()
    CASE nMode == DE_HITTOP
       Tone( 100, 3 )
    CASE nMode == DE_HITBOTTOM
       Tone( 100, 3 )
      // nRetVal := AppendFunc( nKey )
    CASE nMode == DE_EMPTY
      // nRetVal := EmptyFunc()
    CASE nMode == DE_EXCEPT
      // nRetVal := ExceptFunc( nKey, nCol )
    OTHERWISE
       Tone( 100, 3 )
    ENDCASE

 RETURN nRetVal


FUNCTION cUserFunction( nMode, nCurElement, nRowPos )

    LOCAL nRetVal := AC_CONT     // Default, Continue
    LOCAL nKey := LastKey()

    DO CASE
 // After all pending keys are processed, display message
    CASE nMode == AC_IDLE
    DO CASE
       CASE nCurElement == 1
          @ 22, 5 SAY " Adding   "
       CASE nCurElement == 2
          @ 22, 5 SAY " Editing  "
       CASE nCurElement ==  3
          @ 22, 5 SAY " Deleting "
       CASE nCurElement ==  4
          @ 22, 5 SAY " Updating "
    ENDCASE

       nRetVal := AC_CONT            // Continue AChoice()

    CASE nMode == AC_HITTOP          // Attempt to go past Top
       Tone( 100, 3 )
    CASE nMode == AC_HITBOTTOM       // Attempt to go past
                                     // Bottom
       Tone( 100, 3 )

    CASE nMode == AC_EXCEPT          // Key Exception
       DO CASE
       CASE nKey == K_RETURN         // If RETURN key, select
          nRetVal := AC_SELECT
       CASE nKey == K_ESC            // If ESCAPE key, abort
          nRetVal := AC_ABORT
       OTHERWISE
             nRetVal := AC_GOTO      // Otherwise, go to item
       ENDCASE
    ENDCASE

 RETURN nRetVal 

 FUNCTION DBEditFunc ( nMode, nColumnPos )

    LOCAL RetVal := DE_CONT
    @ maxrow(),60 say LastKey()
    IF ( nMode == DE_EXCEPT )
    
        IF ( LastKey() == K_F5 )
    
            RetVal := DE_REFRESH
            
            ENDIF
            IF ( LastKey() == K_F3 )
                alert("LL")
                RetVal := DE_REFRESH
                
                ENDIF    
    
    ENDIF 
RETURN( RetVal )

