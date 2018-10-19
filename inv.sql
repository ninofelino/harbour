select id,name,'consu' as type,1 as categ_id,modal as list_price,True as sale_ok,True as purchase_ok
,1 as uom_id
 from
(
select min(barcode) as id,article as name,count(*),array_agg(ukuran) as ukuran,array_agg(barcode) as barcode,sum(lqoh) as onhand,round(avg(modal),0) as modal,round(avg(hargajual),0) as hargajual,min(lastrcv) as lastrcv,min(firstrcv) as firstrcv from inv
group by article
) t