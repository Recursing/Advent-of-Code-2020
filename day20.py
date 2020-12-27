from collections import defaultdict


with open("day20.txt") as input_file:
    input_tiles = input_file.read().split("\n\n")


def symhash(s: str) -> str:
    if s[::-1] < s:
        return s
    return s[::-1]


sides = defaultdict(list)
tiles = {}
for tile in input_tiles:
    lines = tile.splitlines(keepends=False)
    t_id = int(lines[0].split("Tile ")[1].rstrip(":"))
    grid = lines[1:]
    top = grid[0]
    bot = grid[-1]
    rotated = list("".join(l) for l in zip(*grid))
    left = rotated[0]
    right = rotated[-1]
    for s in (top, bot, left, right):
        sides[symhash(s)].append(t_id)
    tiles[t_id] = grid

from collections import Counter
import math

c = Counter(l[0] for l in sides.values() if len(l) == 1)
print(math.prod(k for k, v in c.items() if v == 2))

# Rotate a corner so unique stuff is top-left
# then complete top-left → bot-right
# ugliest code I've written but it works

# Random corner
corner_id = next(k for k, v in c.items() if v == 2)
top_left = tiles.pop(corner_id)


# Flip so unique sides are top left
if len(sides[symhash(top_left[0])]) > 1:
    top_left = top_left[::-1]
assert len(sides[symhash(top_left[0])]) == 1
left = "".join(l[0] for l in top_left)
if len(sides[symhash(left)]) > 1:
    top_left = [l[::-1] for l in top_left]
left = "".join(l[0] for l in top_left)
assert len(sides[symhash(left)]) == 1

matrix = [[] for _ in range(12)]


def transformations(tile):
    for _ in range(4):
        yield tile
        yield tile[::-1]
        yield [l[::-1] for l in tile]
        tile = list("".join(l) for l in zip(*tile[::-1]))


from itertools import product

for x, y in product(range(12), repeat=2):
    assert len(matrix[y]) == x
    if x == y == 0:
        matrix[y].append(top_left)
    elif y == 0:
        left_tile = matrix[y][x - 1]
        left_side = "".join(l[-1] for l in left_tile)
        (new_tile_id,) = [i for i in sides[symhash(left_side)] if i in tiles]
        new_tile = tiles.pop(new_tile_id)
        for new_tile in transformations(new_tile):
            if "".join(l[0] for l in new_tile) == left_side:
                matrix[y].append(new_tile)
                break
    else:
        above_tile = matrix[y - 1][x]
        first_row = above_tile[-1]
        (new_tile_id,) = [i for i in sides[symhash(first_row)] if i in tiles]
        new_tile = tiles.pop(new_tile_id)
        for new_tile in transformations(new_tile):
            if new_tile[0] == first_row:
                matrix[y].append(new_tile)
                break

assert len(tiles) == 0
for x, y in product(range(12), repeat=2):
    tile = matrix[y][x]
    tile = [r[1:-1] for r in tile[1:-1]]
    matrix[y][x] = tile


picture = [["" for _ in range(12 * 8)] for _ in range(12 * 8)]
for y, x in product(range(12 * 8), repeat=2):
    tile = matrix[y // 8][x // 8]
    picture[y][x] = tile[y % 8][x % 8]

pattern = [
    "                  # ",  #
    "#    ##    ##    ###",
    " #  #  #  #  #  #   ",
]
coords = [
    (r, c) for r, row in enumerate(pattern) for c, cell in enumerate(row) if cell == "#"
]


for picture in transformations(picture):
    picture = [list(r) for r in picture]
    for start_y, start_x in product(range(12 * 8 - 3), range(12 * 8 - 20)):
        if all(picture[start_y + cy][start_x + cx] == "#" for cy, cx in coords):
            for (cy, cx) in coords:
                picture[start_y + cy][start_x + cx] = "O"
    print(sum(cell == "#" for row in picture for cell in row))
