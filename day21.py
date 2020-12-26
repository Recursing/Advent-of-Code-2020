with open("day21.txt") as input_file:
    lines = input_file.readlines()


def parse_line(s: str) -> tuple[list[str], list[str]]:
    ingredients, allergens = s.split(" (contains ")
    return ingredients.split(), allergens.rstrip(")\n").split(", ")


foods = [parse_line(l) for l in lines]

import z3
from functools import cache

ings = set(i for f in foods for i in f[0])
ig_nums = {s: i for i, s in enumerate(ings)}
nums_ig = {i: s for s, i in ig_nums.items()}
s = z3.Solver()


@cache
def allergen_var(s):
    all_allergens.append(z3.Int(s))
    return all_allergens[-1]


all_allergens = []

for ingredients, allergens in foods:
    for al in allergens:
        s.add(z3.Or(*[allergen_var(al) == ig_nums[i] for i in ingredients]))

s.add(z3.Distinct(all_allergens))
s.check()
model = s.model()


s.add(z3.Or(*[allergen != model[allergen] for allergen in all_allergens]))
assert s.check() == z3.unsat, "multiple solutions"


ings_with_allergen = {}
for allergen in all_allergens:
    ings_with_allergen[nums_ig[model[allergen].as_long()]] = str(allergen)

print(sum(i not in ings_with_allergen for ingredients, _ in foods for i in ingredients))

print(",".join(sorted(ings_with_allergen, key=ings_with_allergen.get)))