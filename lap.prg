set defa to "/home/server/posserver/ics/DAT"


achoice(3,1,maxrow()-2,20,{"RCV2","TRANS1","TRANS2","TRANS2S1","TRANS2S2","REST1","RETST2"})
use "RCV2.DBF" SHARED
alert("RT")
dbedit(1,1,maxrow()-1,maxcol()-1)
