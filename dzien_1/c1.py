# napisać 2 wyrażenia generatorowe:
# 1. Doklejający na początek linii aktualny datetime
# 2. Doklejający na koniec linii napis '<-koniec'

import datetime as dt

with open('tmp.txt') as f:
    # doklejam datetime
    g1 = (f'{dt.datetime.now()} {linia}' for linia in f)
    # doklejam <-koniec
    eol = '\n'
    g2 = (f'{linia.rstrip(eol)} <-koniec\n' for linia in g1)
    for linia in g2:
        print(linia)

# przerobić c1 na funkcje z yield
# dodatkowo dodać parametr - napis doklejany na końcu w drugim generatorze