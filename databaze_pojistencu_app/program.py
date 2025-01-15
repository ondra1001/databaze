from validace import Kontrolor
from manager_pojistencu import ManagerDbPojistencu
from rozhrani import Rozhrani
from vypisovac import Vypisovac
import os


def zadej_jmeno(rozhrani):
    jmeno = rozhrani.vrat_jmeno()
    je_jmeno_validni = Kontrolor.zvaliduj_jmeno_nebo_prijmeni(jmeno)
    if not je_jmeno_validni:
        Vypisovac.vypis_spatne_jmeno_nebo_prijmeni("jmeno")
        return zadej_jmeno(rozhrani)
    else:
        return jmeno

def zadej_prijmeni(rozhrani):
    prijmeni = rozhrani.vrat_prijmeni()
    je_prijmeni_validni = Kontrolor.zvaliduj_jmeno_nebo_prijmeni(prijmeni)
    if not je_prijmeni_validni:
        Vypisovac.vypis_spatne_jmeno_nebo_prijmeni("příjmení")
        return zadej_prijmeni(rozhrani)
    else:
        return prijmeni

def zadej_datum_narozeni(rozhrani):
    datum = (rozhrani.vrat_datum_narozeni())
    je_datum_narozeni_validni = Kontrolor.zvaliduj_datum_narození(datum)
    if not je_datum_narozeni_validni:
        Vypisovac.vypis_spatne_datum_narozeni()
        return zadej_datum_narozeni(rozhrani)
    else:
        return datum

def zadej_tel_cislo(rozhrani):
    tel_cislo = rozhrani.vrat_telefonni_cislo()
    je_tel_cislo_validni = Kontrolor.zvaliduj_tel_cislo(tel_cislo)
    if not je_tel_cislo_validni:
        Vypisovac.vypis_spatne_tel_cislo()
        return zadej_tel_cislo(rozhrani)
    else:
        return tel_cislo


def main():

    manager_pojistencu = ManagerDbPojistencu("databaze_pojistencu.db")

    rozhrani = Rozhrani()

    volba = rozhrani.vrat_volbu()

    match volba:
        case "1":
            jmeno = zadej_jmeno(rozhrani)
            prijmeni = zadej_prijmeni(rozhrani)
            vek = zadej_datum_narozeni(rozhrani)
            tel_cislo = zadej_tel_cislo(rozhrani)
            manager_pojistencu.uloz_pojisteneho(jmeno, prijmeni, vek, tel_cislo)
            Vypisovac.vypis_ulozeni_pojistence()
            Vypisovac.vypis_pokracovani()
            pokracovani = input()
        case "2":
            pojistenci = manager_pojistencu.vrat_vsechny_pojistene()
            Vypisovac.vypis_pojistence(pojistenci)
            Vypisovac.vypis_pokracovani()
            pokracovani =input()
        case "3":
            jmeno = zadej_jmeno(rozhrani)
            prijmeni = zadej_prijmeni(rozhrani)
            pojistenec = manager_pojistencu.vyhledej_pojisteneho(jmeno, prijmeni)
            Vypisovac.vypis_pojistence(pojistenec)
            Vypisovac.vypis_pokracovani()
            pokracovani = input()
        case "4":
            jmeno = zadej_jmeno(rozhrani)
            prijmeni = zadej_prijmeni(rozhrani)
            vek = zadej_datum_narozeni(rozhrani)
            manager_pojistencu.vymaz_pojisteneho(jmeno, prijmeni, vek)
            Vypisovac.vypis_vymazani_pojistence()
            Vypisovac.vypis_pokracovani()
            pokracovani = input()
        case "5":
            exit()

    if pokracovani == "":
        main()













