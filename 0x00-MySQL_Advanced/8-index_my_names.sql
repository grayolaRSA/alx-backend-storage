-- script to create an index on table names
-- on column name

-- add column for first letter
ALTER TABLE names ADD COLUMN first_letter CHAR(1);
UPDATE names SET first_letter = SUBSTRING(name, 1, 1);
-- create index
CREATE INDEX idx_name_first ON names (
-- select first character of name
first_letter
);
