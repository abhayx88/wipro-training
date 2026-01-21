# Iterator class
class NumberIterator:
    def __init__(self, n):
        self.n = n
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.n:
            value = self.current
            self.current += 1
            return value
        raise StopIteration


# Generator function
def number_generator(n):
    for i in range(1, n + 1):
        yield i


n = 5

# Iterator
for i in NumberIterator(n):
    print(i)

# Generator
for i in number_generator(n):
    print(i)
