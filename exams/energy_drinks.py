from collections import deque

MAX_DOSE = 300

caffeine_milligrams = [int(x) for x in input().split(", ")]
energy_drinks = deque([int(x) for x in input().split(", ")])

total_caffeine = 0

while caffeine_milligrams and energy_drinks:

    current_caffeine = caffeine_milligrams.pop()
    current_drink = energy_drinks.popleft()
    result = current_caffeine * current_drink

    if result + total_caffeine <= MAX_DOSE:
        total_caffeine += result

    else:
        energy_drinks.append(current_drink)
        if total_caffeine - 30 >= 0:
            total_caffeine -= 30

if energy_drinks:
    print(f"Drinks left: {', '.join(str(el) for el in energy_drinks)}")
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")
print(f"Stamat is going to sleep with {total_caffeine} mg caffeine.")