-- a script that lists all the cities of california
SELECT *
FROM cities
WHERE state_id IN (
	SELECT *
	FROM states
	WHERE name = 'California'
)
ORDER BY cities.id ASC;
