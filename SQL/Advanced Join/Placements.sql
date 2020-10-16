-- https://www.hackerrank.com/challenges/placements/problem

SELECT NAME
FROM STUDENTS S
JOIN FRIENDS F
ON S.ID=F.ID
JOIN PACKAGES P1
ON P1.ID=S.ID
JOIN PACKAGES P2
ON P2.ID=F.FRIEND_ID
WHERE P2.SALARY > P1.SALARY
ORDER BY P2.SALARY;


-- github.com/ArutselvanManivannan
