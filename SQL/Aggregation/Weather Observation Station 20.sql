-- https://www.hackerrank.com/challenges/weather-observation-station-20/problem

SET @ROWNUMBER := -1;
SELECT ROUND(AVG(TEMP.LAT_N), 4)
FROM(
    SELECT @ROWNUMBER := @ROWNUMBER +1 AS ROWNUMBER, STATION.LAT_N AS LAT_N
    FROM STATION
    ORDER BY LAT_N
) TEMP
WHERE TEMP.ROWNUMBER IN (FLOOR(@ROWNUMBER/2), CEIL(@ROWNUMBER/2))

-- github.com/ArutselvanManivannan
