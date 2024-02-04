import functools


def parametry_do_float(f):
    @functools.wraps(f)
    def nowa_f(*args, **kwargs):
        try:
            args = [float(i) for i in args]
        except ValueError:
            raise ValueError('Parametry wejściowe muszą być konwertowalne do float')
        r = f(*args, **kwargs)
        return r
    return nowa_f

@parametry_do_float
def f1(x, y):
    print('jestem f1')
    return x + y

print(f1('2.4', '2.6'))