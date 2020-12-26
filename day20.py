from collections import defaultdict


with open("day20.txt") as input_file:
    input_tiles = input_file.read().split("\n\n")


def symhash(s: str) -> str:
    if s[::-1] < s:
        return s
    return s[::-1]


sides = defaultdict(list)
for tile in input_tiles:
    lines = tile.splitlines(keepends=False)
    t_id = int(lines[0].split("Tile ")[1].rstrip(":"))
    grid = lines[1:]
    top = grid[0]
    bot = grid[-1]
    flipped = list("".join(l) for l in zip(*grid))
    left = flipped[0]
    right = flipped[-1]
    for s in (top, bot, left, right):
        sides[symhash(s)].append(t_id)

from collections import Counter
import math

c = Counter(l[0] for l in sides.values() if len(l) == 1)
print(math.prod(k for k, v in c.items() if v == 2))
print(Counter(map(len, sides.values())))

# TODO rotate a corner so unique stuff is top-left
# then complete top-left → bot-right