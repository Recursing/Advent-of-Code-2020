groups = open("day5.txt").read().split("\n\n")
print(sum(len(set(group) - {"\n", " "}) for group in groups))
print(sum(len(set.intersection(*map(set, group.splitlines()))) for group in groups))
