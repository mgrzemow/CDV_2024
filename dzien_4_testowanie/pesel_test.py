import json
from pprint import pprint

import pytest
import zipfile
from pesel import generuj_pesel
import random
import os

dane = [((29, 6, 2047, 308, False), '47262930801'),
        ((1, 4, 2053, 186, True), '53240118611'),
        ((9, 5, 1982, 599, False), '82050959907'),
        ((2, 8, 2064, 65, True), '64280206514'),
        ((15, 6, 1921, 874, False), '21061587404'),
        ((7, 12, 2092, 154, False), '92320715403'),
        ((20, 9, 2087, 260, False), '87292026006'),
        ((21, 6, 1935, 572, False), '35062157201'),
        ((18, 1, 1906, 366, True), '06011836612'),
        ((7, 8, 1982, 350, False), '82080735003')] * 100


# fixture, który ręcznie:
# 1. Przygotowuje dane do testów
# 2. Zwraca dane yield
# 3. Czyści po testach
@pytest.fixture(scope='session')
def dane_f():
    # rozpakować plik do pliku dane.json
    # wczytać z pliku dane
    print('\nrozpakowuję dane')
    with zipfile.ZipFile('dane.zip', 'r') as f:
        f.extractall()
    with open('dane.json') as f:
        dane = json.load(f)
    yield dane
    # skasować plik json
    print('\nkasuję dane')
    os.remove('dane.json')


@pytest.fixture(scope='session')
def zip_dir(tmp_path_factory):
    tmp = tmp_path_factory.mktemp('tmp')
    yield tmp


@pytest.fixture(scope='session')
def unzip_f(zip_dir):
    with zipfile.ZipFile('dane.zip', 'r') as f:
        f.extractall(zip_dir)
    yield zip_dir / 'dane.json'


# fixture, który ręcznie:
# 1. Przygotowuje dane do testów korzystając z wbudowanego katalogu tymczasowego
# 2. Zwraca dane yield
# 3. pytest sam czyści po testach
@pytest.fixture(scope='session')
def dane_f_tmp_dir_factory(unzip_f):
    with open(unzip_f) as f:
        dane = json.load(f)
    yield dane


def test_bacics():
    for _ in range(100_000):
        dzien = random.randint(1, 31)
        miesiac = random.randint(1, 12)
        rok = random.randint(1901, 2099)
        nr = random.randint(0, 999)
        plec_facet = bool(random.randint(0, 1))

        pesel = generuj_pesel(dzien, miesiac, rok, nr, plec_facet)
        assert type(pesel) is str
        assert len(pesel) == 11
        assert pesel.isdigit()
        assert pesel.isdigit()
        assert pesel[-2] in '01'
        assert 1 <= int(pesel[2:4]) <= 32
        assert 1 <= int(pesel[4:6]) <= 31


def test_sum():
    for _ in range(100_000):
        dzien = random.randint(1, 31)
        miesiac = random.randint(1, 12)
        rok = random.randint(1901, 2099)
        nr = random.randint(0, 999)
        plec_facet = bool(random.randint(0, 1))

        pesel = generuj_pesel(dzien, miesiac, rok, nr, plec_facet)
        assert str(sum(int(d) for d in pesel[:-1]))[-1] == pesel[-1]


def test_plus_20():
    for _ in range(100_000):
        dzien = random.randint(1, 31)
        miesiac = random.randint(1, 12)
        rok = random.randint(1901, 2099)
        nr = random.randint(0, 999)
        plec_facet = bool(random.randint(0, 1))
        pesel = generuj_pesel(dzien, miesiac, rok, nr, plec_facet)
        if rok >= 2000:
            assert 21 <= int(pesel[2:4]) <= 32


# @pytest.mark.parametrize('wejscie, pesel', dane)
# def test_dane_parametrize(wejscie, pesel):
#     assert generuj_pesel(*wejscie) == pesel


def test_dane_fixture_1(dane_f_tmp_dir_factory):
    for wejscie, pesel in dane_f_tmp_dir_factory:
        assert generuj_pesel(*wejscie) == pesel


def test_dane_fixture_2(dane_f_tmp_dir_factory):
    for wejscie, pesel in dane_f_tmp_dir_factory:
        assert generuj_pesel(*wejscie) == pesel


def test_exceptions():
    dane_value_error = [(12, 12, 1999, 11, '1'),
                        ('12', 12, 1999, 11, 1),
                        (12, '12', 1999, 11, 1),
                        (12, 12, '1999', 11, True),
                        (12, 12, 1999, '11', True),
                        (12.2, 12, 1999, 11, True),
                        (12, 12.5, 1999, 11, True),
                        (12, 12, 1999.5, 11, True),
                        (12, 12, 1999, 11.5, True),
                        ]
    for dane in dane_value_error:
        with pytest.raises(ValueError):
            generuj_pesel(*dane)


def testuj_float():
    dane_float = [((12.0, 12, 1999, 11, True), (12, 12, 1999, 11, True)),
                  ((12, 12.0, 1999, 11, True), (12, 12, 1999, 11, True)),
                  ((12, 12, 1999.0, 11, True), (12, 12, 1999, 11, True)),
                  ((12, 12, 1999, 11.0, True), (12, 12, 1999, 11, True)),
                  ]
    for dane1, dane2 in dane_float:
        assert generuj_pesel(*dane1) == generuj_pesel(*dane2)

# if __name__ == '__main__':
#     wynik = []
#     for _ in range(10):
#         dzien = random.randint(1, 31)
#         miesiac = random.randint(1, 12)
#         rok = random.randint(1901, 2099)
#         nr = random.randint(0, 999)
#         plec_facet = bool(random.randint(0, 1))
#         pesel = generuj_pesel(dzien, miesiac, rok, nr, plec_facet)
#         wynik.append(((dzien, miesiac, rok, nr, plec_facet), pesel))
#     pprint(wynik)
#     with open('dane.json', 'wt', encoding='utf8') as f:
#         json.dump(wynik, f)
