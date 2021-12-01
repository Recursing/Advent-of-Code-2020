from collections import deque

# fmt: off
s1 = [18,19,16,11,47,38,6,27,9,22,15,42,3,4,21,41,14,8,23,30,40,13,35,46,50]
s2 = [39,1,29,20,45,43,12,2,37,33,49,32,10,26,36,17,34,44,25,28,24,5,48,31,7]
# fmt: on

p1 = deque(s1)
p2 = deque(s2)
while p1 and p2:
    t1, t2 = p1.popleft(), p2.popleft()
    if t1 > t2:
        p1.append(t1)
        p1.append(t2)
    else:
        p2.append(t2)
        p2.append(t1)


def score(p):
    return sum((i + 1) * v for i, v in enumerate(reversed(p)))


print(score(p1) + score(p2))


def rec_winner(p1: deque, p2: deque) -> bool:
    previous_states = set()
    while p1 and p2:
        h1, h2 = tuple(p1), tuple(p2)
        if (h1, h2) in previous_states:
            return True
        previous_states.add((h1, h2))

        t1, t2 = p1.popleft(), p2.popleft()
        if t1 > len(p1) or t2 > len(p2):
            first_wins = t1 > t2
        else:
            first_wins = rec_winner(deque(tuple(p1)[:t1]), deque(tuple(p2)[:t2]))
        if first_wins:
            p1.append(t1)
            p1.append(t2)
        else:
            p2.append(t2)
            p2.append(t1)
    return bool(p1)


d1, d2 = deque(s1), deque(s2)
rec_winner(d1, d2)
print(score(d1) + score(d2))
