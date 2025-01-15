class Kontrolor:

    @classmethod
    def zvaliduj_jmeno_nebo_prijmeni(self, jmeno):
        if jmeno.isalpha():
            return True
        return False

    @classmethod
    def zvaliduj_vek(self, vek):
        return True

    @classmethod
    def zvaliduj_tel_cislo(self, tel_cislo):
        if tel_cislo.isnumeric():
            return True
        return False