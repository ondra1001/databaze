import pytest

from databaze_pojistencu_app.validace import Kontrolor


@pytest.mark.parametrize(
    ("vstup", "zvaliduj_jmeno_nebo_prijmeni"), [
        (("ondřej"), True),
        (("ondřej!"), False),
        (("0ndřej"), False),
        (("Ondř ej"), False)
    ]
)
def test_zvaliduj_jmeno_nebo_prijmeni(vstup, zvaliduj_jmeno_nebo_prijmeni):
    assert Kontrolor.zvaliduj_jmeno_nebo_prijmeni(vstup) == zvaliduj_jmeno_nebo_prijmeni


@pytest.mark.parametrize(
    ("vstup, zvaliduj_tel_cislo"), [
        (("123456789"), True),
        (("i23456789"), False),
        (("123 456 789"), False),
        (("!23456789"), False)
    ]
)
def test_zvaliduj_tel_cislo(vstup, zvaliduj_tel_cislo):
    assert Kontrolor.zvaliduj_tel_cislo(vstup) == zvaliduj_tel_cislo
