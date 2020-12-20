with open("day13.txt") as input_file:
    lines = input_file.readlines()

earliest = int(lines[0])

ids = lines[1].strip().split(",")
numids = [int(i) for i in ids if i != "x"]
print(min((i - (earliest % i), (i - (earliest % i)) * i) for i in numids))

constraints = [
    (int(num), (int(num) - delta)) for delta, num in enumerate(ids) if num != "x"
]

from sympy.ntheory.modular import crt

multipliers, remainders = zip(*constraints)
print(crt(multipliers, remainders))
