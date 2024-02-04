def f1(n):
    while n > 0:
        yield n
        n -= 1

for i in f1(5):
    print(i)