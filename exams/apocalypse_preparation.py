from collections import deque

textiles = deque([int(x) for x in input().split()])
medicament_s = [int(x) for x in input().split()]

items = {"Patch": 0, "Bandage": 0, "MedKit": 0}

while textiles and medicament_s:

    current_textile = textiles.popleft()
    current_medicament = medicament_s.pop()

    result = current_textile + current_medicament

    if result == 30:
        items["Patch"] += 1

    elif result == 40:
        items["Bandage"] += 1

    elif result == 100:
        items["MedKit"] += 1

    elif result > 100:
        items["MedKit"] += 1
        remaining = (result - 100) + medicament_s.pop()
        medicament_s.append(remaining)

    else:
        medicament_s.append(current_medicament + 10)

removing_keys = []

for key, value in items.items():
    if value <= 0:
        removing_keys.append(key)

for element in removing_keys:
    if element in items.keys():
        del items[element]

result = sorted(items.items(), key=lambda x: (-x[1], x[0]))

if not textiles and medicament_s:
    print("Textiles are empty.")
elif not medicament_s and textiles:
    print("Medicaments are empty.")
else:
    print("Textiles and medicaments are both empty.")

if result:
    for result_tuple in result:
        print(f"{result_tuple[0]} - {result_tuple[1]}")
if medicament_s:

    print(f"Medicaments left: {', '.join(str(el) for el in medicament_s[::-1])}")
if textiles:

    print(f"Textiles left: {', '.join(str(el) for el in textiles)}")