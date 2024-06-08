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


p1 = Pracownik('Jan', 30, 60)
p1.pracuj(2)  # naliczy się 2*30 czyli 60
p1.pracuj(10)  # naliczy się 8*30 + 2 * 60 czyli 360
print(p1)  # Pracownik("Jan")
print(p1.wyplata())  # 420
p1._zarobki = 1_000_000
print(p1.wyplata())  # 0
