import re

inputs = "i".split("\n\n")
parsed = [i.split() for i in inputs]
fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
parsed = [{v.split(":")[0]: v.split(":")[1] for v in p} for p in parsed]
sum(all(f in p for f in fields) for p in parsed)


def int_val(mi, ma):
    def val(s):
        try:
            i = int(s)
            return mi <= i <= ma
        except ValueError:
            return False

    return val


def hgt_val(s):
    if s[-2:] == "cm":
        return int_val(150, 193)(s[:-2])
    if s[-2:] == "in":
        return int_val(59, 76)(s[:-2])
    return False


def re_val(r):
    p = re.compile(r)

    def val(s):
        return p.fullmatch(s)

    return val


rules = {
    "byr": int_val(1920, 2002),
    "iyr": int_val(2010, 2020),
    "eyr": int_val(2020, 2030),
    "hgt": hgt_val,
    "hcl": re_val(r"#[0-9a-f]{6}"),
    "pid": re_val(r"\d{9}"),
    "ecl": (lambda s: s in "amb blu brn gry grn hzl oth".split()),
    "cid": (lambda s: True),
}
print(
    sum(
        all(rules[k](v) for k, v in p.items())
        for p in parsed
        if all(f in p for f in fields)
    )
)
