class GlupiGenerator:

    def __init__(self):
        self.counter = 5

    def __iter__(self):
        return self

    def __next__(self):
        while self.counter:
            self.counter -= 1
            return self.counter
        else:
            raise StopIteration

g = GlupiGenerator()
for e in g:
    print(e)
print('koniec')