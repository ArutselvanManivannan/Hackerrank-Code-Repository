SET @N=21;
SELECT REPEAT('* ', @N:=@N-1)
FROM INFORMATION_SCHEMA.TABLES

-- github.com/ArutselvanManivannan
