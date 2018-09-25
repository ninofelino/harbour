memvar spl
m->spl:={}
cls
set defa to "/home/server"
use SUP.DBF shared new
//dbedit()
select SUP
do while !eof()
   aadd(m->spl,sup->desc)
  // ? sup->desc
skip
enddo
//achoice(1,1,20,20,m->spl)
use INV.DBF shared new
SELECT INV
IF .NOT. FILE("INV____1.ntx")
      INDEX ON "CODE" TO INV_____1
      SET INDEX TO INV_____1
ENDIF

IF .NOT. FILE("INV____2.ntx")
      INDEX ON "DESC1" TO INV_____2
      SET INDEX TO INV_____2
ENDIF

@ maxrow()-1,20 SAY "F2 Edit  F3 Search"

dbedit(1,20,maxrow()-2,maxcol()-3,,"keypad")
function keypad()
      local n:=lastkey()
      local hasil:=1
      local layar 
      local getlist:={}
      local ccolor:=1 
      local baris,kolom,atas,bawah
      
      
            
      do case
      case n==27
            alert("Keluar Dari Program")
              hasil:=0 
              case n==-2
                  
                  cari()
                         
         case n==-3
            save screen to layar
           
            
          //  INV->RECLOCK()
          baris:=(maxrow()/2)
          kolom:=(maxcol()/2)
          
          set color to "W+/b"
          @ baris, 10 CLEAR TO 20, 40
            @ baris+13,kolom-25 CLEAR TO baris-13,kolom+25 
            @ baris+13,(maxcol()/2)-25,(maxrow()/2)-13,(maxcol()/2)+25 BOX 1
            @ baris-12,(maxcol()/2)-22  SAY "BARCODE    "  GET INV->CODE 
            @ baris-11,(maxcol()/2)-22   SAY "Supplier   " 
            @ baris-10,kolom-12,20, kolom+12 GET INV->SUPNAME LISTBOX m->spl CAPTION "&Color" 
            @ baris-9,kolom-22 SAY "Mclass     " GET INV->MCLSCODE 
            @ baris-8,kolom-22 SAY "Article    " GET INV->DESC1           
            @ baris-7,kolom-22 SAY "Ukuran     " GET INV->TUNIT3 
            @ baris-6,kolom-22 SAY "Harga Modal" GET INV->COSTPRC
            @ baris-5,kolom-22 SAY "Harga Modal" GET INV->SELLPRC
            @ baris-4,kolom-22 SAY "Harga Jual " GET INV->SELLPRC1
            @ baris-3,kolom-22 SAY "Harga Jual2" GET INV->SELLPRC1
            
            READ 
            alert("edit")
            rest screen from layar 

      endcase
      @ 1,1 SAY n
      



return hasil


function popup()
         alert("pop")
return nil      

function cari
       local carif
       local caridata:=rtrim(INV->CODE)
       LOCAL GetList := {}
        set cursor on
       SELECT INV
     //  SET INDEX TO INV____1
       save screen to carif
       @ 10,10,12,45 BOX 1
       @ 11,11 SAY "cari" GET caridata
        read
        INV->(dbseek(caridata))
        restore screen from carif
return nil      