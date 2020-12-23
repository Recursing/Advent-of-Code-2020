from itertools import product
from collections import defaultdict
from typing import Iterator

with open("day17.txt") as input_file:
    lines = input_file.readlines()


def neighbours(x: int, y: int, z: int) -> Iterator[tuple[int, int, int]]:
    for dx, dy, dz in product((-1, 0, 1), repeat=3):
        if dx == dy == dz == 0:
            continue
        yield x + dx, y + dy, z + dz


Coordinate = tuple[int, int, int]
Grid = defaultdict[Coordinate, bool]


def step(old_grid: Grid, step_num: int) -> Grid:
    new_grid = defaultdict(bool)
    max_x = step_num + 4
    max_z = step_num
    for x in range(-max_x, max_x):
        for y in range(-max_x, max_x):
            for z in range(-max_z, max_z + 1):
                neighs = neighbours(x, y, z)
                n_active = sum(old_grid[c] for c in neighs)
                new_grid[(x, y, z)] = n_active == 3 or (
                    old_grid[(x, y, z)] and n_active == 2
                )
    return new_grid


grid = defaultdict(bool)
for y, line in enumerate(lines):
    for x, cell in enumerate(line):
        grid[(x - 4, y - 4, 0)] = cell == "#"

for step_num in range(1, 7):
    grid = step(grid, step_num)
    print(step_num, sum(grid.values()))