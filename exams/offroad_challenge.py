from collections import deque

fuel = deque([int(x) for x in input().split()])
consumption_index = deque([int(x) for x in input().split()])
quantities_needed = deque([int(x) for x in input().split()])

first_seq = fuel.copy()
second_seq = consumption_index.copy()
third_seq = quantities_needed.copy()

reached_altitudes = []

for index in range(len(fuel)):
    if first_seq.pop() - second_seq.popleft() >= third_seq.popleft():
        fuel.pop()
        consumption_index.popleft()
        quantities_needed.popleft()
        print(f"John has reached: Altitude {index + 1}")
        reached_altitudes.append(str(f"Altitude {index + 1}"))
    else:
        print(f"John did not reach: Altitude {index + 1}")
        break

if 1 <= len(reached_altitudes) < 4:
    print("John failed to reach the top.")
    print(f"Reached altitudes: {', '.join(reached_altitudes)}")
elif len(reached_altitudes) <= 0:
    print("John failed to reach the top.")
    print("John didn't reach any altitude.")
elif len(reached_altitudes) >= 4:
    print("John has reached all the altitudes and managed to reach the top!")

