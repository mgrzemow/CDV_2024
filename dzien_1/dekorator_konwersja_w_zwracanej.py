import functools


def do_str(f):
    @functools.wraps(f)
    def nowa_f(*args, **kwargs):
        r = f(*args, **kwargs)
        return str(r)
    return nowa_f

@do_str
def f1(x, y):
    print('jestem f1')
    return x + y

print(repr(f1(2.4, 2.6)))