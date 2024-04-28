# Zaprojektować tabelę zawierającą:
# - imie
# - nazwisko
# - wzrost (int)
# - waga float(kg)
# - data urodzenia
import random

# Napisać program w pythonie, który tworzy taką tabelę.
import faker

import sqlite3
import datetime as dt
import bazy_rejestracja_conwerterow

sql_select_all = '''
SELECT osoby.*, adresy.*
FROM osoby
LEFT JOIN adresy ON osoby.adres_id=adresy.id;
'''

"""
1. Dodać tabelę z adresami:
 - id
 - ulica
 - nr domu
 - nr lokalu
 - miasto
2. Dodać id_adresu w tabeli osoby
 - adres_id
3. zapimplementować:
 - dodawanie pojedynczego adresu
 - dodawanie wielu adresow - faker
4. Kod globalny, który z tego skorzysta 
"""


def rob_tabele(cur: sqlite3.Cursor):
    sql1 = '''
    CREATE TABLE IF NOT EXISTS adresy (
                    id INTEGER PRIMARY KEY,
                    ulica TEXT,
                    nr_domu TEXT,
                    nr_lokalu TEXT,
                    miasto TEXT
                 )'''

    sql2 = '''
    CREATE TABLE IF NOT EXISTS osoby (
                    id INTEGER PRIMARY KEY,
                    imie TEXT,
                    nazwisko TEXT,
                    wzrost INTEGER,
                    waga REAL,
                    data_urodzenia DATE,
                    adres_id INTEGER,
                    FOREIGN KEY(adres_id) REFERENCES adresy(id)
                 )'''

    cur.execute(sql1)
    cur.execute(sql2)


def generuj_osoby(cur: sqlite3.Cursor,
                  ile: int,
                  adresy_ids: list[int]) -> list[int]:
    f = faker.Faker('pl_PL')
    id_list = []
    # wygenerowal tyle osob ile chceny z losowymi danymi wzietymi z fakera
    for _ in range(ile):
        imie = f.first_name()
        nazwisko = f.last_name()
        waga = f.pyfloat(7, 2, True, 50, 120)
        wzrost = f.pyint(140, 210)
        data_urodzenia = f.date_of_birth(minimum_age=18)
        x = [None]*20 + adresy_ids
        id_list.append(dodaj_osobe(cur, imie, nazwisko, wzrost, waga, data_urodzenia, random.choice(x)))
        # id_list.append(dodaj_osobe(cur, imie, nazwisko, wzrost, waga, data_urodzenia, 9999))
    return id_list


def dodaj_osobe(cur: sqlite3.Cursor,
                imie: str,
                nazwisko: str,
                wzrost: int,
                waga: float,
                data_urodzenia: dt.date,
                adres_id=None):
    sql = f"""
    INSERT INTO osoby (imie, nazwisko, wzrost, waga, data_urodzenia, adres_id)
    VALUES (?, ?, ?, ?, ?, ?);
    """
    cur.execute(sql, (imie, nazwisko, wzrost, waga, data_urodzenia, adres_id))
    return cur.lastrowid


def dodaj_adres(cur: sqlite3.Cursor, ulica: str, nr_domu: str, nr_lokalu: str, miasto: str):
    sql = f"""
    INSERT INTO adresy (ulica, nr_domu, nr_lokalu, miasto)
    VALUES (?, ?, ?, ?);
    """
    cur.execute(sql, (ulica, nr_domu, nr_lokalu, miasto))
    return cur.lastrowid


def generuj_adresy(cur: sqlite3.Cursor, ile: int) -> list[int]:
    f = faker.Faker('pl_PL')
    id_list = []
    # wygenerowal tyle osob ile chceny z losowymi danymi wzietymi z fakera
    for _ in range(ile):
        ulica = f.street_name()
        nr_domu = str(f.pyint(1, 200))
        nr_lokalu = str(f.pyint(1, 200))
        miasto = f.city()
        id_list.append(dodaj_adres(cur, ulica, nr_domu, nr_lokalu, miasto))
    return id_list


def usun_osobe(cur, id):
    sql = '''
    DELETE FROM osoby WHERE id=:id;
    '''
    d = {'id': id}
    cur.execute(sql, d)


def modyfikuj_osobe(cur,
                    id,
                    imie: str | None = None,
                    nazwisko: str | None = None,
                    wzrost: int | None = None,
                    waga: float | None = None,
                    data_urodzenia: dt.date | None = None):
    d = {'imie': imie,
         'nazwisko': nazwisko,
         'wzrost': wzrost,
         'waga': waga,
         'data_urodzenia': data_urodzenia}
    # zostwić tylko pola z niepustą wartością
    d1 = {k: w for k, w in d.items() if w is not None}
    # jak sownik pusty to znaczy że nie ma ani jednej wartości
    if not d1:
        raise ValueError('Należy podać wartość przynajmniej dla jednego pola.')
    # lista fragmentów SET
    set_list = [f'{k} = :{k}' for k, w in d1.items()]
    # cala klauzula SET
    set_c = ', '.join(set_list)
    d1['id'] = id
    sql = f"""
        UPDATE osoby
        SET {set_c}
        WHERE id = :id;    """
    cur.execute(sql, d1)


if __name__ == '__main__':
    with sqlite3.connect(':memory:') as conn:
        conn.execute("PRAGMA foreign_keys = 1")
        cur = conn.cursor()
        rob_tabele(cur)
        adresy_ids = generuj_adresy(cur, 20)
        osoby_ids = generuj_osoby(cur, 20, adresy_ids)
        print('Dodano rekordy', osoby_ids, adresy_ids)
        modyfikuj_osobe(cur, osoby_ids[0], imie='Rafal', wzrost=555)
        usun_osobe(cur, adresy_ids[2])
        cur.execute(sql_select_all)
        # for id, imie, nazwisko, wzrost, waga, data_urodzenia, adres_id in cur:
        #     print(id, imie, nazwisko, wzrost, data_urodzenia, adres_id)
        for r in cur:
            print(r)

        # conn.commit()
