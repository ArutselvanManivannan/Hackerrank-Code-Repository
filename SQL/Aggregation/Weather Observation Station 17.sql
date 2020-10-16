-- https://www.hackerrank.com/challenges/weather-observation-station-17/problem

SELECT ROUND(LONG_W, 4)
FROM
(
    SELECT LONG_W
    FROM STATION
    WHERE LAT_N>38.7780
    ORDER BY LAT_N
) TEMP
LIMIT 1

-- github.com/ArutselvanManivannan
