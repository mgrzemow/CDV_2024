@do_float
def dodaj(a, b, *args):

    suma = a + b
    for e in args:
        suma = suma + e
    return suma

# napisać dekorator kowertujący parametry a, b, i całą zawartość args do float

print(dodaj('1', '2', '3', '4'))

