SET @NUM1=1;
SET @NUM2=1;
SELECT GROUP_CONCAT(I SEPARATOR '&')
FROM (
    SELECT @NUM1:=@NUM1+1 as I
    FROM
        information_schema.tables t1,
        information_schema.tables t2
    LIMIT 1000
) tempNum
WHERE NOT EXISTS(
    SELECT *
    FROM (
        SELECT @NUM2:=@NUM2+1 as J
        FROM
            information_schema.tables t1,
            information_schema.tables t2
        LIMIT 1000
    ) tatata
    WHERE I>J AND MOD(I,J)=0
)

-- github.com/ArutselvanManivannan
