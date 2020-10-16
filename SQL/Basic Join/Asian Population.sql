-- https://www.hackerrank.com/challenges/asian-population/problem


SELECT SUM(C1.POPULATION)
FROM CITY C1
JOIN COUNTRY C2
ON C1.COUNTRYCODE=C2.CODE
WHERE C2.CONTINENT='Asia'

-- github.com/ArutselvanManivannan
