from functools import lru_cache

with open("day11.txt") as input_file:
    lines = input_file.readlines()

grid = tuple(l.strip() for l in lines)


@lru_cache(maxsize=None)
def neighbours1(r, c):
    height = len(grid)
    width = len(grid[0])
    l = []
    for dr in (-1, 0, 1):
        for dc in (-1, 0, 1):
            if dr == dc == 0:
                continue
            nr = r + dr
            nc = c + dc
            if 0 <= nr < height and 0 <= nc < width:
                l.append((nr, nc))
    return l


def rule1(grid, r, c):
    if grid[r][c] == ".":
        return "."
    occupied = sum(grid[nr][nc] == "#" for nr, nc in neighbours1(r, c))
    if grid[r][c] == "L" and occupied == 0:
        return "#"
    if grid[r][c] == "#" and occupied >= 4:
        return "L"
    return grid[r][c]


def step(grid, rule):
    newgrid = [list(r) for r in grid]
    for r, row in enumerate(grid):
        for c, _cell in enumerate(row):
            newgrid[r][c] = rule(grid, r, c)
    return tuple("".join(l) for l in newgrid)


def neighbours2(grid, r, c):
    height = len(grid)
    width = len(grid[0])
    l = []
    for dr in (-1, 0, 1):
        for dc in (-1, 0, 1):
            if dr == dc == 0:
                continue
            nr, nc = r, c
            while True:
                nr += dr
                nc += dc
                if not (0 <= nr < height and 0 <= nc < width):
                    break
                if grid[nr][nc] != ".":
                    l.append((nr, nc))
                    break
    return l


def rule2(grid, r, c):
    if grid[r][c] == ".":
        return "."
    occupied = sum(grid[nr][nc] == "#" for nr, nc in neighbours2(grid, r, c))
    if grid[r][c] == "L" and occupied == 0:
        return "#"
    if grid[r][c] == "#" and occupied >= 5:
        return "L"
    return grid[r][c]


for rule in (rule1, rule2):
    current_grid = grid
    for i in range(1_000_000):
        next_grid = step(current_grid, rule)
        if next_grid == current_grid:
            print(sum(l.count("#") for l in current_grid))
            break
        current_grid = next_grid