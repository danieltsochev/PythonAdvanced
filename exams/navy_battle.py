SIZE = int(input())

matrix = []
position = []

battle_cruisers = 3
mines_reached = 0

for r in range(SIZE):
    matrix.append(list(input()))
    if "S" in matrix[r]:
        position.append(r)
        position.append(matrix[r].index("S"))

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

while battle_cruisers > 0 and mines_reached < 3:
    command = input()

    current_row = position[0] + directions[command][0]
    current_col = position[1] + directions[command][1]

    if 0 <= current_row < SIZE and 0 <= current_col < len(matrix[current_row]):
        if matrix[current_row][current_col] == "*":
            matrix[current_row][current_col] = "-"
            mines_reached += 1

        if matrix[current_row][current_col] == "C":
            matrix[current_row][current_col] = "-"
            battle_cruisers -= 1
        matrix[position[0]][position[1]] = "-"
        position = [current_row, current_col]

    else:
        pass

matrix[position[0]][position[1]] = "S"

if battle_cruisers <= 0:
    print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")

elif mines_reached >= 3:
    print(f"Mission failed, U-9 disappeared! Last known coordinates {position}!")

[print(''.join(row)) for row in matrix]
