from collections import deque

worms = [int(x) for x in input().split()]
holes = deque([int(x) for x in input().split()])

matches_count = 0
all_worms_fit = True

while worms and holes:
    current_worm = worms.pop()
    current_hole = holes.popleft()

    if current_worm == current_hole:
        matches_count += 1

    else:
        current_worm -= 3
        if current_worm > 0:
            worms.append(current_worm)

        all_worms_fit = False

if matches_count > 0:
    print(f"Matches: {matches_count}")
else:
    print("There are no matches.")

if len(worms) <= 0 and all_worms_fit:
    print("Every worm found a suitable hole!")
elif len(worms) <= 0 and not all_worms_fit:
    print("Worms left: none")
elif len(worms) > 0:
    print(f"Worms left: {', '.join([str(x) for x in worms])}")

if len(holes) <= 0:
    print("Holes left: none")
else:
    print(f"Holes left: {', '.join([str(x) for x in holes])}")

