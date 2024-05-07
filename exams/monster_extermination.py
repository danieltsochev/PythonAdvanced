from collections import deque

armor_values = deque([int(x) for x in input().split(",")])
soldier_strike = [int(x) for x in input().split(",")]

monsters_killed = 0

while armor_values and soldier_strike:

    monster = armor_values.popleft()
    soldier = soldier_strike.pop()

    result_both = 0

    if soldier >= monster:

        monsters_killed += 1

        remain_value = 0

        result_both = soldier - monster
        if result_both > 0:
            if soldier_strike:
                remain_value = result_both + soldier_strike.pop()
                soldier_strike.append(remain_value)
            else:
                soldier_strike.append(result_both)

    else:
        result_both = monster - soldier

        armor_values.append(result_both)

if not armor_values:
    print("All monsters have been killed!")

if not soldier_strike:
    print("The soldier has been defeated.")

print(f"Total monsters killed: {monsters_killed}")