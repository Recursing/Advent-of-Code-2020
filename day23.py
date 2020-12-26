from __future__ import annotations
from typing import Optional

cups = list(map(int, "853192647"))

for _ in range(100):
    lifted = cups[1:4]
    del cups[1:4]
    dest_label = cups[0] - 1
    if dest_label == 0:
        dest_label = 9
    while dest_label not in cups:
        dest_label -= 1
        if dest_label == 0:
            dest_label = 9
    i = cups.index(dest_label)
    cups[i + 1 : i + 1] = lifted
    cups.append(cups.pop(0))

print(cups)


class Node:
    __slots__ = "label", "next"
    label: int
    next: Optional[Node]

    def __init__(self, label: int):
        self.label = label
        self.next = None


cups = list(map(int, "853192647"))

prev = None
index: dict[int, Node] = {}
for c in cups + list(range(max(cups) + 1, 1000001)):
    n = Node(c)
    index[c] = n
    if isinstance(prev, Node):
        prev.next = n
    prev = n

prev.next = index[cups[0]]
cur = prev.next

for _ in range(10_000_000):
    lift_head = cur.next
    cur.next = lift_head.next.next.next
    lifted = (lift_head.label, lift_head.next.label, lift_head.next.next.label)
    dest_label = cur.label - 1
    if dest_label == 0:
        dest_label = 1_000_000
    while dest_label in lifted:
        dest_label -= 1
        if dest_label == 0:
            dest_label = 1_000_000
    ins_after = index[dest_label]
    lift_head.next.next.next = ins_after.next
    ins_after.next = lift_head
    cur = cur.next

print(index[1].next.label * index[1].next.next.label)