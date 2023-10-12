-- create a trigger to reset valid_email attribute
-- after change of email

DELIMITER //
CREATE TRIGGER valid_email_reset
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
	IF NEW.email <> OLD.email THEN
	   SET NEW.valid_email = 0;
	END IF;
END;
//
DELIMITER ;
