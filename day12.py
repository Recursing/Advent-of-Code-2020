import math

with open("day12.txt") as input_file:
    lines = input_file.readlines()

ship = 0 + 0j
direction = 1
for line in lines:
    letter, *digits = line
    amount = int("".join(digits))
    if letter == "N":
        ship += amount * 1j
    elif letter == "S":
        ship -= amount * 1j
    elif letter == "E":
        ship += amount
    elif letter == "W":
        ship -= amount
    elif letter == "F":
        ship += amount * direction
    elif letter == "R":
        angle = -amount / 180 * math.pi
        direction *= 1j * round(math.sin(angle)) + round(math.cos(angle))
    elif letter == "L":
        angle = amount / 180 * math.pi
        direction *= 1j * round(math.sin(angle)) + round(math.cos(angle))
    else:
        raise ValueError("Wrong letter", letter)

print(abs(ship.real) + abs(ship.imag))

waypoint = 10 + 1j
ship = 0

for line in lines:
    letter, *digits = line
    amount = int("".join(digits))
    if letter == "N":
        waypoint += amount * 1j
    elif letter == "S":
        waypoint -= amount * 1j
    elif letter == "E":
        waypoint += amount
    elif letter == "W":
        waypoint -= amount
    elif letter == "F":
        ship += amount * waypoint
    elif letter == "R":
        angle = -amount / 180 * math.pi
        waypoint *= 1j * round(math.sin(angle)) + round(math.cos(angle))
    elif letter == "L":
        angle = amount / 180 * math.pi
        waypoint *= 1j * round(math.sin(angle)) + round(math.cos(angle))

print(abs(ship.real) + abs(ship.imag))
