-- create a function that divides a result for division
-- returns 0 if second number is 0

DELIMITER ??
CREATE FUNCTION SafeDiv(a INT, b INT)
RETURNS DECIMAL(10, 2)
BEGIN
  IF b = 0 THEN
    RETURN 0;
  ELSE
    RETURN CAST(a AS DECIMAL(10, 2)) / b;
  END IF;
END
??
DELIMITER ;
