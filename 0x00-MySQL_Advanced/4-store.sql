-- create a trigger to decrease qty in table items
-- after increase of orders corresponding to item in table order

DELIMITER //
CREATE TRIGGER item_order
BEFORE INSERT ON orders
FOR EACH ROW
BEGIN
  DECLARE quantity_to_decrease INT;
  -- SELECT (SELECT quantity FROM items WHERE name = NEW.item_name) - New.number INTO quantity_to_decrease;
 --  FROM items
 --  WHERE name = NEW.item_name;
 SELECT New.number INTO quantity_to_decrease; 
  
  UPDATE items
  SET quantity = quantity - quantity_to_decrease
  WHERE name = NEW.item_name;
END;
//
DELIMITER ;
