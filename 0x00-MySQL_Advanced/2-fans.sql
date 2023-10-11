-- script that ranks country origins by number of fans
-- uses index command

SELECT origin, SUM(fans) as nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC;


