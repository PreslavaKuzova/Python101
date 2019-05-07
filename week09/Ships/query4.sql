SELECT CLASSES.COUNTRY, SHIPS.NAME
FROM SHIPS
JOIN CLASSES
ON CLASSES.CLASS = SHIPS.CLASS
WHERE SHIPS.NAME NOT IN 
    (SELECT SHIP
    FROM OUTCOMES)
GROUP BY CLASSES.COUNTRY;