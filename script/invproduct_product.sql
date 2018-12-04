SELECT a.barcode AS id,
    ( SELECT min(inv.barcode::text) AS min
           FROM inv
          WHERE inv.article::text = a.article::text) AS product_tmpl_id,
    a.barcode,
    a.barcode AS default_code,a.ukuran,(select id from product_attribute_value where name=ukuran)
   FROM inv a
  ORDER BY a.barcode;
