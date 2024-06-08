class Pracownik:
    def __init__(self, imie, stawka_norm, stawka_nad):
        ...

    def pracuj(self, ile_h):
        ...

    def wyplata(self):
        ...
    def __str__(self):
        ...


p1 = Pracownik('Jan', 30, 60)
p1.pracuj(2) # naliczy się 2*30 czyli 60
p1.pracuj(10)# naliczy się 8*30 + 2 * 60 czyli 360
print(p1) # Pracownik("Jan")
print(p1.wyplata()) # 420
print(p1.wyplata()) # 0
