SELECT STARNAME
FROM STARSIN
INNER JOIN MOVIE 
ON MOVIE.YEAR = "1995" AND MOVIE.STUDIONAME = "MGM";