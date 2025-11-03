# Problem 2: Custom Range Iterator (Iterators - Beginner)
class CustomRange:
    def __init__(self, start, stop=None, step=1):
        if stop is None:
            self.start = 0
            self.stop = start
        else:
            self.start = start
            self.stop = stop
        self.step = step
        self.current = self.start

    def __iter__(self):
        self.current = self.start
        return self

    def __next__(self):
        if (self.step > 0 and self.current >= self.stop) or (self.step < 0 and self.current <= self.stop):
            raise StopIteration
        else:
            value = self.current
            self.current += self.step
            return value

    def reset(self):
        self.current = self.start
class EvenNumbers:
    def __init__(self, start, stop):
        self.start = start 
        self.stop = stop
        self.current = self.start

    def __iter__(self):
        self.current = self.start
        return self

    def __next__(self):
        if self.current >= self.stop:
            raise StopIteration
        else:
            if self.current % 2 != 0 : self.current += 1
            value = self.current
            self.current += 2
            return value

# Basic usage
print("Custom Range 0 to 10:")
for num in CustomRange(10):
    print(num, end=" ")
# Output: 0 1 2 3 4 5 6 7 8 9
print("\n\nCustom Range 5 to 15, step 2:")
for num in CustomRange(5, 15, 2):
    print(num, end=" ")
# Output: 5 7 9 11 13
print("\n\nCustom Range 10 to 0, step -2:")
for num in CustomRange(10, 0, -2):
    print(num, end=" ")
# Output: 10 8 6 4 2
print("\n\nFloat step - 0 to 2, step 0.5:")
for num in CustomRange(0, 2, 0.5):
    print(num, end=" ")
# Output: 0 0.5 1.0 1.5
print("\n\nEven Numbers 1 to 20:")
for num in EvenNumbers(1, 20):
    print(num, end=" ")
# Output: 2 4 6 8 10 12 14 16 18
# Test reset
print("\n\nTest Reset:")
my_range = CustomRange(3)
for num in my_range:
    print(num, end=" ")
print()
my_range.reset()
for num in my_range:
    print(num, end=" ")
# Output: 0 1 2
# 0 1 2