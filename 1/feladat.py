import sqlite3
from pprint import pprint

conn = sqlite3.connect("kereskedes.db")
curs = conn.cursor()

curs.execute("CREATE TABLE IF NOT EXISTS autok (jogositvanyszam TEXT, vasarlonev TEXT, rendszam TEXT, ar REAL, tipus TEXT)")
# curs.execute("INSERT INTO autok VALUES ('DH123456', 'John', 'DFG-123', 34000000, 'Toyota')")
# curs.execute("INSERT INTO autok VALUES ('QW345678', 'Cait', 'FTG-456', 3400000, 'Tesla')")
# curs.execute("INSERT INTO autok VALUES ('HG125476', 'Jayce', 'IJH-233', 66000000, 'Peugea')")
# curs.execute("INSERT INTO autok VALUES ('HJ768765', 'Viktor', 'CFR-999', 14050500, 'Honda')")
# curs.execute("INSERT INTO autok VALUES ('IJ444444', 'Jhin', 'ZHG-444', 44444444, 'Audi')")
# curs.execute("INSERT INTO autok VALUES ('UH897643', 'Aatrox', 'AAA-767', 5600000, 'Ferrari')")
# curs.execute("INSERT INTO autok VALUES ('IJ763210', 'Ezreal', 'JJH-353', 1007000, 'Toyota')")
# curs.execute("INSERT INTO autok VALUES ('TZ665432', 'Sera', 'TXT-898', 340000, 'Toyota')")
# curs.execute("INSERT INTO autok VALUES ('OO776655', 'Sora', 'HJH-666', 10050000, 'Opel')")
# curs.execute("INSERT INTO autok VALUES ('BH888976', 'Senna', 'IKJ-877', 22004005, 'BMW')")

curs.execute("SELECT tipus FROM autok WHERE tipus Like 'T%'")
curs.execute("SELECT vasarlonev,ar FROM autok WHERE ar > 10000000")
curs.execute("SELECT MAX(ar) FROM autok")
curs.execute("SELECT SUM(ar) FROM autok")

curs.execute("SELECT * FROM autok")
pprint(curs.fetchall())

conn.commit()
conn.close()