import functools


def dekorator(f):
    @functools.wraps(f)
    def nowa_f(*args, **kwargs):
        print(f'Wywołuję funkcję {f.__name__} z parametrami {args=}, {kwargs=}')
        r = f(*args, **kwargs)
        print(f'Funkcja {f.__name__} zwróciła {r}')
        return r

    return nowa_f


@dekorator
def f1(x, y):
    print('jestem f1')
    return x + y


f1(1, 4)
print(f1)