-- Script to create an index on the `names` table
-- SELECT SUBSTRING(name, 1, 1) AS first_letter FROM names;
-- SELECT name INTO first_letter FROM names;
-- SELECT LEFT(name, 1) AS first_letter
-- FROM names;
-- Create a computed (generated) column for the first letter
ALTER TABLE names ADD COLUMN first_letter CHAR(1) GENERATED ALWAYS AS (LEFT(name, 1)) STORED;
CREATE INDEX idx_name_first ON names (name);
