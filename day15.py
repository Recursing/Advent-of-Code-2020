start = [0, 8, 15, 2, 12, 1]
history = {n: i for i, n in enumerate(start)}
last_index = len(start)
last_spoken = 4
while last_index < 30000000-1:
    spoken = last_index - history.get(last_spoken, last_index)
    history[last_spoken] = last_index
    last_spoken = spoken
    last_index += 1
print(last_spoken)

