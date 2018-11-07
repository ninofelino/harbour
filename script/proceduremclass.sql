CREATE OR REPLACE FUNCTION mclass(name)
RETURNS integer AS $total$
declare
	total integer;
BEGIN
   SELECT id  into total FROM MCLASS where name=$1;
   RETURN total;
END;
$total$ LANGUAGE plpgsql;