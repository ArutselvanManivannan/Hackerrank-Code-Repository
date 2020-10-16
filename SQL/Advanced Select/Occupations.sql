-- https://www.hackerrank.com/challenges/occupations/problem

SELECT MAX(DOCTOR), MAX(PROFESSOR), MAX(SINGER), MAX(ACTOR)
FROM(
    SELECT
        RANK() OVER(PARTITION BY OCCUPATION ORDER BY NAME) RANK,
        CASE OCCUPATION WHEN 'Doctor' THEN NAME END AS DOCTOR,
        CASE OCCUPATION WHEN 'Professor' THEN NAME END AS PROFESSOR,
        CASE OCCUPATION WHEN 'Singer' THEN NAME END AS SINGER,
        CASE OCCUPATION WHEN 'Actor' THEN NAME END AS ACTOR
    FROM
        OCCUPATIONS
)
GROUP BY RANK
ORDER BY RANK;

-- github.com/ArutselvanManivannan

