-- https://www.hackerrank.com/challenges/the-report/problem

SELECT CASE WHEN G.GRADE>=8 THEN S.NAME ELSE "NULL" END AS NAME, G.GRADE, S.MARKS
FROM STUDENTS S, GRADES G
WHERE S.MARKS BETWEEN G.MIN_MARK AND G.MAX_MARK
ORDER BY G.GRADE DESC, NAME

-- github.com/ArutselvanManivannan
