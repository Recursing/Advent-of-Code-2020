from dataclasses import dataclass
from graphlib import TopologicalSorter

with open("day7.txt") as input_file:
    lines = input_file.readlines()

@dataclass
class Requirement:
    name: str
    dependencies: list[tuple[int, str]]

def parsed(line: str) -> Requirement:
    name, rest = line.split(" contain ")
    name = name.strip().rstrip("s.")
    deps = rest.split(",")
    def parse_dep(a: str) -> tuple[int, str]:
        amount, nm = a.split(None, 1)
        return (int(amount), nm.strip().rstrip("s."))
    return Requirement(name, [parse_dep(d) for d in deps if d != "no other bags.\n"])

g = {}
g2 = {}
for line in lines:
    r = parsed(line)
    g[r.name] = {n for d,n in r.dependencies}
    g2[r.name] = r.dependencies

sorter = TopologicalSorter(graph=g)

sorted_bags = tuple(sorter.static_order())


options = set()
for bag in sorted_bags:
    if any("shiny gold" in v for v in g[bag]):
        options.add(bag)
    if g[bag] & options:
        options.add(bag)
print(len(options))

costs = {}
for bag in sorted_bags:
    costs[bag] = 1
    for amount, name in g2[bag]:
        costs[bag] += amount * costs[name]

print(costs["shiny gold bag"] - 1)