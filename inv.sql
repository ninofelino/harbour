select min(barcode) as key,count(*),article,array_agg(ukuran),array_agg(barcode) as barcode,sum(lqoh) as onhand,round(avg(modal),0) as modal,round(avg(hargajual),0) as hargajual,min(lastrcv) as lastrcv,min(firstrcv) as firstrcv from inv
group by article