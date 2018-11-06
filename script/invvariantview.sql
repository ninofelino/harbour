- View: public.invvariant

-- DROP VIEW public.invvariant;

CREATE OR REPLACE VIEW public.invvariant AS 
 SELECT min(inv.barcode::text) AS key,
    count(*) AS count,
    inv.article,
    array_agg(inv.ukuran) AS ukuran,
    array_agg(inv.barcode) AS barcode,
    sum(inv.lqoh) AS onhand,
    round(avg(inv.modal), 0) AS modal,
    round(avg(inv.hargajual), 0) AS hargajual,
    min(inv.lastrcv) AS lastrcv,
    min(inv.firstrcv) AS firstrcv
   FROM inv
  GROUP BY inv.article;

ALTER TABLE public.invvariant
  OWNER TO postgres;
