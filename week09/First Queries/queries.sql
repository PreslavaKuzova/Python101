----- task01 -----
SELECT ADDRESS 
FROM STUDIO
WHERE NAME = "MGM";

----- task02 -----
SELECT BIRTHDATE
FROM MOVIESTAR
WHERE NAME = "Kim Basinger";

----- task03 -----
SELECT NAME
FROM MOVIEEXEC
WHERE NETWORTH >= 10000000;

----- task04 -----
SELECT NAME 
FROM MOVIESTAR
WHERE GENDER = "M" OR ADDRESS LIKE "%Prefect Rd%";

----- task05 -----
INSERT INTO MOVIESTAR
VALUES("Zahari Baharov", "Address unknown", "M", "1980-12-08");

----- task06 -----
DELETE FROM STUDIO
WHERE ADDRESS LIKE "%5%";

----- task07 -----
UPDATE MOVIE
SET STUDIONAME = 'Fox'
WHERE TITLE LIKE '%star%'; 
