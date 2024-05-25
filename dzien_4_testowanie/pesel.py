"""
Ćwiczenie:

Napisać program, który:

1. Na podstawie:
 - roku urodenia,
 - miesiąca urodzenia
 - dnia urodzenia
 - nr kolejnego
 - określenia płci True == mężczyzna

wygeneruje pesel w następującego schematu:
 - 2 ostatnie cyfry roku
 - 2 cyfrowy miesiąc uzupełniony od lewej zerem (jeżeli rok >= 2000 to do miesiąca dodajemy 20)
 - 2 cyfrowy dzień uzupełniony od lewej zerem
 - 3 cyfrowy nr kolejny uzupełniony od lewej zerem
 - cyfra płci - 1 mężczyzna, 0 kobieta
 - suma kontrolna będąca ostatnią cyfrą sumy powyższych cyfr

Np dla kobiety urodzonej 3.12.2005r jako 13ta osoba powinno wyjść:
05320301307

Podpowiedzi:
 - pętla for dla napisów iteruje po literach
 - str(12)
 - int('12')
 - '2'.zfill(3)

Rozszerzenia ćwiczenia:
 - czy da się uniknąć użycia zfill (formatowanie fstringów)

Wymagania do funkcji:
- w razie błędów wywala wyjątek ValueError
- poprawne dane numeryczne to int, float ale tylko okrągłe
- sprawdzamy zakresy wartości dla dzien, miesiac, nr_kolejny
- zwraca 11 znakowy string
"""


def generuj_pesel(dzien: float, miesiac: float, rok: float, nr: float, plec_facet: bool) -> str:
    if type(dzien) not in [float, int]:
        raise ValueError('Dzien powinien być int lub float')
    if type(miesiac) not in [float, int]:
        raise ValueError('Miesiac powinien być int lub float')
    if type(rok) not in [float, int]:
        raise ValueError('Rok powinien być int lub float')
    if type(nr) not in [float, int]:
        raise ValueError('nr powinien być int lub float')
    if type(plec_facet) is not bool:
        raise ValueError('Plec_facet powinien być bool')

    if int(dzien) != dzien:
        raise ValueError('Wartość dnia powinna być okrągła')
    if int(miesiac) != miesiac:
        raise ValueError('Wartość miesiaca powinna być okrągła')
    if int(rok) != rok:
        raise ValueError('Wartość roku powinna być okrągła')
    if int(nr) != nr:
        raise ValueError('Wartość nr powinna być okrągła')
    dzien, miesiac, rok, nr = int(dzien), int(miesiac), int(rok), int(nr)

    pesel = f'{str(rok)[2:]}{miesiac + 20 if rok >= 2000 else miesiac:02d}{dzien:02d}{nr:03d}{int(plec_facet)}'
    pesel += str(sum(int(d) for d in pesel))[-1]
    return pesel
