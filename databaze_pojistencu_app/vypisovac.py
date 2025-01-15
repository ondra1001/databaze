class Vypisovac:

    @classmethod
    def vypis_spatne_jmeno_nebo_prijmeni(cls, jmeno_nebo_prijmeni):
        print(f"\nŠpatně zadané {jmeno_nebo_prijmeni}!")

    @classmethod
    def vypis_spatne_datum_narozeni(cls):
        print("\nŠpatně zadané datum!")

    @classmethod
    def vypis_spatne_tel_cislo(cls):
        print("\nŠpatně zadané telefonní číslo!")

    @classmethod
    def vypis_ulozeni_pojistence(cls):
        print("\nPojištěnec byl uložen.")

    @classmethod
    def vypis_pojistence(cls, pojistenci):
        for i in pojistenci:
            print(f"\nJméno: {i[0]} {i[1]} Datum narozeni: {i[2]} Tel.Číslo: {i[3]}")

    @classmethod
    def vypis_pokracovani(cls):
        print("\nPokud si přejete pokračovat, zmáčkněte enter.")

    @classmethod
    def vypis_vymazani_pojistence(cls):
        print("\nPojištěnec byl vymazán.")