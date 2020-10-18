-- https://www.hackerrank.com/challenges/challenges/problem

SELECT H.HACKER_ID, H.NAME, COUNT(C.CHALLENGE_ID) AS TOTAL
FROM HACKERS H
JOIN CHALLENGES C
ON H.HACKER_ID=C.HACKER_ID
GROUP BY H.HACKER_ID, H.NAME
HAVING
    TOTAL = (
        SELECT MAX(TOTAL1)
        FROM(
            SELECT COUNT(*) AS TOTAL1
            FROM CHALLENGES
            GROUP BY HACKER_ID
        ) TEMP1
    )
    OR
    TOTAL IN (
        SELECT TOTAL2
        FROM(
            SELECT COUNT(*) AS TOTAL2
            FROM CHALLENGES
            GROUP BY HACKER_ID
        ) TEMP2
        GROUP BY TOTAL2
        HAVING COUNT(TEMP2.TOTAL2)=1
    )
ORDER BY TOTAL DESC, H.HACKER_ID

-- github.com/ArutselvanManivannan
