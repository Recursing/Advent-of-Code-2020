from collections import defaultdict

with open("day9.txt") as input_file:
    lines = input_file.readlines()

numbers = [int(l) for l in lines]

valids = defaultdict(int)
part1 = 0
for i, n in enumerate(numbers):
    if i >= 25 and not valids[n]:
        part1 = n
        break
    window_start = max(i - 24, 0)
    old_n = numbers[i - 25]
    for previous in numbers[window_start:i]:
        valids[previous + n] += 1
        if i >= 25:
            valids[previous + old_n] -= 1

print(part1)

for i, n in enumerate(numbers):
    s = n
    for j in range(i + 1, len(numbers)):
        s += numbers[j]
        if s == part1:
            mi = min(numbers[i : j + 1])
            ma = max(numbers[i : j + 1])
            print(mi + ma)
            break
        if s > part1:
            break
