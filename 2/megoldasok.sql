-- A feladatok megoldására elkészített SQL parancsokat illessze be a feladat sorszáma után!


-- 8. feladat:
CREATE DATABASE konyvtarak CHARACTER SET utf8 COLLATE utf8_hungarian_ci;

-- 10. feladat:

UPDATE megyek SET megyeNev="Budapest" WHERE megyeNev LIKE "BP";
-- 11. feladat:

SELECT konyvtarNev, irsz 
FROM konyvtarak
WHERE konyvtarNev LIKE "%Szakkönyvtára";
-- 12. feladat:
SELECT konyvtarak.konyvtarNev, konyvtarak.irsz , konyvtarak.cim
FROM konyvtarak
ORDER BY konyvtarak.irsz ASC, konyvtarak.konyvtarNev ASC;

-- 13. feladat:
SELECT telepNev, COUNT(id) AS konyvtarDarab
FROM konyvtarak INNER JOIN telepulesek
ON konyvtarak.irsz=telepulesek.irsz
GROUP BY telepNev HAVING konyvtarDarab >=7;

-- 14. feladat:

SELECT megyeNev, COUNT(irsz) AS telepulesDarab
FROM telepulesek INNER JOIN megyek
ON telepulesek.megyeId=megyek.id
WHERE irsz NOT LIKE "1%"
GROUP BY megyeNev ORDER BY telepulesDarab DESC;
