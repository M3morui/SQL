import sqlite3
from pprint import pprint

conn = sqlite3.connect("vizsga.db")
curs = conn.cursor()

# curs.execute("CREATE TABLE IF NOT EXISTS vizsgazok (azonosito INTEGER, nev TEXT, szulido INTEGER, pontszam REAL)")
# curs.execute("INSERT INTO vizsgazok VALUES (7223231, 'John Watson', 1995, 75.4)")
# curs.execute("INSERT INTO vizsgazok VALUES (7545532, 'Proba Elek', 1997, 50.6)")
# curs.execute("INSERT INTO vizsgazok VALUES (7656565, 'Jane Doe', 1995, 75.4)")
# curs.execute("INSERT INTO vizsgazok VALUES (7934334, 'Sherlock Holmes', 2000, 90.4)")
# curs.execute("INSERT INTO vizsgazok VALUES (7434332, 'Proba Kinga', 2001, 56.6)")

curs.execute("SELECT * FROM vizsgazok")

#pontszam több mint 56 meg lesz jelenítve
curs.execute("SELECT nev,pontszam FROM vizsgazok WHERE pontszam > 56.6")

#p vel kezdődik
curs.execute("SELECT nev FROM vizsgazok WHERE nev Like 'P%'")

#legkisebb pontszam
curs.execute("SELECT MIN(pontszam) FROM vizsgazok")

#legnagyobb pontszam
curs.execute("SELECT MAX(pontszam) FROM vizsgazok")

#osszegzi
curs.execute("SELECT SUM(pontszam) FROM vizsgazok")

#átlag
curs.execute("SELECT AVG(pontszam) FROM vizsgazok")

curs.execute("UPDATE vizsgazok SET nev='Kiss Jenő' WHERE RowID = 6")
curs.execute("UPDATE vizsgazok SET szulido=2004 WHERE nev='Kiss Jenő'")
curs.execute("DELETE FROM vizsgazok WHERE RowID = 7")


curs.execute("SELECT * FROM vizsgazok")
pprint(curs.fetchall())

conn.commit()
conn.close()