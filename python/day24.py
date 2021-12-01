from collections import defaultdict


with open("day24.txt") as input_file:
    lines = input_file.readlines()


directions = {
    "e": -2 + 0j,
    "w": +2 + 0j,
    "sr": -1 - 1j,
    "nr": -1 + 1j,
    "sl": +1 - 1j,
    "nl": +1 + 1j,
}

replacements = {"se": "sr", "ne": "nr", "sw": "sl", "nw": "nl"}


def displacement(line: str) -> complex:
    for old, new in replacements.items():
        line = line.replace(old, new)
    return sum(d * line.count(k) for k, d in directions.items())


tiles = defaultdict(bool)
for line in lines:
    tiles[displacement(line)] = not tiles[displacement(line)]

print(sum(tiles.values()))


def expand(grid: defaultdict) -> None:
    for p, tile in list(grid.items()):
        if not tile:
            continue
        for d in directions.values():
            if p + d not in grid:
                grid[p + d] = False


def step(old_grid: defaultdict) -> defaultdict:
    new_grid = old_grid.copy()
    expand(new_grid)
    for p, tile in new_grid.items():
        neigh = sum(old_grid[p + d] for d in directions.values())
        if tile and (neigh == 0 or neigh > 2):
            new_grid[p] = False
        elif (not tile) and (neigh == 2):
            new_grid[p] = True
    return new_grid


for _ in range(100):
    tiles = step(tiles)

print(sum(tiles.values()))
