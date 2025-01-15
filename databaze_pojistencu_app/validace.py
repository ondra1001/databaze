import re
from datetime import datetime

class Kontrolor:

    @classmethod
    def zvaliduj_jmeno_nebo_prijmeni(self, jmeno):
        if jmeno.isalpha() and len(jmeno) > 1 and len(jmeno) < 15:
            return True
        return False

    @classmethod
    def zvaliduj_datum_narození(self, datum):
        vzorec = r'^(0[1-9]|[12][0-9]|3[01])\.(0[1-9]|1[0-2])\.(19|20)\d{2}$'
        if not re.match(vzorec, datum):
            return False, "Nesprávný formát data (použijte DD.MM.YYYY)"
        try:
            day, month, year = map(int, datum.split('.'))
            datetime(year, month, day)
        
            current_year = datetime.now().year
            if year > current_year:
                return False
            if year < current_year - 150:
                return False
            return True
        
        except ValueError:
            return False

    @classmethod
    def zvaliduj_tel_cislo(self, tel_cislo):
        vzorec = r'^(\+420|420)?\s*[0-9]{3}\s*[0-9]{3}\s*[0-9]{3}$'
        return bool(re.match(vzorec, tel_cislo))