-- https://www.hackerrank.com/challenges/symmetric-pairs/problem

SELECT F1.X, F1.Y
FROM FUNCTIONS F1
JOIN FUNCTIONS F2
ON F1.X=F2.Y AND F2.X=F1.Y
GROUP BY F1.X, F1.Y
HAVING F1.X < F1.Y OR COUNT(F1.X) > 1
ORDER BY F1.X, F1.Y;


-- github.com/ArutselvanManivannan
