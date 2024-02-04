# napisać 2 wyrażenia generatorowe:
# 1. Doklejający na początek linii aktualny datetime
# 2. Doklejający na koniec linii napis '<-koniec'

import datetime as dt

def doklej_datetime(g):
    for linia in g:
        yield f'{dt.datetime.now()} {linia}'

def doklej_str(g, *, napis):
    eol = '\n'
    for linia in g:
        yield f'{linia.rstrip(eol)} {napis}\n'

with open('tmp.txt') as f:
    # doklejam datetime
    g1 = doklej_datetime(f)
    # doklejam <-koniec
    g2 = doklej_str(g1, napis='<= koniec')
    for linia in g2:
        print(linia)

# przerobić c1 na funkcje z yield
# dodatkowo dodać parametr - napis doklejany na końcu w drugim generatorze