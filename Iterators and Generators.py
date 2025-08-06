# Iterators


class Counter:
    def __init__(self, max_val):
        self.max = max_val
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.max:
            num = self.current
            self.current += 1
            return num
        else:
            raise StopIteration

counter = Counter(5)
for num in counter:
    print(num)


# Generators


def countdown(n):
    while n > 0:
        yield n
        n -= 1

for num in countdown(3):
    print(num)