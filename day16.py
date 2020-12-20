from itertools import chain

with open("day16.txt") as input_file:
    sections = input_file.read().split("\n\n")
sections = [s.splitlines() for s in sections]
fields, my_ticket, nearby_tickets = sections
my_ticket = [int(f) for f in my_ticket[1].split(",")]
del nearby_tickets[0]
nearby_tickets = [[int(f) for f in l.split(",")] for l in nearby_tickets]
ranges = [
    range(int(a), int(b))
    for s in chain(*[s.split(": ")[1].split(" or ") for s in fields])
    for a, b in [s.split("-")]
]
print(sum(n for n in chain(*nearby_tickets) if not any(n in r for r in ranges)))

valid_tickets = [
    ticket
    for ticket in nearby_tickets
    if all(any(f in r for r in ranges) for f in ticket)
]

assert all(any(f in r for r in ranges) for f in my_ticket)

range_fields = {}
field_names = {}
for i, field in enumerate(fields):
    name, ranges_str = field.split(": ")
    ranges = ranges_str.split(" or ")
    for r in ranges:
        a, b = map(int, r.split("-"))
        range_fields[range(a, b + 1)] = i
    field_names[i] = name


def possibilities(ticket: list[int]) -> list[set[int]]:
    res = [set() for _ in ticket]
    for i, field in enumerate(ticket):
        for r, field_num in range_fields.items():
            if field in r:
                res[i].add(field_num)
    return res


valid_tickets.append(my_ticket)
import z3

grid = [
    [z3.Int(f"ticket_{t}_{f}") for f, _ in enumerate(ticket)]
    for t, ticket in enumerate(valid_tickets)
]


solver = z3.Solver()
for row in grid:
    solver.add(z3.Distinct(*row))

for column in zip(*grid):
    first = column[0]
    cond = z3.And(*[other == first for other in column[1:]])
    solver.add(cond)


for t, ticket in enumerate(valid_tickets):
    for p, pos in enumerate(possibilities(ticket)):
        cond = z3.Or(*[grid[t][p] == v for v in pos])
        solver.add(cond)

print("solving...")
print(solver.check())
m = solver.model()
indexes = [m[cell].as_long() for cell in grid[0]]
from math import prod

print(
    prod(
        n
        for i, n in enumerate(my_ticket)
        if field_names[indexes[i]].startswith("departure")
    )
)
