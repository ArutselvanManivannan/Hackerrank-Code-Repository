SET @N=0;
SELECT REPEAT('* ', @N:=@N+1)
FROM INFORMATION_SCHEMA.TABLES
LIMIT 20


-- github.com/ArutselvanManivannan
