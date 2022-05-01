-- Wheater Observation Station 4

SELECT
  COUNT(CITY) - COUNT (DISTINCT CITY)
FROM
  STATION;