class Pracownik:
    __slots__ = [
        '_imie',
        'stawka_norm',
        'stawka_nad',
        '_zarobki',
    ]

    def __init__(self, imie, stawka_norm, stawka_nad):
        ...
        # zapisać w self wartości parametrów
        self._imie = imie
        self.stawka_norm = stawka_norm
        self.stawka_nad = stawka_nad
        # licznik zarobków na 0
        self._zarobki = 0

    def pracuj(self, ile_h):
        # wyliczyć zarobki i zwiększyć licznik
        if ile_h < 8:
            self._zarobki += self.stawka_norm * ile_h
        else:
            self._zarobki += self.stawka_norm * 8 + self.stawka_nad * (ile_h - 8)

    def wyplata(self):
        tmp = self._zarobki
        self._zarobki = 0
        return tmp

    def __str__(self):
        return f'{self.__class__.__name__}("{self._imie}")'


class Kierownik(Pracownik):
    # dodatkowa premia, kwota za pracę powyżejh 10h
    __slots__ = [
        'bonus_kier',
    ]

    def __init__(self, imie, stawka_norm, stawka_nad, bonus_kier):
        ...
        # zapisać w self wartości parametrów
        # doczytac o mandatory keywork only parameters
        super().__init__(imie, stawka_norm, stawka_nad)
        self.bonus_kier = bonus_kier

    def pracuj(self, ile_h):
        # wyliczyć zarobki i zwiększyć licznik
        super().pracuj(ile_h)
        if ile_h >= 10:
            self._zarobki += self.bonus_kier


class Dyrektor(Kierownik):
    # dodatkowa premia, kwota za pracę powyżejh 10h
    __slots__ = [
        'bonus_dyr',
    ]

    def __init__(self, imie, stawka_norm, stawka_nad, bonus_kier, bonus_dyr):
        ...
        # zapisać w self wartości parametrów
        # doczytac o mandatory keywork only parameters
        super().__init__(imie, stawka_norm, stawka_nad, bonus_kier)
        self.bonus_dyr = bonus_dyr

    def pracuj(self, ile_h):
        # wyliczyć zarobki i zwiększyć licznik
        super().pracuj(ile_h)
        self._zarobki += self.bonus_dyr


def zatrudnij_zepol(ile_p, ile_k, ile_d):
    lista_p = []
    ...  # dodajemy odpowiednie obiekty do listy, imiona i stawki dowolne
    return lista_p


if __name__ == '__main__':
    zespol = zatrudnij_zepol(10, 2, 1)
    # wszyscy pracują 2, 9, 11 h
    # policzyć sumę wypłat
