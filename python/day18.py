import operator
import math

with open("day18.txt") as input_file:
    lines = input_file.readlines()

ops = {"+": operator.add, "*": operator.mul}


def eval(line: str) -> int:
    line = line.strip().replace(" ", "")
    stack = [[0, ops["+"]]]
    for c in line:
        if c == "(":
            stack.append([0, ops["+"]])
        elif c == ")":
            t = stack.pop()[0]
            a, op = stack[-1]
            stack[-1] = [op(a, t), None]
        elif c in "+*":
            stack[-1][1] = ops[c]
        else:
            assert "0" <= c <= "9"
            n = int(c)
            p, op = stack[-1]
            stack[-1] = [op(p, n), None]
    assert len(stack) == 1
    return stack[0][0]


print(sum(map(eval, lines)))


def eval2_no_parens(line: str) -> int:
    mults = line.split("*")
    return math.prod(sum(map(int, term.split("+"))) for term in mults)


import re

parens_pattern = re.compile(r"\(([^()]+)\)")


def eval2(line: str) -> int:
    line = line.strip().replace(" ", "")
    while subs := parens_pattern.findall(line):
        for sub in subs:
            line = line.replace(f"({sub})", str(eval2_no_parens(sub)))
    return eval2_no_parens(line)


print(sum(map(eval2, lines)))
