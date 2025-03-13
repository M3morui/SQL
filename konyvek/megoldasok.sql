-- A feladatok megoldására elkészített SQL parancsokat illessze be a feladat sorszáma után!


-- 1. feladat:
CREATE DATABASE nagykonyv CHARACTER SET utf8 COLLATE utf8_hungarian_ci;

-- 3. feladat:
SELECT DISTINCT nemzetiseg FROM `szerzo` WHERE nemzetiseg NOT LIKE "magyar";

-- 4. feladat:
SELECT nev AS nev, 2005-szulEv AS kor FROM szerzo WHERE halEv IS NULL;

-- 5. feladat:
SELECT szerzo.nev AS nev, konyv.helyezes AS legjobb
FROM szerzo
LEFT JOIN konyv ON szerzo.id = konyv.szerzoId
WHERE szerzo.nemzetiseg LIKE "magyar"
ORDER BY legjobb ASC;

-- 6. feladat:
SELECT szerzo.nev AS nev, COUNT(konyv.id) AS konyvek
FROM szerzo
LEFT JOIN konyv ON szerzo.id = konyv.szerzoId
GROUP BY nev
ORDER BY konyvek DESC, nev ASC;
