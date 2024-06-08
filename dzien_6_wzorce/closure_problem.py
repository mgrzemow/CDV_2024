def f0(i, x=[]):
    x.append(i)
    print(x)


f0(1)
f0(2)
f0(3)


def f1():
    lista_f = []
    for i in range(3):
        def f2(i=i):
            print('f2', i)

        lista_f.append(f2)
    return lista_f


lf = f1()
for f in lf:
    f()
