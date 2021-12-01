with open("day8.txt") as input_file:
    lines = input_file.readlines()


def terminates(lines) -> tuple[bool, int]:
    ic = 0
    acc = 0
    seen = set()
    while True:
        seen.add(ic)
        instruction, arg = lines[ic].split()
        argn = int(arg)
        if instruction == "jmp":
            ic += argn
        elif instruction == "acc":
            acc += argn
            ic += 1
        else:
            assert instruction == "nop"
            ic += 1
        if ic in seen:
            return False, acc
        if ic == len(lines):
            return True, acc
        if ic > len(lines):
            return False, acc


print(terminates(lines))


for i, line in enumerate(lines):
    if "jmp" in line:
        orig, rep = "jmp", "nop"
    elif "nop" in line:
        orig, rep = "nop", "jmp"
    else:
        continue
    lines[i] = lines[i].replace(orig, rep)
    t, r = terminates(lines)
    if t:
        print(r)
        break
    lines[i] = lines[i].replace(rep, orig)
