from operator import and_
from functools import reduce

groups = open("day5.txt").read().split("\n\n")
print(sum(len(set(group) - {"\n", " "}) for group in groups))
print(
    sum(len(reduce(and_, map(set, group.splitlines()), set(group))) for group in groups)
)
