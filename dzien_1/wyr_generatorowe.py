# x1 = range(10_000_000)
# input('stop')
# x2 = (i ** 2 for i in x1)
# input('stop')
# x3 = (i / 13 for i in x2)
# input('stop')
# for i in x3:
#     print(i)
#     if i > 100:
#         break

x = [11, 13, 15, 17, 'ala']
x1 = [i % 2 for i in x if i is int]
x2 = [i == 1 for i in x1]
print(x2)
print(all(x2))
print(any(x2))

print(all(i % 2 == 1 for i in x if i is int))
print(any(i % 2 == 1 for i in x if i is int))

x = ['Ala', 'stół', 'Ola', 'Zosia', 'dach']
# sprawdzić czy:
# - spośród słów zaczynających się od wielkiej litery, wszystkie kończą się na 'a'
# - spośród słów zaczynających się od wielkiej litery, którekolwiek kończy się na 'a'
print(all(slowo.endswith('a') for slowo in x if slowo[0].isupper()))
print(any(slowo.endswith('a') for slowo in x if slowo[0].isupper()))
