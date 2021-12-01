from functools import cache

with open("day19.txt") as input_file:
    rules, lines = input_file.read().split("\n\n")

rules = rules.splitlines(keepends=False)
lines = lines.splitlines(keepends=False)

parsed_rules = {}
for rule in rules:
    num, stuff = rule.split(": ")
    num = int(num)
    if stuff in ('"a"', '"b"'):
        parsed_rules[num] = stuff[1]
    else:
        parsed_rules[num] = [[int(d) for d in o.split()] for o in stuff.split(" | ")]


import sys

sys.setrecursionlimit(100000)

depth = 0
maxdepth = max(map(len, lines))


@cache
def expand_rule(n: int) -> str:
    global depth
    if depth > maxdepth:
        depth -= 1
        return ""
    options = parsed_rules[n]
    if isinstance(options, str):
        depth -= 1
        return options
    depth += 1
    r = "|".join("".join(map(expand_rule, o)) for o in options)
    depth -= 1
    return f"({r})"


import re

pattern = re.compile(expand_rule(0))
print(pattern)
print(sum(bool(pattern.fullmatch(l)) for l in lines))

parsed_rules[8] = [[42], [42, 8]]
parsed_rules[11] = [[42, 31], [42, 11, 31]]
expand_rule.cache_clear()
pattern = re.compile(expand_rule(0))
print(pattern)
print(sum(bool(pattern.fullmatch(l)) for l in lines))
