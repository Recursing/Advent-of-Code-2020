def transform(subject: int, loop_size: int) -> int:
    return pow(subject, loop_size, 20201227)


def reverse(subject: int, transformed: int) -> int:
    value = 1
    for loop_size in range(1_000_000_000):
        if value == transformed:
            return loop_size
        value *= subject
        value %= 20201227
    raise ValueError


card_public = 9033205
door_public = 9281649
card_loop_size = reverse(7, card_public)
door_loop_size = reverse(7, door_public)
assert transform(7, card_loop_size) == card_public
assert transform(7, door_loop_size) == door_public
assert transform(card_public, door_loop_size) == transform(door_public, card_loop_size)
print(transform(card_public, door_loop_size))
