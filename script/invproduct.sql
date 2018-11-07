-- View: public.invproduct_product

-- DROP VIEW public.invproduct_product;

CREATE OR REPLACE VIEW public.invproduct_product AS 
 SELECT a.barcode AS id,
    ( SELECT min(inv.barcode::text) AS min
           FROM inv
          WHERE inv.article::text = a.article::text) AS product_tmpl_id,
    a.barcode,
    a.barcode AS default_code
   FROM inv a
  ORDER BY a.barcode;

ALTER TABLE public.invproduct_product
  OWNER TO postgres;
