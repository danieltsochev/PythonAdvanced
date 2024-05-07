from collections import deque

daily_food = [int(x) for x in input().split(", ")]
stamina_daily = deque([int(x) for x in input().split(", ")])

peaks_values = deque([80, 90, 100, 60, 70])
peaks_names = deque(["Vihren", "Kutelo", "Banski Suhodol", "Polezhan", "Kamenitza"])

peaks_conquered = deque()

while daily_food and stamina_daily and peaks_names:
    food = daily_food.pop()
    stamina = stamina_daily.popleft()
    sum_food_stamina = food + stamina
    peak_to_climb = peaks_values.popleft()

    if sum_food_stamina >= peak_to_climb:
        peaks_conquered.append(peaks_names.popleft())
    else:
        peaks_values.appendleft(peak_to_climb)


if not peaks_names:
    print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
else:
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")

if peaks_conquered:
    print("Conquered peaks:")
    for i in range(len(peaks_conquered)):
        print(peaks_conquered.popleft())


