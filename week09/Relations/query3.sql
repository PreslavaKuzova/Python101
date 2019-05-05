--- Adds the column President in the table Studio ---
ALTER TABLE STUDIO ADD COLUMN PRESIDENT CHAR(15);

--- Add values to the column ---
UPDATE STUDIO
SET PRESIDENT = "Bob Iger"
WHERE NAME = "Disney";

UPDATE STUDIO
SET PRESIDENT = "Roger Ailes"
WHERE NAME = "Fox";

UPDATE STUDIO
SET PRESIDENT = "Scott Sibella"
WHERE NAME = "MGM";

UPDATE STUDIO
SET PRESIDENT = "George Winslow"
WHERE NAME = "Paramount";

UPDATE STUDIO
SET PRESIDENT = "Marlene Angelo"
WHERE NAME = "USA Entertainment";

UPDATE STUDIO
SET PRESIDENT = "Kevin Ken Tsujihara"
WHERE NAME = "Warner Bros";


--- Get the name of the president of MGM ---
SELECT PRESIDENT
FROM STUDIO 
WHERE NAME = "MGM";


