from collections import deque

f_effects = deque([int(x) for x in input().split(", ")])
f_power = [int(x) for x in input().split(", ")]

fireworks = {'Palm Fireworks': 0, 'Willow Fireworks': 0, 'Crossette Fireworks': 0}

palm = False
willow = False
crossette = False
firework_show = False

while f_effects and f_power:

    effect = f_effects.popleft()
    power = f_power.pop()

    if effect <= 0 < power:
        f_power.append(power)
        continue
    elif power <= 0 < effect:
        f_effects.appendleft(effect)
        continue
    elif power <= 0 and effect <= 0:
        continue

    result = effect + power

    if result % 3 == 0 and result % 5 != 0:
        fireworks['Palm Fireworks'] += 1
        if fireworks['Palm Fireworks'] >= 3:
            palm = True

    elif result % 5 == 0 and result % 3 != 0:
        fireworks['Willow Fireworks'] += 1
        if fireworks['Willow Fireworks'] >= 3:
            willow = True

    elif result % 3 == 0 and result % 5 == 0:
        fireworks['Crossette Fireworks'] += 1
        if fireworks['Crossette Fireworks'] >= 3:
            crossette = True

    else:
        f_effects.append(effect - 1)
        f_power.append(power)

    if palm and willow and crossette:
        firework_show = True
        break

if firework_show:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")

if f_effects:
    print(f"Firework Effects left: {', '.join(str(x) for x in f_effects)}")
if f_power:
    print(f"Explosive Power left: {', '.join(str(x) for x in f_power)}")

for key, value in fireworks.items():
    print(f"{key}: {value}")