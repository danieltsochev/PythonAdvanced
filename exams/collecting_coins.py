from math import floor

SIZE = int(input())

collected_coins = 0

matrix = []
position = []
first_position = []

path = []
check = False

for r in range(SIZE):
    matrix.append([element for element in input().split()])
    if "P" in matrix[r]:
        position.append(r)
        first_position.append(r)
        position.append(matrix[r].index("P"))
        first_position.append(matrix[r].index("P"))

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

while collected_coins < 100 and not check:
    command = input()

    if command not in directions.keys():
        continue

    row = position[0] + directions[command][0]
    col = position[1] + directions[command][1]

    if row < 0:
        row = SIZE - 1
    elif row >= SIZE:
        row = 0

    if col < 0:
        col = SIZE - 1
    elif col >= SIZE:
        col = 0

    position = [row, col]

    path.append(position)

    if matrix[row][col] == "X":
        print(f"Game over! You've collected {floor(collected_coins / 2)} coins.")
        check = True

    elif matrix[position[0]][position[1]].isdigit():
        collected_coins += int(matrix[position[0]][position[1]])
        matrix[position[0]][position[1]] = "-"

path.insert(0, first_position)

if collected_coins >= 100:
    print(f"You won! You've collected {floor(collected_coins)} coins.")

print("Your path:")

for element in path:
    print(element)