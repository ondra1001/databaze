import sqlite3
class ManagerDbPojistencu:

    def __init__(self, databaze):
        self.databaze = databaze
        self.vytvor_tabulku()

    def vytvor_spojeni_db(self):
        return sqlite3.connect(self.databaze)

    def vytvor_tabulku(self):
        sql_vytvor_tabulku = """
        CREATE TABLE IF NOT EXISTS pojistenci(
            jmeno TEXT,
            prijmeni TEXT,
            datum_narozeni TEXT,
            telefon TEXT);
            """
        with self.vytvor_spojeni_db() as spojeni:
            spojeni.cursor().execute(sql_vytvor_tabulku)

    def uloz_pojisteneho(self, jmeno, prijmeni, datum_narozeni, tel_cislo):
        sql_vloz_pojisteneho = """
        INSERT INTO pojistenci(jmeno, prijmeni, datum_narozeni, telefon)
        VALUES (?, ?, ?, ?);"""

        with self.vytvor_spojeni_db() as spojeni:
            spojeni.cursor().execute(sql_vloz_pojisteneho, (jmeno, prijmeni, datum_narozeni, tel_cislo))
            spojeni.commit()

    def vyhledej_pojisteneho(self, jmeno, prijmeni):
        sql_vyber_pojisteneho = """
        SELECT * FROM pojistenci WHERE jmeno = ? AND prijmeni = ?;"""

        with self.vytvor_spojeni_db() as spojeni:
            cursor = spojeni.cursor()
            cursor.execute(sql_vyber_pojisteneho, (jmeno, prijmeni))
            return cursor.fetchall()

    def vrat_vsechny_pojistene(self):
        sql_vyber_vsechny = """
        SELECT * FROM pojistenci"""

        with self.vytvor_spojeni_db() as spojeni:
            cursor = spojeni.cursor()
            cursor.execute(sql_vyber_vsechny)
            return cursor.fetchall()


    def vymaz_pojisteneho(self, jmeno, prijmeni, datum_narozeni):
        sql_vymaz_pojistence = """
        DELETE FROM pojistenci WHERE jmeno = ? AND prijmeni = ? AND datum_narozeni = ?"""

        with self.vytvor_spojeni_db() as spojeni:
            cursor = spojeni.cursor()
            cursor.execute(sql_vymaz_pojistence, (jmeno, prijmeni, datum_narozeni))




