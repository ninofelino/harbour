-- Table: public.inv

-- DROP TABLE public.inv;

CREATE TABLE public.inv
(
  barcode character varying(8) NOT NULL,
  article character varying(40),
  ukuran character varying(4),
  desc1 character varying(50),
  mclass character varying(40),
  hargajual integer,
  modal integer,
  lqoh integer,
  lastrcv date,
  firstrcv date,
  CONSTRAINT inv_pkey PRIMARY KEY (barcode)
)
WITH (
  OIDS=FALSE
);
ALTER TABLE public.inv
  OWNER TO postgres;

-- Index: public.article

-- DROP INDEX public.article;

CREATE INDEX article
  ON public.inv
  USING btree
  (article COLLATE pg_catalog."default");

