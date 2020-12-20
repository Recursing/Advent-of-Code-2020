from collections import defaultdict
from itertools import product

with open("day14.txt") as input_file:
    lines = input_file.readlines()


def parse_mask(line):
    bit_str = line.split(" = ")[1]
    and_mask = int(bit_str.replace("X", "1"), 2)
    or_mask = int(bit_str.replace("X", "0"), 2)
    return or_mask, and_mask


assert lines[0].startswith("mask")
or_mask = 0
and_mask = -1
mem = defaultdict(int)
for line in lines:
    if line.startswith("mask"):
        or_mask, and_mask = parse_mask(line)
        continue

    loc, val = line.split(" = ")
    loc = int(loc.split("[")[1].rstrip("]"))
    val = int(val)
    val |= or_mask
    val &= and_mask
    mem[loc] = val
print(sum(mem.values()))


def gen_float_masks(bit_str):
    locations = [i for i, c in enumerate(bit_str) if c == "X"]
    for values in product("01", repeat=len(locations)):
        and_str = list("1" * len(bit_str))
        or_str = list("0" * len(bit_str))
        for l, v in zip(locations, values):
            if v == "1":
                or_str[l] = "1"
            if v == "0":
                and_str[l] = "0"
        and_mask = int("".join(and_str), 2)
        or_mask = int("".join(or_str), 2)
        yield or_mask, and_mask


def parse_mask2(line):
    bit_str = line.split(" = ")[1].strip()
    or_mask = int(bit_str.replace("X", "0"), 2)
    float_masks = list(gen_float_masks(bit_str))
    return or_mask, float_masks


mem = defaultdict(int)
float_masks = []
for line in lines:
    if line.startswith("mask"):
        or_mask, float_masks = parse_mask2(line)
        continue

    loc, val = line.split(" = ")
    loc = int(loc.split("[")[1].rstrip("]"))
    val = int(val)
    loc |= or_mask
    for for_mask, fand_mask in float_masks:
        t_loc = (loc & fand_mask) | for_mask
        mem[t_loc] = val

print(sum(mem.values()))
