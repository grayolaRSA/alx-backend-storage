-- script to create an index on table names
-- on column name and score

DELIMITER //
CREATE PROCEDURE add_index_on_name_and_score()
BEGIN
  -- add first letter column
  IF NOT EXISTS (SELECT 1 FROM information_schema.columns WHERE table_name = 'names' AND column_name = 'first_letter') THEN
     ALTER TABLE names ADD COLUMN first_letter CHAR(1);
     UPDATE names SET first_letter = SUBSTRING(name, 1, 1);
  END IF;

  -- create index for score
  CREATE INDEX idx_name_first_score ON names (
  -- select first character of name and score columns
  first_letter, score
  );
END;
//
DELIMITER ;

CALL add_index_on_name_and_score();
