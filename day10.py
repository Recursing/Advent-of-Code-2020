from collections import Counter
from functools import cache

with open("day10.txt") as input_file:
    lines = input_file.readlines()

numbers = [0] + sorted(map(int, lines))
numbers.append(max(numbers) + 3)
c = Counter(n - p for p, n in zip(numbers, numbers[1:]))
print(c[1] * c[3])


@cache
def arrangements(n):
    if n not in numbers:
        return 0
    if n == 0:
        return 1
    return arrangements(n - 1) + arrangements(n - 2) + arrangements(n - 3)


print(arrangements(numbers[-1]))
