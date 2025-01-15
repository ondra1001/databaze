from _datetime import datetime


class Rozhrani:

    def __init__(self):
        self.rozhrani()


    def rozhrani(self):
        print(f"""
        {20 * "_"}
        Evidence pojištěných
        {20 * "_"}

        Vyberte si akci:

        1 - Pridat noveho pojisteneho
        2 - Vypsat vsechny pojistene
        3 - Vyhledat pojisteneho
        4 - Vymaž pojištěného
        5 - Konec\n""")

    def vrat_volbu(self):
        volba = input("Zadejte volbu: ")
        return volba
    
    def vrat_jmeno(self):
        jmeno = input("Zadejte jméno: ")
        return jmeno.capitalize()

    def vrat_prijmeni(self):
        prijmeni = input("Zadejte příjmení: ")
        return prijmeni.capitalize()

    def vrat_datum_narozeni(self):
        datum_narozeni = input("Zadejte datum narozeni (d.m.r): ")

        return datum_narozeni

    def vrat_telefonni_cislo(self):
        tel_cislo = input("Zadejte telefonní číslo: ")
        return tel_cislo