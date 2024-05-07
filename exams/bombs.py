from collections import deque

b_effects = deque([int(x) for x in input().split(', ')])
b_casings = [int(x) for x in input().split(', ')]

datura = False
cherry = False
smoke = False

bombs_book = {
    'Datura Bombs': 0,
    'Cherry Bombs': 0,
    'Smoke Decoy Bombs': 0
}

while b_effects and b_casings:

    effect = b_effects.popleft()
    casing = b_casings.pop()

    if effect + casing == 40:
        bombs_book['Datura Bombs'] += 1
        if bombs_book['Datura Bombs'] >= 3:
            datura = True

    elif effect + casing == 60:
        bombs_book['Cherry Bombs'] += 1
        if bombs_book['Cherry Bombs'] >= 3:
            cherry = True

    elif effect + casing == 120:
        bombs_book['Smoke Decoy Bombs'] += 1
        if bombs_book['Smoke Decoy Bombs'] >= 3:
            smoke = True

    else:
        b_effects.appendleft(effect)
        b_casings.append(casing - 5)

    if datura and cherry and smoke:
        print("Bene! You have successfully filled the bomb pouch!")
        break

else:
    print("You don't have enough materials to fill the bomb pouch.")

if not b_effects:
    print("Bomb Effects: empty")
else:
    print(f"Bomb Effects: {', '.join(str(number) for number in b_effects)}")

if not b_casings:
    print("Bomb Casings: empty")
else:
    print(f"Bomb Casings: {', '.join(str(number) for number in b_casings)}")

result = dict(sorted(bombs_book.items(), key=lambda x: (x[0])))

for key, value in result.items():
    print(f"{key}: {value}")