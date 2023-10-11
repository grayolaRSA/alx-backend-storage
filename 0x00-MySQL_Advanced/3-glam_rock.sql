-- script that ranks band lifespans according to sub-genre
-- uses index command

CREATE INDEX idx_stlu ON metal_bands (style);


-- Change NULL values in split to 2022
UPDATE metal_bands
SET split = COALESCE(split, 2022);

-- Rank band lifespans according to the 'Glam rock' sub-genre
SELECT band_name, (split - formed) AS lifespan
FROM metal_bands
WHERE FIND_IN_SET('Glam rock', style) > 0
ORDER BY lifespan DESC;


