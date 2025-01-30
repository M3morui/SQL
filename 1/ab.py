import sqlite3
from pprint import pprint

conn = sqlite3.connect("felhasznalo.db")
curs = conn.cursor()

#tábla létrehozása
curs.execute("CREATE TABLE IF NOT EXISTS szemely (nev TEXT, kor INTEGER, nem TEXT)")

#a tabla feltöltése
# curs.execute("INSERT INTO szemely VALUES ('John', 32, 'ferfi')")
# curs.execute("INSERT INTO szemely VALUES ('Erika', 42, 'no')")
# curs.execute("INSERT INTO szemely VALUES ('Kinga', 51, 'no')")
# curs.execute("INSERT INTO szemely VALUES ('Leonard', 52, 'ferfi')")
# curs.execute("INSERT INTO szemely VALUES ('Emily', 35, 'no')")
# curs.execute("INSERT INTO szemely VALUES ('Edward', 27, 'ferfi')")

#az adatok megjelenítése
curs.execute("SELECT * FROM szemely")

curs.execute("SELECT nev,kor,nem FROM szemely WHERE RowID = 1")
curs.execute("SELECT nev,kor FROM szemely WHERE kor>50")

#adatok módosítása
curs.execute("UPDATE szemely SET nem=? WHERE nem=?", ("nő","no"))

#adatok törlése
curs.execute("DELETE FROM szemely WHERE RowID = 8")
curs.execute("SELECT * FROM szemely")
pprint(curs.fetchall())

#az adatok mentése
conn.commit()
conn.close()