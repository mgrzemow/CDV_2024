import functools


def do_float(f):
    @functools.wraps(f)
    def nowa_f(*args, **kwargs):
        r = f(*(float(a) for a in args), **kwargs)
        return r

    return nowa_f
@do_float
def dodaj(a, b, *args):

    suma = a + b
    for e in args:
        suma = suma + e
    return suma

# napisać dekorator kowertujący parametry a, b, i całą zawartość args do float

print(dodaj('1', '2', '3', '4'))

